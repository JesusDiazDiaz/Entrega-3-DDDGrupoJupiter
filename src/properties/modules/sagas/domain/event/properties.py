from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime

from src.properties.seedwork.domain.event import DomainEvent


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