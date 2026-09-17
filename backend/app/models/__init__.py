"""Registro completo de modelos para SQLAlchemy y Alembic."""

from app.db.base import Base
from app.models.carrito import Carrito, DetalleCarrito, Favorito
from app.models.catalogo import (
    Categoria,
    DefinicionEspecificacion,
    EspecificacionProducto,
    ImagenProducto,
    Marca,
    Producto,
)
from app.models.identidad import CuentaOAuth, Rol, Usuario
from app.models.ventas import DetallePedido, MetodoPago, Pedido

__all__ = [
    "Base",
    "Carrito",
    "Categoria",
    "CuentaOAuth",
    "DefinicionEspecificacion",
    "DetalleCarrito",
    "DetallePedido",
    "EspecificacionProducto",
    "Favorito",
    "ImagenProducto",
    "Marca",
    "MetodoPago",
    "Pedido",
    "Producto",
    "Rol",
    "Usuario",
]
