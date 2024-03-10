from __future__ import annotations
from dataclasses import dataclass, field
from properties.seedwork.domain.event import (DomainEvent)
from datetime import datetime

class EventoPago(DomainEvent):
    ...

@dataclass
class ReservaPagada(EventoPago):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    monto: float = None
    monto_vat: float = None
    fecha_actualizacion: datetime = None

@dataclass
class PagoFallido(EventoPago):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    monto: float = None
    monto_vat: float = None
    fecha_actualizacion: datetime = None

@dataclass
class PagoRevertido(EventoPago):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    monto: float = None
    monto_vat: float = None
    fecha_actualizacion: datetime = None