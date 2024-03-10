from __future__ import annotations
from dataclasses import dataclass, field
from properties.seedwork.domain.event import (DomainEvent)
from datetime import datetime


class AuditoriaEvent(DomainEvent):
    ...


@dataclass
class DataEnrichmentCreated(AuditoriaEvent):
    property_id: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None


@dataclass
class DataEnrichmentCanceled(AuditoriaEvent):
    property_id: uuid.UUID = None
    fecha_actualizacion: datetime = None


@dataclass
class DataEnrichmentFailed(AuditoriaEvent):
    property_id: uuid.UUID = None
    fecha_actualizacion: datetime = None