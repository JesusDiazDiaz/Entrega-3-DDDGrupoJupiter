import logging
from dataclasses import dataclass
from pydispatch import dispatcher

from src.properties.modules.listings.application.commands.base import CommandBaseHandler
from src.properties.modules.listings.domain.entity import Listing
from src.properties.modules.listings.domain.repository import ListingRepository
from src.properties.modules.listings.infrastructure.dto import ListingDatalake as ListingDTO
from src.properties.modules.listings.infrastructure.mapper import ListingMapper
from src.properties.modules.listings.infrastructure.adapters import ListingsAPIAdapter
from src.properties.seedwork.application.commands import Command
from src.properties.seedwork.application.commands import execute_command as command
from src.properties.seedwork.infrastructure.uow import UnitOfWorkPort


LOGGER = logging.getLogger()

@dataclass
class RecoverListings(Command):
    ...


class RecoverListingsHandler(CommandBaseHandler):
    def handle(self, command: RecoverListings):
        adapter = ListingsAPIAdapter()

        listing = adapter.get_properties()

        first_listing = listing[0]

        LOGGER.info(f'First listing: {first_listing}')

        listing_dto = ListingDTO(
            property_id=first_listing['property_id'],
            extra_data=listing
        )
        listing: Listing = self.properties_factory.create_object(listing_dto, ListingMapper())
        listing.data_recovered(listing)

        repository = self.repository_factory.create_object(ListingRepository.__class__)

        UnitOfWorkPort.register_batch(repository.get,repository)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()
       

        


@command.register(RecoverListings)
def execute_recover_listings_command(command: RecoverListings):
    handler = RecoverListingsHandler()
    handler.handle(command)