import uuid
from dataclasses import dataclass

from src.properties.seedwork.domain.event import IntegrationEvent

class ListingEvent(IntegrationEvent):
    ...


@dataclass
class ListingDataRecovered(ListingEvent):
    property_id: uuid.UUID = None