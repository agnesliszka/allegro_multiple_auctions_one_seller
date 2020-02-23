# Standard library imports
import os
import sqlite3

# 3rd party imports
from sqlalchemy.sql import func

# Project imports
from first_database_schema_design import OffersFirstSearch, OffersSecondSearch
from second_db_engine import Session


session = Session()

# Function to run a database query
def run_query(query, db):
    with sqlite3.connect(db) as conn:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result

# Define a query map
QUERY_MAP = {
    'number_of_offers_firts_search': 'SELECT COUNT (*) FROM allegro_offers_first_search;',
    'number_of_offers_second_search': 'SELECT COUNT (*) FROM allegro_offers_second_search;',
    'sellers_that_offer_two_searched_products': 'SELECT DISTINCT allegro_offers_first_search.seller_id FROM allegro_offers_first_search INNER JOIN allegro_offers_second_search ON allegro_offers_first_search.seller_id = allegro_offers_second_search.seller_id GROUP BY allegro_offers_first_search.seller_id;',
    'sellers_two_products_url_example': 'SELECT DISTINCT allegro_offers_first_search.seller_id, allegro_offers_first_search.url FROM allegro_offers_first_search INNER JOIN allegro_offers_second_search ON allegro_offers_first_search.seller_id = allegro_offers_second_search.seller_id GROUP BY allegro_offers_first_search.seller_id;',
    'offers_links': 'SELECT DISTINCT allegro_offers_first_search.seller_id, allegro_offers_first_search.url, allegro_offers_second_search.url FROM allegro_offers_first_search INNER JOIN allegro_offers_second_search ON allegro_offers_first_search.seller_id = allegro_offers_second_search.seller_id GROUP BY allegro_offers_first_search.seller_id;',
}

# Define a database path
dirname = os.path.dirname(__file__)
db_name = 'allegro_offers.db'
path_to_db = os.path.join(dirname, db_name)

# Function to get general statistics - number of offers
def general_statistics():
    # Get numbers of offers from the database
    number_of_offers_first_search = run_query(QUERY_MAP['number_of_offers_firts_search'], path_to_db)
    print('Number of offers in the first search in the database: ' + str(number_of_offers_first_search))
    number_of_offers_second_search = run_query(QUERY_MAP['number_of_offers_second_search'], path_to_db)
    print('Number of offers in the second search in the database: ' + str(number_of_offers_second_search))

def sellers_that_offer_two_products():
    sellers_with_two_searched_products = run_query(QUERY_MAP['sellers_that_offer_two_searched_products'], path_to_db)
    print('Sellers that offer two searched products: ')
    for seller in sellers_with_two_searched_products:
        print(seller)

def sellers_two_products_url_example():
    sellers_with_two_searched_products = run_query(QUERY_MAP['sellers_two_products_url_example'], path_to_db)
    print('Sellers that offer two searched products with url example: ')
    for seller in sellers_with_two_searched_products:
        print(seller)

def offers_data():
    offers_links = run_query(QUERY_MAP['offers_links'], path_to_db)
    print('Sellers that offer two products with example of both product urls: ')
    for link in offers_links:
        print(link)

# Create a menu representing available options
def menu():
    while True:
        user_choice = input('''
        What would you like to do now? 
        Please input one of the following options:         
        1 - show statistics,
        2 - show sellers that offer both products
        3 - show sellers that offer both products with url example 
        4 - show examples of offers links grouped by seller
        5 - quit  
        ''')

        if user_choice == "1":
            general_statistics()
        elif user_choice == "2":
            sellers_that_offer_two_products()
        elif user_choice == "3":
            sellers_two_products_url_example()
        elif user_choice == "4":
            offers_data()
        elif user_choice == "5":
            return
        else:
            print("You have inputted incorrect value.")
    return

# Run menu
menu()
