import pulsar
from pulsar.schema import AvroSchema

from src.properties.modules.listings.infrastructure import utils
from src.properties.modules.listings.infrastructure.mapper import ListingDataRecoveredEventMapper


class Dispatcher:
    def __init__(self):
        self.event_mapper = ListingDataRecoveredEventMapper()

    def _publish_message(self, message, topic, schema) -> None:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publisher = client.create_producer(topic, schema=AvroSchema(schema))
        publisher.send(message)
        client.close()

    def publish_event(self, event, topic) -> None:
        event = self.event_mapper.entity_to_dto(event)
        self._publish_message(event, topic, event.__class__)


    # TODO: Add command
    def publish_command(self, command, topic) -> None:
        # command = self.mapper.entity_to_dto(command)
        raise NotImplementedError