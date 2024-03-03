import uuid
from dataclasses import dataclass
from datetime import datetime

from src.auditoria.seedwork.domain.event import DomainEvent


class PropertyEvent(DomainEvent):
    ...



# TODO: Add Fields
@dataclass
class EnrichedInformation(PropertyEvent):
    property_id: uuid.UUID = None