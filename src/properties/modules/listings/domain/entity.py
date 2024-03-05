import datetime
import uuid
from typing import Dict


from src.properties.modules.listings.domain.event.listing import ListingDataRecovered
from src.properties.seedwork.domain.aggregate_root import AggregateRoot
from dataclasses import dataclass, field



@dataclass
class Listing(AggregateRoot):
    property_id: uuid.UUID = field(default_factory=uuid.uuid4)
    data: Dict = field(default_factory=dict)

    def data_recovered(self, _property):
        self.data = _property.data

        self.add_event(
            ListingDataRecovered(
                property_id=self.property_id,
            )
        )
