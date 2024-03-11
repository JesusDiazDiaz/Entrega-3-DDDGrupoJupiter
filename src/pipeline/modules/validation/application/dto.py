from dataclasses import dataclass, field
from typing import List
from src.pipeline.seedwork.application.dto import DTO

@dataclass(frozen=True)
class RentalListingDTO(DTO):
    id: int
    price: float
    availability_date: str
    property_id: int


@dataclass(frozen=True)
class PropertyDTO(DTO):
    id: str
    size_sqft: float
    construction_type: str
    floors: int

