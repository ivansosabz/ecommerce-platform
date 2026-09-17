from enum import StrEnum


class EstadoPedido(StrEnum):
    PENDIENTE = "pendiente"
    CONFIRMADO = "confirmado"
    EN_PREPARACION = "en_preparacion"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"
