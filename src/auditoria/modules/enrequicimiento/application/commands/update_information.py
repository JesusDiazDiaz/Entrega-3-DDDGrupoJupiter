from dataclasses import dataclass

from src.auditoria.modules.enrequicimiento.application.commands.base import CommandBaseHandler
from src.auditoria.modules.enrequicimiento.application.dto import PropertyDTO
from src.auditoria.seedwork.application.commands import Command, CommandHandler
from src.auditoria.seedwork.application.commands import execute_command as command
from src.auditoria.modules.enrequicimiento.domain.entity import Property

from src.auditoria.modules.enrequicimiento.application.mapper import PropertyMapper
from src.auditoria.modules.enrequicimiento.domain.repository import PropertyRepository


@dataclass
class UpdateInformation(Command):
    id: str
    size_sqft: float
    construction_type: str
    floors: int


class UpdateInformationHandler(CommandBaseHandler):
    def handle(self, command: UpdateInformation):
        property_dto = PropertyDTO(
            id=command.id,
            size_sqft=command.size_sqft,
            construction_type=command.construction_type,
            floors=command.floors
        )
        property: Property = self.audit_factory.create_object(property_dto, PropertyMapper())

        repository = self.repository_factory.create_object(PropertyRepository.__class__)
        repository.update(command.id, property)


@command.register(UpdateInformation)
def execute_update_information_command(command: UpdateInformation):
    handler = UpdateInformationHandler()
    handler.handle(command)