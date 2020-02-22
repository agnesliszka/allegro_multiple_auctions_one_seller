# 3rd party imports
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Create 'offers' database schema
class OffersFirstSearch(Base):
    # Set a table name
    __tablename__ = 'allegro_offers_first_search'
    
    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    offer_id = Column(String, nullable='True')
    seller_id = Column(String, nullable='True')
    title = Column(String, nullable='True')
    price = Column(Float, nullable='True')
    url = Column(String, nullable='True')


# Create 'offers' database schema
class OffersSecondSearch(Base):
    # Set a table name
    __tablename__ = 'allegro_offers_second_search'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    offer_id = Column(String, nullable='True')
    seller_id = Column(String, nullable='True')
    title = Column(String, nullable='True')
    price = Column(Float, nullable='True')
    url = Column(String, nullable='True')