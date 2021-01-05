"""
------------------------------------------------------------------------
Database Module
------------------------------------------------------------------------
Purpose: to initialize the database to store scraped listings
------------------------------------------------------------------------
"""

# Imports
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create connection to apartment_listings.db
engine = create_engine('sqlite:///apartment_listings.db', echo=False)           
Base = declarative_base()

# Define listing structure for database
class DatabaseListing(Base):
    __tablename__ = 'apartment_listings'
    created = Column(String)
    available = Column(String)
    listing_type = Column(String)
    room_type = Column(String)
    address = Column(String)
    distance = Column(Float)
    sublet = Column(String)
    rooms = Column(Integer)
    features = Column(String)
    price = Column(String)
    listing_id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)

def get_engine():
    """
    Used to create database connection in web_scraper module
    """
    Base.metadata.create_all(engine)
    return engine
