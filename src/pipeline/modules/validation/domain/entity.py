import datetime

from src.pipeline.modules.validation.domain.events.information import CleanedData
from src.pipeline.seedwork.domain.aggregate_root import AggregateRoot
from dataclasses import dataclass, field

from src.auditoria.modules.enrequicimiento.domain.value_object import Characteristics


@dataclass
class Property(AggregateRoot):
    characteristics: Characteristics = field(default_factory=Characteristics)

    def enrich_information(self, _property):
        self.characteristics = _property.characteristics

        self.add_event(
            CleanedData(
                property_id=self.id,
            )
        )
