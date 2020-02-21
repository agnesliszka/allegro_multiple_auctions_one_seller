# Standard library imports
import os
import re
import json

# 3rd party imports
from bs4 import BeautifulSoup
from parsel import Selector

# Create output list
output = []

# Function to load an offer file data from offer catalog
def load_offer(_offer):
    file_name = os.path.join('allegro_offers_first_search', _offer)
    with open(file_name, 'r', encoding="utf-8") as _file_in:
        _data = _file_in.read()
    return _data

# Function to get required data of the corresponding offer
def get_details(_data):
    soup = BeautifulSoup(_data, 'html.parser')

    # Get each element of table where searched parameters and their values are stored as a separate list element
    selector = Selector(text=_data)

    # Search for required data
    print(" ")

    # Search for offer_id
    filtered = selector.css('.markdown-text > p:nth-child(1)::text').get()
    print("offer_id: " + filtered)
    offers_data['offer_id'] = filtered

    # Search for seller_id
    filtered = selector.css('body > div.main-wrapper > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div > div > div > div._9a071_MD0He._9a071_27Ce5 > div._9a071_1LGgN > div._1h7wt._15mod > a::text').get()
    print("seller_id: " + filtered)
    offers_data['seller_id'] = filtered

    # Search for title
    filtered = selector.css('body > div.main-wrapper > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div > div > div > div._9a071_MD0He._9a071_27Ce5 > div._9a071_1LGgN > div._1h7wt._15mod > h1::text').get()
    print("title: " + filtered)
    offers_data['title'] = filtered
    # filtered = soup.find("title")
    # print("title: " + filtered.text)
    # offers_data['title'] = filtered.text

    # Search for price
    filtered = soup.find(itemprop="price")
    print("Cena : " + filtered.get('content'))
    offers_data['price'] = float(filtered.get('content'))

    # Search for url
    # filtered = selector.css('head > meta:nth-child(133)::attr(content)').get()
    filtered = selector.css('body > div.main-wrapper > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div > div > div > meta:nth-child(1)::attr(content)').get()
    print("url: " + filtered)
    offers_data['url'] = filtered

    # pattern = '[0-9]+'
    # match = re.search(pattern, _data)
    # if match:
    #     start_position = match.start()
    #     end_position = match.end()
    #     filtered = _data[start_position:end_position]
    # print("ID oferty : " + filtered)
    # offers_data['offer_id'] = filtered

# Create a json file to store the offers data
with open('stored_offers_data.json', 'w', encoding="utf-8") as data_file:
    offers = os.listdir('allegro_offers_first_search')
    for offer in offers:
        offers_data = {}
        # Print offer file name
        print(offer)
        # Load an offer file data from offer catalog
        data = load_offer(offer)
        # Print searched data of the corresponding offer
        get_details(data)
        # Add searched data to the output list
        output.append(offers_data)

    # Save offers details to a json's file
    json.dump(output, data_file, indent=4, ensure_ascii=False)
