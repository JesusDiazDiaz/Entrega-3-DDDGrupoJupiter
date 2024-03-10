from __future__ import annotations
from dataclasses import dataclass, field
from properties.seedwork.domain.event import (DomainEvent)
from datetime import datetime


class PropertiesEvent(DomainEvent):
    ...


@dataclass
class DatalakeFileCreated(PropertiesEvent):
    property_id: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None


@dataclass
class DatalakeFileCanceled(PropertiesEvent):
    property_id: uuid.UUID = None
    fecha_actualizacion: datetime = None


@dataclass
class DatalakeFileFailed(PropertiesEvent):
    property_id: uuid.UUID = None
    fecha_actualizacion: datetime = None