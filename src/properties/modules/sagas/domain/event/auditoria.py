from __future__ import annotations
from dataclasses import dataclass, field
from properties.seedwork.domain.event import (DomainEvent)
from datetime import datetime

class EventoGDS(DomainEvent):
    ...

@dataclass
class ReservaGDSConfirmada(EventoGDS):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    fecha_actualizacion: datetime = None

@dataclass
class ConfirmacionGDSRevertida(EventoGDS):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    fecha_actualizacion: datetime = None

@dataclass
class ConfirmacionFallida(EventoGDS):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    fecha_actualizacion: datetime = None