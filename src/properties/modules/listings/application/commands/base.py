from src.properties.modules.listings.domain.factory import PropertiesFactory
from src.properties.modules.listings.infrastructure.factory import RepositoryFactory
from src.properties.seedwork.application.commands import CommandHandler


class CommandBaseHandler(CommandHandler):
    def __init__(self):
        self._repository_factory:  RepositoryFactory = RepositoryFactory()
        self._properties_factory: PropertiesFactory = PropertiesFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def properties_factory(self):
        return self._properties_factory
