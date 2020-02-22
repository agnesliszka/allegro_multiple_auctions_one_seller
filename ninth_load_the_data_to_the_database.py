# Standard library imports
import json

# Project imports
from second_db_engine import Session
from first_database_schema_design import OffersFirstSearch, OffersSecondSearch


session = Session()

# Create object representing allegro offers and input required data - first search
with open('stored_offers_data_first_search.json', 'r', encoding="utf-8") as data_file:
    reader = json.load(data_file)
    for single_offers_data in reader:
        offers_data_first_search = OffersFirstSearch(**single_offers_data)
        session.add(offers_data_first_search)
        session.commit()

# Check database status
print(session.query(OffersFirstSearch).all())

# Create object representing allegro offers and input required data - second search
with open('stored_offers_data_second_search.json', 'r', encoding="utf-8") as data_file:
    reader = json.load(data_file)
    for single_offers_data in reader:
        offers_data_second_search = OffersSecondSearch(**single_offers_data)
        session.add(offers_data_second_search)
        session.commit()

# Check database status
print(session.query(OffersSecondSearch).all())



