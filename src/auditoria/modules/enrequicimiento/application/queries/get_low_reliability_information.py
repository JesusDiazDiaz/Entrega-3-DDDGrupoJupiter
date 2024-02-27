from dataclasses import dataclass

from src.auditoria.modules.enrequicimiento.application.mapper import PropertyMapper
from src.auditoria.modules.enrequicimiento.application.queries.base import QueryBaseHandler
from src.auditoria.modules.enrequicimiento.domain.repository import PropertyRepository
from src.auditoria.seedwork.application.queries import Query, QueryResult, execute_query as query


@dataclass
class GetLowReliabilityInformation(Query):
    ...


class GetLowReliabilityInformationHandler(QueryBaseHandler):
    def handle(self, query: GetLowReliabilityInformation):
        repository = self.repository_factory.create_object(PropertyRepository.__class__)
        information = repository.get_all()
        result = [self.audit_factory.create_object(info, PropertyMapper()) for info in information]
        return QueryResult(result=result)


@query.register(GetLowReliabilityInformation)
def execute_low_query(query: GetLowReliabilityInformation):
    handler = GetLowReliabilityInformationHandler()
    return handler.handle(query)