from dataclasses import dataclass

from src.pipeline.modules.validation.application.commands.base import CommandBaseHandler
from src.pipeline.modules.validation.application.dto import PropertyDTO
from src.pipeline.seedwork.application.commands import Command, CommandHandler
from src.pipeline.seedwork.application.commands import execute_command as command
from src.pipeline.modules.validation.domain.entity import Property

from src.pipeline.modules.enrequicimiento.application.mapper import PropertyMapper
from src.pipeline.modules.validation.domain.repository import PropertyRepository
from src.pipeline.seedwork.infrastructure.uow import UnitOfWorkPort


@dataclass
class UpdateInformation(Command):
    id: str
    size_sqft: float
    construction_type: str
    floors: int


class SaveInformationHandler(CommandBaseHandler):
    def handle(self, command: UpdateInformation):
        property_dto = PropertyDTO(
            id=command.id,
            size_sqft=command.size_sqft,
            construction_type=command.construction_type,
            floors=command.floors
        )
        property: Property = self.audit_factory.create_object(property_dto, PropertyMapper())
        # Add event domain
        property.enrich_information(property)

        repository = self.repository_factory.create_object(PropertyRepository.__class__)
        # repository.update(command.id, property)

        UnitOfWorkPort.register_batch(repository.update, command.id, property)
        UnitOfWorkPort.commit()



@command.register(UpdateInformation)
def execute_update_information_command(command: UpdateInformation):
    handler = UpdateInformationHandler()
    handler.handle(command)