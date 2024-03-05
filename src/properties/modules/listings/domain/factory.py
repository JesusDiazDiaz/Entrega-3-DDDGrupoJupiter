
from dataclasses import dataclass

from src.properties.seedwork.domain.entity import Entity
from src.properties.seedwork.domain.factory import Factory
from src.properties.seedwork.domain.repository import Mapper
from .entity import Listing
from .exceptions import InvalidTypeInAuditDomainException


@dataclass
class _PropertiesFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            entity: Entity = mapper.dto_to_entity(obj)
            return entity


@dataclass
class PropertiesFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if mapper.get_type() == Listing.__class__:
            properties_factory = _PropertiesFactory()
            return properties_factory.create_object(obj, mapper)

        return InvalidTypeInAuditDomainException