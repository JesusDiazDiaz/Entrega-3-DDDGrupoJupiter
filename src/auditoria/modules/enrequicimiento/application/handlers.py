import logging

from src.auditoria.modules.enrequicimiento.infrastructure.dispatchers import Dispatcher
from src.auditoria.seedwork.application.handlers import Handler

LOGGER = logging.getLogger()

class PropertyIntegrationHandler(Handler):
    @staticmethod
    def handle_enriched_information(event):
        dispatcher = Dispatcher()

        LOGGER.info(f"Handling event {event}")

        dispatcher.publish_event(event, "property-events")
