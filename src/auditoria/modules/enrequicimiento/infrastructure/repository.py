from uuid import UUID
import logging
from src.auditoria.modules.enrequicimiento.domain.repository import PropertyRepository

from src.auditoria.config.db import db
from src.auditoria.modules.enrequicimiento.domain.entity import Property
from src.auditoria.modules.enrequicimiento.domain.factory import AuditFactory
from .dto import Property as PropertyDto
from .mapper import PropertyMapper

LOGGER = logging.getLogger()


class PropertyRepositoryPostgres(PropertyRepository):
    def __init__(self):
        self._property_factory = AuditFactory()

    def add(self, entity):
        raise NotImplementedError

    def get(self, id: UUID):
        raise NotImplementedError

    def remove(self, entity):
        raise NotImplementedError

    @property
    def property_factory(self):
        return self._property_factory

    def get_all(self):
        properties = db.session.query(PropertyDto).all()
        return [self.property_factory.create_object(property, PropertyMapper()) for property in properties]

    def update(self, id, property: Property) -> Property:
        LOGGER.info(f"update property: {property}")

        property_dto = db.session.query(PropertyDto).get(id)

        LOGGER.info(f"update property_dto: {property.id}, {property_dto.construction_type}")

        property_dto.size_sqft = property.characteristics.size_sqft
        property_dto.construction_type = property.characteristics.construction_type
        property_dto.floors = property.characteristics.floors

        db.session.commit()

        return self.property_factory.create_object(property_dto, PropertyMapper())
