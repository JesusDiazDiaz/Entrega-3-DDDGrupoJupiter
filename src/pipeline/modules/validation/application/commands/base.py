from src.pipeline.modules.validation.domain.factory import AuditFactory
from src.pipeline.seedwork.application.commands import CommandHandler


class CommandBaseHandler(CommandHandler):
    def __init__(self):
        self._repository_factory:  RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory