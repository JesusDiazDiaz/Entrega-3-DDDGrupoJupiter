from uuid import UUID

from src.properties.modules.listings.domain.repository import ListingRepository
from src.properties.modules.listings.domain.factory import PropertiesFactory
from src.properties.config.db import db
from .mapper import ListingMapper
from ..domain.entity import Listing


class ListingRepositoryPostgres(ListingRepository):
    def __init__(self):
        self._properties_factory = PropertiesFactory()

    @property
    def properties_factory(self):
        return self._properties_factory

    def add(self, entity: Listing):
        listing_dto = self.properties_factory.create_object(entity, ListingMapper())
        db.session.add(listing_dto)

    def get(self, id: UUID):
        raise NotImplementedError

    def remove(self, entity):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def update(self, id, listing) -> None:
        raise NotImplementedError