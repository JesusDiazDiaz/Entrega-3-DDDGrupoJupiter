from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, JSON
from src.pipeline.config.db import db_datalake, db_roots
from sqlalchemy.dialects.postgresql import UUID
import uuid


class ListingDatalake(db_datalake.Model):
    __bind_key__ = 'datalake'
    __tablename__ = 'ListingDataLake'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    property_id = Column(UUID(as_uuid=True))
    extra_data = Column(JSON)


class Property(db_roots.Model):
    __bind_key__ = 'roots'
    __tablename__ = 'properties'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    size_sqft = Column(Float, nullable=False)
    construction_type = Column(String)
    floors = Column(Integer)
