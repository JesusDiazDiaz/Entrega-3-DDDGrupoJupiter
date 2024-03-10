from __future__ import annotations
from dataclasses import dataclass, field
from properties.seedwork.domain.event import (DomainEvent)
from datetime import datetime


class PipelineEvent(DomainEvent):
    ...


@dataclass
class DataValidationCreated(PipelineEvent):
    property_id: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None


@dataclass
class DataValidationCanceled(PipelineEvent):
    property_id: uuid.UUID = None
    fecha_actualizacion: datetime = None


@dataclass
class DataValidationFailed(PipelineEvent):
    property_id: uuid.UUID = None
    fecha_actualizacion: datetime = None
