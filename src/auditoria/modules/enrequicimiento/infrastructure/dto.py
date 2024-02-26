from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Property(Base):
    __tablename__ = 'properties'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    size_sqft = Column(Float, nullable=False)
    construction_type = Column(String)
    floors = Column(Integer)

    # Relación con los listados de alquiler
    # rental_listings = relationship('RentalListing', back_populates='property')


# class RentalListing(Base):
#     __tablename__ = 'rental_listings'
#
#     id = Column(Integer, primary_key=True)
#     price = Column(Float)
#     availability_date = Column(DateTime)
#     property_id = Column(Integer, ForeignKey('properties.id'))
#     property = relationship('Property', back_populates='rental_listings')
