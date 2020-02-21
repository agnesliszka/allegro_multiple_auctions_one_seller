# 3rd party imports
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Create 'offers' database schema
class Offer(Base):
    # Set a table name
    __tablename__ = 'allegro_offers'
    
    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    offer_id = Column(String)
    seller_id = Column(String)
    title = Column(String, nullable='True')
    price = Column(Float, nullable='True')
