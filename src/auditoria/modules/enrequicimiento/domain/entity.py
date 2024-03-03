import datetime

from src.auditoria.modules.enrequicimiento.domain.events.information import EnrichedInformation
from src.auditoria.seedwork.domain.aggregate_root import AggregateRoot
from dataclasses import dataclass, field

from src.auditoria.modules.enrequicimiento.domain.value_object import Characteristics


@dataclass
class Property(AggregateRoot):
    characteristics: Characteristics = field(default_factory=Characteristics)

    def enrich_information(self, _property):
        self.characteristics = _property.characteristics

        self.add_event(
            EnrichedInformation(
                property_id=self.id,
            )
        )
