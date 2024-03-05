from sqlalchemy import Column, JSON
from src.properties.config.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = db.declarative_base()

class ListingDatalake(db.Model):
    __tablename__ = 'ListingDataLake'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    property_id = Column(UUID(as_uuid=True))
    extra_data = Column(JSON)
