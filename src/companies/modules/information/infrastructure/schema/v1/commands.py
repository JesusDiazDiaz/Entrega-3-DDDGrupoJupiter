from pulsar.schema import *

from src.companies.seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class UpdateInformationCommandPayload(IntegrationCommand):
    property_id: String()



class UpdateInformationCommand(IntegrationCommand):
    data: UpdateInformationCommandPayload()