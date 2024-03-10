from uuid import UUID

from src.pipeline.config.db import db_dataleak


class ListingRepositoryPostgres(ListingRepository):
    def __init__(self):
        self._properties_factory = PropertiesFactory()

    @property
    def properties_factory(self):
        return self._properties_factory

    def add(self, entity):
        listing_dto = self.properties_factory.create_object(entity, ListingMapper())
        db.session.add(listing_dto)
        db.session.commit()

    def get(self, id: UUID):
        db_dataleak.session.get(id)
        raise NotImplementedError

    def remove(self, entity):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def update(self, id, listing) -> None:
        raise NotImplementedError