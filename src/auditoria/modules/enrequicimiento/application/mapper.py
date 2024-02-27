
from src.auditoria.seedwork.application.dto import Mapper as AppMap

from src.auditoria.modules.enrequicimiento.domain.entity import Property
from src.auditoria.modules.enrequicimiento.domain.value_object import Characteristics
from src.auditoria.seedwork.domain.entity import Entity
from src.auditoria.seedwork.domain.repository import Mapper as RepMap

from .dto import PropertyDTO


class PropertyDTOJson(AppMap):
    def external_to_dto(self, external) -> PropertyDTO:
        return PropertyDTO(
            id=external["id"],
            size_sqft=external["size_sqft"],
            construction_type=external["construction_type"],
            floors=external["floors"]
        )

    def dto_to_external(self, dto: PropertyDTO) -> dict:
        return dto.__dict__


class PropertyMapper(RepMap):
    def entity_to_dto(self, entity: Property) -> PropertyDTO:
        return PropertyDTO(
            id=entity.id,
            size_sqft=entity.characteristics.size_sqft,
            construction_type=entity.characteristics.construction_type,
            floors=entity.characteristics.floors,
        )

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