"""Modelos del MVP según el DBML aprobado."""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import (
    CHAR,
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import EstadoPedido


class MetodoPago(Base):
    __tablename__ = "metodos_pago"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    codigo: Mapped[str] = mapped_column(String(50), nullable=False)

    nombre: Mapped[str] = mapped_column(String(100), nullable=False)

    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)

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
        UniqueConstraint("codigo", name="uq_metodos_pago_codigo"),
        UniqueConstraint("nombre", name="uq_metodos_pago_nombre"),
    )

    pedidos = relationship(
        "Pedido", back_populates="metodo_pago", passive_deletes="all", lazy="raise"
    )


class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    usuario_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("usuarios.id", name="fk_pedidos_usuario", ondelete="RESTRICT"),
        nullable=False,
    )

    metodo_pago_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey(
            "metodos_pago.id", name="fk_pedidos_metodo_pago", ondelete="RESTRICT"
        ),
        nullable=False,
    )

    estado: Mapped[EstadoPedido] = mapped_column(
        ENUM(
            EstadoPedido,
            name="estado_pedido",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
        server_default=text("'pendiente'"),
    )

    moneda: Mapped[str] = mapped_column(CHAR(3), nullable=False)

    subtotal: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)

    importe_envio: Mapped[Decimal] = mapped_column(
        Numeric(14, 2), nullable=False, server_default=text("0")
    )

    total: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)

    destinatario_envio: Mapped[str] = mapped_column(String(150), nullable=False)

    telefono_envio: Mapped[str] = mapped_column(String(40), nullable=False)

    direccion_envio_linea_1: Mapped[str] = mapped_column(String(255), nullable=False)

    direccion_envio_linea_2: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )

    ciudad_envio: Mapped[str] = mapped_column(String(120), nullable=False)

    region_envio: Mapped[str] = mapped_column(String(120), nullable=False)

    codigo_postal_envio: Mapped[str | None] = mapped_column(String(20), nullable=True)

    codigo_pais_envio: Mapped[str] = mapped_column(CHAR(2), nullable=False)

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
        Index("ix_pedidos_usuario_id", "usuario_id"),
        Index("ix_pedidos_metodo_pago_id", "metodo_pago_id"),
        Index("ix_pedidos_estado", "estado"),
        Index("ix_pedidos_creado_en", "creado_en"),
        CheckConstraint("subtotal >= 0", name="ck_pedidos_subtotal_no_negativo"),
        CheckConstraint(
            "importe_envio >= 0", name="ck_pedidos_importe_envio_no_negativo"
        ),
        CheckConstraint("total >= 0", name="ck_pedidos_total_no_negativo"),
        CheckConstraint(
            "total = subtotal + importe_envio", name="ck_pedidos_total_consistente"
        ),
    )

    usuario = relationship("Usuario", back_populates="pedidos", lazy="raise")

    metodo_pago = relationship("MetodoPago", back_populates="pedidos", lazy="raise")

    detalles_pedido = relationship(
        "DetallePedido", back_populates="pedido", passive_deletes="all", lazy="raise"
    )


class DetallePedido(Base):
    __tablename__ = "detalles_pedido"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    pedido_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("pedidos.id", name="fk_detalles_pedido_pedido", ondelete="CASCADE"),
        nullable=False,
    )

    producto_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey(
            "productos.id", name="fk_detalles_pedido_producto", ondelete="SET NULL"
        ),
        nullable=True,
    )

    nombre_producto: Mapped[str] = mapped_column(String(200), nullable=False)

    precio_unitario: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)

    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)

    subtotal: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    __table_args__ = (
        Index("ix_detalles_pedido_pedido_id", "pedido_id"),
        Index("ix_detalles_pedido_producto_id", "producto_id"),
        CheckConstraint(
            "precio_unitario >= 0", name="ck_detalles_pedido_precio_no_negativo"
        ),
        CheckConstraint("cantidad > 0", name="ck_detalles_pedido_cantidad_positiva"),
        CheckConstraint(
            "subtotal = precio_unitario * cantidad",
            name="ck_detalles_pedido_subtotal_consistente",
        ),
    )

    pedido = relationship("Pedido", back_populates="detalles_pedido", lazy="raise")

    producto = relationship("Producto", back_populates="detalles_pedido", lazy="raise")
