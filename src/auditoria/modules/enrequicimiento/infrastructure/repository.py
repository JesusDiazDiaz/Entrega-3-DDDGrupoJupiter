from src.auditoria.modules.enrequicimiento.domain.repository import PropertyRepository

from src.auditoria.config.db import db
from src.auditoria.modules.enrequicimiento.domain.entity import Property
from src.auditoria.modules.enrequicimiento.domain.factory import AuditFactory
from .dto import Property as PropertyDto
from .mapper import PropertyMapper


class PropertyRepositoryPostgres(PropertyRepository):
    def __init__(self):
        self._property_factory = AuditFactory()

    @property
    def property_factory(self):
        return self._property_factory


    def update(self, property: Property) -> Property:
        property_dto = db.session.query(PropertyDto).filter(Property.id == property.id)

        property_dto.size_sqft = property.size_sqft
        property_dto.construction_type = property.construction_type
        property_dto.floors = property.floors

        db.session.commit()

        return self.property_factory.create_object(property_dto, PropertyMapper())

