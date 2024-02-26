from src.auditoria.seedwork.application.services import Service

from .dto import PropertyDTO
from .mapper import PropertyMapper
from ..domain.entity import Property
from ..domain.factory import AuditFactory
from ..domain.repository import PropertyRepository
from ..infrastructure.factory import RepositoryFactory


class PropertyService(Service):

    def __init__(self):
        self._repository_factory = RepositoryFactory()
        self._audit_factory = AuditFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def audit_factory(self):
        return self._audit_factory

    def update_property(self, property_dto: PropertyDTO) -> PropertyDTO:
        property: Property = self.audit_factory.create_object(property_dto, PropertyMapper())

        repository = self.repository_factory.create_object(PropertyRepository.__class__)
        repository.update(property)

        return self.audit_factory.create_object(property, PropertyMapper())
