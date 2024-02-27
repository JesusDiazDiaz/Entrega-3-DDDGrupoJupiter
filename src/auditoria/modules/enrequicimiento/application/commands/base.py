from src.auditoria.modules.enrequicimiento.domain.factory import AuditFactory
from src.auditoria.modules.enrequicimiento.infrastructure.factory import RepositoryFactory
from src.auditoria.seedwork.application.commands import CommandHandler


class CommandBaseHandler(CommandHandler):
    def __init__(self):
        self._repository_factory:  RepositoryFactory = RepositoryFactory()
        self._audit_factory: AuditFactory = AuditFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def audit_factory(self):
        return self._audit_factory
