from src.auditoria.modules.enrequicimiento.domain.factory import AuditFactory
from src.auditoria.modules.enrequicimiento.infrastructure.factory import RepositoryFactory
from src.auditoria.seedwork.application.queries import QueryHandler


class QueryBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory = RepositoryFactory()
        self._audit_factory = AuditFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def audit_factory(self):
        return self._audit_factory
