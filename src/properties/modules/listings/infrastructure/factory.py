from dataclasses import dataclass
from src.properties.seedwork.domain.factory import Factory
from src.properties.seedwork.domain.repository import Repository
from .exceptions import ImplementationNotExistsForFactoryException
from .repository import ListingRepositoryPostgres
from ..domain.repository import ListingRepository

@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == ListingRepository.__class__:
            return ListingRepositoryPostgres()

        raise ImplementationNotExistsForFactoryException()