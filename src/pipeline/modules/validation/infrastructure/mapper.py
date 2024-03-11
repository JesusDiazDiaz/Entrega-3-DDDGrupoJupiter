from src.pipeline.seedwork.utils import unix_time_millis
from .dto import ListingDatalake as ListingDTO


class ListingDataRecoveredEventMapper(Mapper):
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            ListingDataRecoveredEvent: self._entity_to_listing_data_recovered_event,
        }

    def is_valid_version(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entity_to_listing_data_recovered_event(self, entity: ListingDataRecoveredEvent, version=LATEST_VERSION):
        def v1(event):
            from .schema.v1.events import ListingDataRecoveredPayload, ListingDataRecoveredEvent
            payload = ListingDataRecoveredPayload(
                property_id=str(event.property_id)
            )

            integration_event = ListingDataRecoveredEvent(id=str(event.id))
            integration_event.id = str(event.id)
            integration_event.time = int(unix_time_millis(event.event_date))
            integration_event.specversion = str(version)
            integration_event.type = 'CleanedData'
            integration_event.datacontenttype = 'AVRO'
            integration_event.service_name = 'pipeline'

            integration_event.data = payload
            return integration_event

        if not self.is_valid_version(version):
            raise Exception(f'Invalid version {version}')

        if version == 'v1':
            return v1(entity)

    def entity_to_dto(self, entity: ListingDataRecoveredEvent, version=LATEST_VERSION) -> ListingDataRecoveredPayload:
        if not entity:
            raise ImplementationNotExistsForFactoryException

        func = self.router.get(entity.__class__, None)

        if not func:
            raise ImplementationNotExistsForFactoryException

        return func(entity, version)

    def dto_to_entity(self, dto: any) -> Entity:
        raise NotImplementedError

    def get_type(self) -> type:
        return ListingDataRecoveredEvent.__class__


class ListingMapper(Mapper):
    def entity_to_dto(self, entity: Listing) -> ListingDTO:
        dto = ListingDTO()
        dto.property_id = entity.property_id
        dto.extra_data = entity.data
        return dto

    def dto_to_entity(self, dto: ListingDTO) -> Listing:
        property = Listing()
        property.property_id = dto.property_id
        property.data = dto.extra_data

        return property

    def get_type(self) -> type:
        return Listing.__class__
