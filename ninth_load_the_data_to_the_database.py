# Standard library imports
import json
import datetime

# Project imports
from second_db_engine import Session
from first_database_schema_design import OffersFirstSearch, OffersSecondSearch


session = Session()

# Create object representing allegro offers and input required data
with open('stored_offers_data.json', 'r', encoding="utf-8") as data_file:
    reader = json.load(data_file)
    for single_offers_data in reader:
        offer_data = OffersFirstSearch(**single_offers_data)
        session.add(offer_data)
        session.commit()

# Check database status
print(session.query(OffersFirstSearch).all())