"""Pruebas de integración sobre una base de pruebas previamente migrada.

Se habilitan únicamente mediante TEST_DATABASE_URL. Cada prueba revierte sus datos.
"""

import asyncio
import os
from decimal import Decimal
from uuid import uuid4

import pytest
from sqlalchemy import create_engine, delete, insert, select, update
from sqlalchemy.exc import IntegrityError

from app.core.config import Settings
from app.core.event_loop import create_event_loop
from app.db.session import Database
from app.models import Base, Categoria, Marca, Producto, Usuario


@pytest.fixture
def connection():
    url = os.environ.get("TEST_DATABASE_URL")
    if not url:
        pytest.skip("Definir TEST_DATABASE_URL para ejecutar contra PostgreSQL")
    engine = create_engine(url)
    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            yield connection
        finally:
            transaction.rollback()
    engine.dispose()


def add(connection, table, **values):
    return connection.execute(
        insert(Base.metadata.tables[table])
        .values(**values)
        .returning(Base.metadata.tables[table].c.id)
    ).scalar_one()


@pytest.fixture
def data(connection):
    suffix = uuid4().hex
    role = add(connection, "roles", codigo=suffix, nombre=suffix)
    user = add(
        connection,
        "usuarios",
        rol_id=role,
        correo_electronico=f"{suffix}@test.local",
        nombre_completo="Prueba",
    )
    category = add(connection, "categorias", nombre="Prueba", slug=suffix)
    brand = add(connection, "marcas", nombre=suffix, slug=suffix)
    product = add(
        connection,
        "productos",
        categoria_id=category,
        marca_id=brand,
        nombre="Producto original",
        slug=suffix,
        precio=Decimal("100.50"),
    )
    cart = add(connection, "carritos", usuario_id=user)
    payment = add(connection, "metodos_pago", codigo=suffix, nombre=suffix)
    order = add(
        connection,
        "pedidos",
        usuario_id=user,
        metodo_pago_id=payment,
        moneda="PYG",
        subtotal=Decimal(201),
        total=Decimal(201),
        destinatario_envio="Prueba",
        telefono_envio="123",
        direccion_envio_linea_1="Prueba",
        ciudad_envio="Prueba",
        region_envio="Prueba",
        codigo_pais_envio="PY",
    )
    return {
        "role": role,
        "user": user,
        "category": category,
        "brand": brand,
        "product": product,
        "cart": cart,
        "payment": payment,
        "order": order,
    }


@pytest.mark.parametrize(
    "table,values,constraint",
    [
        ("productos", {"precio": -1}, "ck_productos_precio_no_negativo"),
        ("productos", {"existencias": -1}, "ck_productos_existencias_no_negativas"),
        ("detalles_carrito", {"cantidad": 0}, "ck_detalles_carrito_cantidad_positiva"),
        ("pedidos", {"total": 0}, "ck_pedidos_total_consistente"),
    ],
)
def test_database_rejects_invalid_amounts(connection, data, table, values, constraint):
    record_id = data[{"productos": "product", "pedidos": "order"}.get(table, "cart")]
    with pytest.raises(IntegrityError) as error, connection.begin_nested():
        target = Base.metadata.tables[table]
        if table == "detalles_carrito":
            connection.execute(
                insert(target).values(
                    carrito_id=data["cart"], producto_id=data["product"], **values
                )
            )
        else:
            connection.execute(
                update(target).where(target.c.id == record_id).values(**values)
            )
    assert error.value.orig.diag.constraint_name == constraint


def test_one_cart_per_user(connection, data):
    with pytest.raises(IntegrityError) as error, connection.begin_nested():
        add(connection, "carritos", usuario_id=data["user"])
    assert error.value.orig.diag.constraint_name == "uq_carritos_usuario_id"


def test_duplicate_favorites_are_rejected(connection, data):
    add(connection, "favoritos", usuario_id=data["user"], producto_id=data["product"])
    with pytest.raises(IntegrityError) as error, connection.begin_nested():
        add(
            connection,
            "favoritos",
            usuario_id=data["user"],
            producto_id=data["product"],
        )
    assert error.value.orig.diag.constraint_name == "uq_favoritos_usuario_producto"


def test_product_delete_preserves_order_history(connection, data):
    detail = add(
        connection,
        "detalles_pedido",
        pedido_id=data["order"],
        producto_id=data["product"],
        nombre_producto="Producto original",
        precio_unitario=Decimal("100.50"),
        cantidad=2,
        subtotal=Decimal(201),
    )
    image = add(
        connection,
        "imagenes_producto",
        producto_id=data["product"],
        url="https://example.com/test.png",
    )
    add(connection, "favoritos", usuario_id=data["user"], producto_id=data["product"])
    add(
        connection,
        "detalles_carrito",
        carrito_id=data["cart"],
        producto_id=data["product"],
    )
    connection.execute(
        update(Producto)
        .where(Producto.id == data["product"])
        .values(nombre="Nombre nuevo", precio=500)
    )
    connection.execute(delete(Producto).where(Producto.id == data["product"]))
    details = Base.metadata.tables["detalles_pedido"]
    row = (
        connection.execute(select(details).where(details.c.id == detail))
        .mappings()
        .one()
    )
    assert row["producto_id"] is None
    assert row["nombre_producto"] == "Producto original"
    assert row["precio_unitario"] == Decimal("100.50")
    assert row["subtotal"] == Decimal(201)
    images = Base.metadata.tables["imagenes_producto"]
    assert (
        connection.execute(select(images).where(images.c.id == image)).first() is None
    )
    for name in ("favoritos", "detalles_carrito"):
        table = Base.metadata.tables[name]
        assert (
            connection.execute(
                select(table).where(table.c.producto_id == data["product"])
            ).first()
            is None
        )


def test_order_restricts_user_deletion(connection, data):
    with pytest.raises(IntegrityError) as error, connection.begin_nested():
        connection.execute(delete(Usuario).where(Usuario.id == data["user"]))
    assert error.value.orig.diag.constraint_name == "fk_pedidos_usuario"


def test_async_orm_roundtrip_and_rollback():
    url = os.environ.get("TEST_DATABASE_URL")
    if not url:
        pytest.skip("Definir TEST_DATABASE_URL para ejecutar contra PostgreSQL")

    async def exercise():
        database = Database(Settings(database_url=url))
        suffix = uuid4().hex
        try:
            with pytest.raises(ValueError, match="rollback"):
                async with database.session() as session:
                    category = Categoria(nombre="Prueba", slug=suffix)
                    brand = Marca(nombre=suffix, slug=suffix)
                    session.add_all([category, brand])
                    await session.flush()
                    product = Producto(
                        categoria_id=category.id,
                        marca_id=brand.id,
                        nombre="Prueba",
                        slug=suffix,
                        precio=Decimal("123.45"),
                    )
                    session.add(product)
                    await session.flush()
                    await session.refresh(product)
                    assert product.precio == Decimal("123.45")
                    assert product.existencias == 0
                    assert product.creado_en.tzinfo is not None
                    assert (
                        await session.scalar(
                            select(Producto).where(Producto.id == product.id)
                        )
                    ) is product
                    raise ValueError("rollback")
            async with database.session() as session:
                assert (
                    await session.scalar(
                        select(Producto).where(Producto.slug == suffix)
                    )
                    is None
                )
        finally:
            await database.dispose()

    asyncio.run(exercise(), loop_factory=create_event_loop)
