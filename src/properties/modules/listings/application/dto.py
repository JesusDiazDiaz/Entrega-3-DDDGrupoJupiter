from dataclasses import dataclass, field

from src.properties.seedwork.application.dto import DTO


@dataclass(frozen=True)
class ListingDTO(DTO):
    property_id: str = field(default_factory=str)
    extra_data: dict = field(default_factory=dict)