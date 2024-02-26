from src.auditoria.seedwork.domain.aggregate_root import AggregateRoot
from dataclasses import dataclass, field

from src.auditoria.modules.enrequicimiento.domain.value_object import Characteristics


@dataclass
class Property(AggregateRoot):
    characteristics: Characteristics = field(default_factory=Characteristics)