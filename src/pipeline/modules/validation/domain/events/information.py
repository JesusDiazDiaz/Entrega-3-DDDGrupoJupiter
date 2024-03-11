import uuid
from dataclasses import dataclass
from datetime import datetime

from src.pipeline.seedwork.domain.event import DomainEvent


class PropertyEvent(DomainEvent):
    ...



# TODO: Add Fields
@dataclass
class CleanedData(PropertyEvent):
    property_id: uuid.UUID = None