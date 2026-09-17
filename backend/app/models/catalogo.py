"""Modelos del MVP según el DBML aprobado."""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    SmallInteger,
    String,
    Text,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    categoria_padre_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("categorias.id", name="fk_categorias_padre", ondelete="RESTRICT"),
        nullable=True,
    )

    nombre: Mapped[str] = mapped_column(String(120), nullable=False)

    slug: Mapped[str] = mapped_column(String(140), nullable=False)

    esta_activo: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),
        onupdate=func.now(),
    )

    __table_args__ = (UniqueConstraint("slug", name="uq_categorias_slug"),)

    categoria_padre = relationship(
        "Categoria",
        back_populates="subcategorias",
        lazy="raise",
        remote_side="Categoria.id",
    )

    subcategorias = relationship(
        "Categoria",
        back_populates="categoria_padre",
        passive_deletes="all",
        lazy="raise",
    )

    productos = relationship(
        "Producto", back_populates="categoria", passive_deletes="all", lazy="raise"
    )


class Marca(Base):
    __tablename__ = "marcas"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    nombre: Mapped[str] = mapped_column(String(120), nullable=False)

    slug: Mapped[str] = mapped_column(String(140), nullable=False)

    esta_activo: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),
        onupdate=func.now(),
    )

    __table_args__ = (
        UniqueConstraint("nombre", name="uq_marcas_nombre"),
        UniqueConstraint("slug", name="uq_marcas_slug"),
    )

    productos = relationship(
        "Producto", back_populates="marca", passive_deletes="all", lazy="raise"
    )


class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    categoria_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("categorias.id", name="fk_productos_categoria", ondelete="RESTRICT"),
        nullable=False,
    )

    marca_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("marcas.id", name="fk_productos_marca", ondelete="RESTRICT"),
        nullable=False,
    )

    nombre: Mapped[str] = mapped_column(String(200), nullable=False)

    slug: Mapped[str] = mapped_column(String(220), nullable=False)

    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)

    precio: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)

    existencias: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default=text("0")
    )

    esta_activo: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),
        onupdate=func.now(),
    )

    __table_args__ = (
        Index("ix_productos_categoria_id", "categoria_id"),
        Index("ix_productos_marca_id", "marca_id"),
        Index("ix_productos_nombre", "nombre"),
        Index("ix_productos_precio", "precio"),
        CheckConstraint("precio >= 0", name="ck_productos_precio_no_negativo"),
        CheckConstraint(
            "existencias >= 0", name="ck_productos_existencias_no_negativas"
        ),
        UniqueConstraint("slug", name="uq_productos_slug"),
    )

    categoria = relationship("Categoria", back_populates="productos", lazy="raise")

    marca = relationship("Marca", back_populates="productos", lazy="raise")

    imagenes_producto = relationship(
        "ImagenProducto", back_populates="producto", passive_deletes="all", lazy="raise"
    )

    especificaciones_producto = relationship(
        "EspecificacionProducto",
        back_populates="producto",
        passive_deletes="all",
        lazy="raise",
    )

    favoritos = relationship(
        "Favorito", back_populates="producto", passive_deletes="all", lazy="raise"
    )

    detalles_carrito = relationship(
        "DetalleCarrito", back_populates="producto", passive_deletes="all", lazy="raise"
    )

    detalles_pedido = relationship(
        "DetallePedido", back_populates="producto", passive_deletes="all", lazy="raise"
    )


class ImagenProducto(Base):
    __tablename__ = "imagenes_producto"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    producto_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey(
            "productos.id", name="fk_imagenes_producto_producto", ondelete="CASCADE"
        ),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(String(2048), nullable=False)

    texto_alternativo: Mapped[str | None] = mapped_column(String(255), nullable=True)

    orden: Mapped[int] = mapped_column(
        SmallInteger, nullable=False, server_default=text("0")
    )

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    __table_args__ = (
        UniqueConstraint("producto_id", "orden", name="uq_imagenes_producto_orden"),
        CheckConstraint("orden >= 0", name="ck_imagenes_producto_orden_no_negativo"),
    )

    producto = relationship(
        "Producto", back_populates="imagenes_producto", lazy="raise"
    )


class DefinicionEspecificacion(Base):
    __tablename__ = "definiciones_especificacion"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    nombre: Mapped[str] = mapped_column(String(120), nullable=False)

    slug: Mapped[str] = mapped_column(String(140), nullable=False)

    unidad: Mapped[str | None] = mapped_column(String(40), nullable=True)

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),
        onupdate=func.now(),
    )

    __table_args__ = (
        UniqueConstraint("slug", name="uq_definiciones_especificacion_slug"),
    )

    especificaciones_producto = relationship(
        "EspecificacionProducto",
        back_populates="definicion_especificacion",
        passive_deletes="all",
        lazy="raise",
    )


class EspecificacionProducto(Base):
    __tablename__ = "especificaciones_producto"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    producto_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey(
            "productos.id",
            name="fk_especificaciones_producto_producto",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    definicion_especificacion_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey(
            "definiciones_especificacion.id",
            name="fk_especificaciones_producto_definicion",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    valor: Mapped[str] = mapped_column(String(255), nullable=False)

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),
        onupdate=func.now(),
    )

    __table_args__ = (
        UniqueConstraint(
            "producto_id",
            "definicion_especificacion_id",
            name="uq_especificaciones_producto",
        ),
    )

    producto = relationship(
        "Producto", back_populates="especificaciones_producto", lazy="raise"
    )

    definicion_especificacion = relationship(
        "DefinicionEspecificacion",
        back_populates="especificaciones_producto",
        lazy="raise",
    )
