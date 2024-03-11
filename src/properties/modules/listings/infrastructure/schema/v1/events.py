import uuid

from pulsar.schema import *
from src.properties.seedwork.infrastructure.schema.v1.events import IntegrationEvent
from src.properties.seedwork.infrastructure.utils import time_millis

class ListingDataRecoveredPayload(Record):
    property_id = String()


class ListingDataRecoveredEvent(IntegrationEvent):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ListingDataRecoveredPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)