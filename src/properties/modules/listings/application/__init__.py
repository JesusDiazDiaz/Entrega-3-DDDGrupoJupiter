from pydispatch import dispatcher

from .handlers import ListingIntegrationHandler
from ..domain.event.listing import ListingDataRecovered

dispatcher.connect(
    ListingIntegrationHandler.handle_listing_data_recovered,
    signal=f'{ListingDataRecovered.__name__}Integration'
)