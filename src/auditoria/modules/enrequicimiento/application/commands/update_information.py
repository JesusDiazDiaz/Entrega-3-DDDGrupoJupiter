from dataclasses import dataclass

from src.auditoria.seedwork.application.commands import Command, CommandHandler
from src.auditoria.seedwork.application.commands import execute_command as command
from src.auditoria.modules.enrequicimiento.domain.entity import Property
from src.auditoria.modules.enrequicimiento.dto import Property as PropertyDto

from src.auditoria.modules.enrequicimiento.application.mapper import PropertyMapper
from src.auditoria.modules.enrequicimiento.domain.repository import PropertyRepository


@dataclass
class UpdateInformation(Command):
    size_sqft: float
    construction_type: str
    floors: int


class UpdateInformationHandler(CommandHandler):
    def handle(self, command: UpdateInformation):
        property_dto = PropertyDto()
        property: Property = self.audit_factory.create_object(property_dto, PropertyMapper())

        repository = self.repository_factory.create_object(PropertyRepository.__class__)
        repository.update(property)


@command.register(UpdateInformation)
def execute_update_information_command(command: UpdateInformation):
    handler = UpdateInformationHandler()
    handler.handle(command)