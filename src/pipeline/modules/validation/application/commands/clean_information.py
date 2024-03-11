import json
from dataclasses import dataclass

from src.pipeline.config.db import db_datalake, db_roots
from src.pipeline.modules.validation.application.commands.base import CommandBaseHandler
from src.pipeline.modules.validation.application.dto import PropertyDTO
from src.pipeline.seedwork.application.commands import Command, CommandHandler
from src.pipeline.seedwork.application.commands import execute_command as command
from src.pipeline.modules.validation.domain.entity import Property

from src.pipeline.modules.validation.domain.repository import PropertyRepository

from src.pipeline.modules.validation.infrastructure.dto import ListingDatalake as ListingDatalakeDTO
from src.pipeline.modules.validation.infrastructure.dto import Property as PropertyDTO


@dataclass
class CleanInformation(Command):
    property_id: str


class CleanInformationHandler(CommandBaseHandler):
    def handle(self, command: CleanInformation):
        datalake = db_datalake.session.query(ListingDatalakeDTO).find(command.property_id)

        extra_data = json.loads(datalake.extra_data)

        property_dto = PropertyDTO(
            id=datalake.property_id,
            size_sqft=datalake["size_sqft"],
            floors=datalake["size_sqft"]
        )

        db_roots.session.add(property_dto)



@command.register(CleanInformation)
def execute_update_information_command(command: CleanInformation):
    handler = CleanInformationHandler()
    handler.handle(command)