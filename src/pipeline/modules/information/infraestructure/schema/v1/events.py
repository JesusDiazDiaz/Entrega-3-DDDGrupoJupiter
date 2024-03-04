import uuid

from pulsar.schema import *
from src.pipeline.seedwork.infrastructure.schema.v1.events import IntegrationEvent
from src.pipeline.seedwork.infrastructure.utils import time_millis

class EnrichedInformationPayload(Record):
    property_id = String()


class EnrichedInformationEvent(IntegrationEvent):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EnrichedInformationPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)