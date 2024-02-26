from src.auditoria.modules.enrequicimiento.domain.entity import Property
from src.auditoria.modules.enrequicimiento.domain.value_object import Characteristics
from src.auditoria.seedwork.domain.repository import Mapper
from .dto import Property as PropertyDTO


class PropertyMapper(Mapper):
    def entity_to_dto(self, entity: Property) -> PropertyDTO:
        dto = PropertyDTO()
        dto.size_sqft = entity.characteristics.size_sqft
        dto.construction_type = entity.characteristics.construction_type
        dto.floors = entity.characteristics.floors
        return dto

    def dto_to_entity(self, dto: PropertyDTO) -> Property:
        property = Property()
        property.characteristics = Characteristics(
            size_sqft=dto.size_sqft,
            construction_type=dto.construction_type,
            floors=dto.floors,
        )

        return property

    def get_type(self) -> type:
        return Property.__class__