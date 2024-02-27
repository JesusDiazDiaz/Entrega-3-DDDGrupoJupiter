from dataclasses import field, dataclass

from src.auditoria.seedwork.domain.value_object import ValueObject


@dataclass(frozen=True)
class Characteristics(ValueObject):
    size_sqft: float = field(default_factory=float)
    construction_type: str = field(default_factory=str)
    floors: int = field(default_factory=int)