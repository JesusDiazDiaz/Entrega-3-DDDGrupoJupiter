from src.properties.modules.listings.application.dto import ListingDTO
from src.properties.modules.listings.domain.entity import Listing
from src.properties.seedwork.domain.repository import Mapper as RepMap


class ListingMapper(RepMap):
    def entity_to_dto(self, entity: Listing) -> ListingDTO:
        return ListingDTO(
            property_id=str(entity.property_id),
            extra_data=entity.data
        )

    def dto_to_entity(self, dto: ListingDTO) -> Listing:
        listing = Listing()
        listing.property_id = dto.property_id
        listing.data = dto.extra_data

        return listing

    def get_type(self) -> type:
        return Listing.__class__