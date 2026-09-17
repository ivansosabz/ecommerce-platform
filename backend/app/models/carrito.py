"""Modelos del MVP según el DBML aprobado."""

from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Favorito(Base):
    __tablename__ = "favoritos"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    usuario_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("usuarios.id", name="fk_favoritos_usuario", ondelete="CASCADE"),
        nullable=False,
    )

    producto_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("productos.id", name="fk_favoritos_producto", ondelete="CASCADE"),
        nullable=False,
    )

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    __table_args__ = (
        UniqueConstraint(
            "usuario_id", "producto_id", name="uq_favoritos_usuario_producto"
        ),
    )

    usuario = relationship("Usuario", back_populates="favoritos", lazy="raise")

    producto = relationship("Producto", back_populates="favoritos", lazy="raise")


class Carrito(Base):
    __tablename__ = "carritos"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    usuario_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("usuarios.id", name="fk_carritos_usuario", ondelete="CASCADE"),
        nullable=False,
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

    __table_args__ = (UniqueConstraint("usuario_id", name="uq_carritos_usuario_id"),)

    detalles_carrito = relationship(
        "DetalleCarrito", back_populates="carrito", passive_deletes="all", lazy="raise"
    )

    usuario = relationship("Usuario", back_populates="carritos", lazy="raise")


class DetalleCarrito(Base):
    __tablename__ = "detalles_carrito"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    carrito_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey(
            "carritos.id", name="fk_detalles_carrito_carrito", ondelete="CASCADE"
        ),
        nullable=False,
    )

    producto_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey(
            "productos.id", name="fk_detalles_carrito_producto", ondelete="CASCADE"
        ),
        nullable=False,
    )

    cantidad: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default=text("1")
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
        UniqueConstraint(
            "carrito_id", "producto_id", name="uq_detalles_carrito_producto"
        ),
        CheckConstraint("cantidad > 0", name="ck_detalles_carrito_cantidad_positiva"),
    )

    carrito = relationship("Carrito", back_populates="detalles_carrito", lazy="raise")

    producto = relationship("Producto", back_populates="detalles_carrito", lazy="raise")
