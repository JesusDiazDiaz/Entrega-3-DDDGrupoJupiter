from uuid import UUID
import logging
from src.pipeline.modules.validation.domain.repository import PropertyRepository

from src.pipeline.config.db import db
from src.pipeline.modules.validation.domain.entity import Property
from src.pipeline.modules.validation.domain.factory import AuditFactory
from .dto import Property as PropertyDto
from .mapper import ListingMapper

LOGGER = logging.getLogger()


class PropertyRepositoryPostgres(PropertyRepository):
    def __init__(self):
        self._property_factory = AuditFactory()

    def add(self, entity):
        property_dto = self.property_factory.create_object(entity, ListingMapper())
        db.session.add(property_dto)

    def get(self, id: UUID):
        raise NotImplementedError

    def remove(self, entity):
        raise NotImplementedError

    @property
    def property_factory(self):
        return self._property_factory

    def get_all(self):
        raise NotImplementedError

    def update(self, id, property: Property) -> None:
        LOGGER.info(f"update property: {property}")

        property_dto = db.session.query(PropertyDto).get(id)

        LOGGER.info(f"update property_dto: {property.id}, {property_dto.construction_type}")

        property_dto.size_sqft = property.characteristics.size_sqft
        property_dto.construction_type = property.characteristics.construction_type
        property_dto.floors = property.characteristics.floors

        db.session.add(property_dto)

        # db.session.commit()

        # return self.property_factory.create_object(property_dto, PropertyMapper())
