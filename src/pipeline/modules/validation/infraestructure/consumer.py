import logging
import time
import traceback
import pulsar, _pulsar
from _pulsar import PulsarException
from pulsar.schema import *

from src.pipeline.modules.validation.infrastructure.schema.v1.events import EnrichedInformationEvent
from src.pipeline.seedwork import utils


LOGGER = logging.getLogger()


def subscribe_to_events(app=None):
    client = None
    consumer = None
    connected = False
    subscribed = False

    while True:
        while not connected:
            try:
                client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
                connected = True
            except _pulsar.ConnectError:
                LOGGER.error("Connection failed. Retrying...")
                time.sleep(5)  # Wait for 5 seconds before retrying

        while not subscribed:
            try:
                consumer = client.subscribe(
                    'property-events',
                    'alpes-sub-events',
                    schema=AvroSchema(EnrichedInformationEvent)
                )
                subscribed = True
            except _pulsar.TopicNotFound:
                LOGGER.error("Topic not found. Retrying...")
                time.sleep(5)  # Wait for 5 seconds before retrying

        while True:
            try:
                msg = consumer.receive()
            except _pulsar.AlreadyClosed:
                LOGGER.error("Connection closed. Reconnecting...")
                connected = False
                subscribed = False
                time.sleep(5)  # Wait for 5 seconds before retrying
                break
            else:
                try:
                    data = msg.value()

                    LOGGER.info(f"📩 Received message: {data}")
                    consumer.acknowledge(msg)
                except PulsarException as e:
                    consumer.negative_acknowledge(msg)
                finally:
                    if client:
                        client.close()