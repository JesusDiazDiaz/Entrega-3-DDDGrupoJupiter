from dataclasses import dataclass

from src.pipeline.seedwork.domain.factory import Factory
from src.pipeline.seedwork.domain.repository import Mapper

from src.pipeline.seedwork.domain.entity import Entity
from .entity import Property
from .exceptions import InvalidTypeInAuditDomainException


@dataclass
class _AuditFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            entity: Entity = mapper.dto_to_entity(obj)
            return entity


@dataclass
class AuditFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if mapper.get_type() == Property.__class__:
            audit_factory = _AuditFactory()
            return audit_factory.create_object(obj, mapper)

        return InvalidTypeInAuditDomainException