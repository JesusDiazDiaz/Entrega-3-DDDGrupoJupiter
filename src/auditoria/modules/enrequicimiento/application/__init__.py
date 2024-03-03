from pydispatch import dispatcher

from src.auditoria.modules.enrequicimiento.domain.events.information import EnrichedInformation
from .handlers import PropertyIntegrationHandler



dispatcher.connect(
    PropertyIntegrationHandler.handle_enriched_information,
    signal=f'{EnrichedInformation.__name__}Integration'
)