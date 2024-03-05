import logging

from src.properties.modules.listings.infrastructure.dispatchers import Dispatcher
from src.properties.seedwork.application.handlers import Handler

LOGGER = logging.getLogger()

class ListingIntegrationHandler(Handler):
    @staticmethod
    def handle_listing_data_recovered(event):
        dispatcher = Dispatcher()

        LOGGER.info(f"Handling event {event}")

        dispatcher.publish_event(event, "properties-events")
