import uuid
from dataclasses import dataclass

from src.pipeline.seedwork.domain.event import DomainEvent

class ListingEvent(DomainEvent):
    ...


@dataclass
class ListingDataRecovered(ListingEvent):
    property_id: uuid.UUID = None