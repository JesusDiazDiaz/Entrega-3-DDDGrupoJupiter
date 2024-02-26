from dataclasses import dataclass

from src.auditoria.seedwork.domain.factory import Factory
from src.auditoria.seedwork.domain.repository import Repository
from src.auditoria.seedwork.domain.repository import PropertyRepository

from .exceptions import ImplementationNotExistsForFactoryException
from .repository import PropertyRepositoryPostgres


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == PropertyRepository.__class__:
            return PropertyRepositoryPostgres()

        raise ImplementationNotExistsForFactoryException()