"""Modelos del MVP según el DBML aprobado."""

from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Index,
    String,
    Text,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Rol(Base):
    __tablename__ = "roles"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    codigo: Mapped[str] = mapped_column(String(50), nullable=False)

    nombre: Mapped[str] = mapped_column(String(80), nullable=False)

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
        UniqueConstraint("codigo", name="uq_roles_codigo"),
        UniqueConstraint("nombre", name="uq_roles_nombre"),
    )

    usuarios = relationship(
        "Usuario", back_populates="rol", passive_deletes="all", lazy="raise"
    )


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    rol_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("roles.id", name="fk_usuarios_rol", ondelete="RESTRICT"),
        nullable=False,
    )

    correo_electronico: Mapped[str] = mapped_column(String(320), nullable=False)

    nombre_completo: Mapped[str] = mapped_column(String(150), nullable=False)

    hash_contrasena: Mapped[str | None] = mapped_column(String(255), nullable=True)

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
        Index("ix_usuarios_rol_id", "rol_id"),
        UniqueConstraint("correo_electronico", name="uq_usuarios_correo_electronico"),
    )

    rol = relationship("Rol", back_populates="usuarios", lazy="raise")

    cuentas_oauth = relationship(
        "CuentaOAuth", back_populates="usuario", passive_deletes="all", lazy="raise"
    )

    favoritos = relationship(
        "Favorito", back_populates="usuario", passive_deletes="all", lazy="raise"
    )

    pedidos = relationship(
        "Pedido", back_populates="usuario", passive_deletes="all", lazy="raise"
    )

    carritos = relationship(
        "Carrito",
        back_populates="usuario",
        passive_deletes="all",
        lazy="raise",
        uselist=False,
    )


class CuentaOAuth(Base):
    __tablename__ = "cuentas_oauth"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()"),
    )

    usuario_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("usuarios.id", name="fk_cuentas_oauth_usuario", ondelete="CASCADE"),
        nullable=False,
    )

    proveedor: Mapped[str] = mapped_column(String(50), nullable=False)

    identificador_proveedor: Mapped[str] = mapped_column(String(255), nullable=False)

    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )

    __table_args__ = (
        UniqueConstraint(
            "proveedor",
            "identificador_proveedor",
            name="uq_cuentas_oauth_proveedor_identificador",
        ),
        UniqueConstraint(
            "usuario_id", "proveedor", name="uq_cuentas_oauth_usuario_proveedor"
        ),
    )

    usuario = relationship("Usuario", back_populates="cuentas_oauth", lazy="raise")
