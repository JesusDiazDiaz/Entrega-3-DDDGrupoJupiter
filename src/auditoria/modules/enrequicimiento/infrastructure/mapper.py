from src.auditoria.modules.enrequicimiento.domain.entity import Property
from src.auditoria.modules.enrequicimiento.domain.value_object import Characteristics
from src.auditoria.seedwork.domain.entity import Entity
from src.auditoria.seedwork.domain.repository import Mapper
from src.auditoria.seedwork.infrastructure.utils import unix_time_millis
from .dto import Property as PropertyDTO
from .exceptions import ImplementationNotExistsForFactoryException
from ..domain.events.information import PropertyEvent, EnrichedInformation


class PropertyCommandMapper(Mapper):
    def get_type(self) -> type:
        pass

    def entity_to_dto(self, entity: Entity):
        pass

    def dto_to_entity(self, dto: any) -> Entity:
        pass

    ...


class PropertyEventMapper(Mapper):
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            EnrichedInformation: self._entity_to_enriched_information,
        }

    def is_valid_version(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entity_to_enriched_information(self, entity: EnrichedInformation, version=LATEST_VERSION):
        def v1(event):
            from .schema.v1.events import EnrichedInformationPayload, EnrichedInformationEvent
            payload = EnrichedInformationPayload(
                property_id=str(event.property_id)
            )

            integration_event = EnrichedInformationEvent(id=str(event.id))
            integration_event.id = str(event.id)
            integration_event.time = int(unix_time_millis(event.event_date))
            integration_event.specversion = str(version)
            integration_event.type = 'EnrichedInformation'
            integration_event.datacontenttype = 'AVRO'
            integration_event.service_name = 'audit'

            integration_event.data = payload
            return integration_event

        if not self.is_valid_version(version):
            raise Exception(f'Invalid version {version}')

        if version == 'v1':
            return v1(entity)

    def entity_to_dto(self, entity: PropertyEvent, version=LATEST_VERSION) -> PropertyDTO:
        if not entity:
            raise ImplementationNotExistsForFactoryException

        func = self.router.get(entity.__class__, None)

        if not func:
            raise ImplementationNotExistsForFactoryException

        return func(entity, version)

    def dto_to_entity(self, dto: any) -> Entity:
        raise NotImplementedError

    def get_type(self) -> type:
        return PropertyEvent.__class__


class PropertyMapper(Mapper):
    def entity_to_dto(self, entity: Property) -> PropertyDTO:
        dto = PropertyDTO()
        dto.size_sqft = entity.characteristics.size_sqft
        dto.construction_type = entity.characteristics.construction_type
        dto.floors = entity.characteristics.floors
        return dto

    def dto_to_entity(self, dto: PropertyDTO) -> Property:
        property = Property()
        property.characteristics = Characteristics(
            size_sqft=dto.size_sqft,
            construction_type=dto.construction_type,
            floors=dto.floors,
        )

        return property

    def get_type(self) -> type:
        return Property.__class__
