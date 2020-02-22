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
    file_name = os.path.join('allegro_offers_second_search', _offer)
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
    try:
        filtered = selector.css('.markdown-text > p:nth-child(1)::text').get()
        print("offer_id: " + filtered)
        offers_data_second_search['offer_id'] = filtered
    except:
        try:
            # filtered = selector.css('a._xjsso::text').get()
            filtered = selector.css('a._xjsso._15mod._9a071_1BlBd::text').get()
            print("offer_id: " + filtered)
            offers_data_second_search['offer_id'] = filtered
        except:
            filtered = selector.css('span.text-10::text').get()
            filtered = filtered[8:]
            print("offer_id: " + filtered)
            offers_data_second_search['offer_id'] = filtered

    # Search for seller_id
    try:
        filtered = selector.css('body > div.main-wrapper > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div > div > div > div._9a071_MD0He._9a071_27Ce5 > div._9a071_1LGgN > div._1h7wt._15mod > a::text').get()
        print("seller_id: " + filtered)
        offers_data_second_search['seller_id'] = filtered
    except:
        try:
            filtered = selector.css('a._15mod:nth-child(3)::text').get()
            print("seller_id: " + filtered)
            offers_data_second_search['seller_id'] = filtered
        except:
            filtered = selector.css('a.btn-text-secondary:nth-child(2)::text').get()
            print("seller_id: " + filtered)
            offers_data_second_search['seller_id'] = filtered

    # Search for title
    try:
        filtered = selector.css('body > div.main-wrapper > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div > div > div > div._9a071_MD0He._9a071_27Ce5 > div._9a071_1LGgN > div._1h7wt._15mod > h1::text').get()
        print("title: " + filtered)
        offers_data_second_search['title'] = filtered
    except:
        try:
            filtered = selector.css('._1sjrk::text').get()
            print("title: " + filtered)
            offers_data_second_search['title'] = filtered
        except:
            filtered = selector.css('.h1.m-v-2.m-t-0--desktop.hyphens::text').get()
            print("title: " + filtered)
            offers_data_second_search['title'] = filtered

            # filtered = soup.find("title")
            # print("title: " + filtered.text)
            # offers_data_second_search['title'] = filtered.text

    # Search for price
    try:
        filtered = soup.find(itemprop="price")
        print("price : " + filtered.get('content'))
        offers_data_second_search['price'] = float(filtered.get('content'))
    except:
        filtered_price = selector.css('.sticky-sidebar > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > span:nth-child(2)::text').get()
        pattern = '\d^'
        filtered_price_match = re.search(pattern, filtered_price)
        if filtered_price_match:
            start_position = filtered_price_match.start()
            end_position = filtered_price_match.end()
            filtered_price_digits_only = filtered_price[start_position:end_position]

            filtered_cents = selector.css('.sticky-sidebar > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > span:nth-child(2) > span:nth-child(1)::text').get()
            filtered_cents_match = re.search(pattern, filtered_cents)
            if filtered_cents_match:
                start_position = filtered_cents_match.start()
                end_position = filtered_cents_match.end()
                filtered_cents_digits_only = filtered_cents[start_position:end_position]

                filtered_price_digits_only = float(filtered_price_digits_only+"."+filtered_cents_digits_only)
                print("price: " + filtered_price_digits_only)
                offers_data_second_search['price'] = filtered_price_digits_only

    # Search for url
    # filtered = selector.css('head > meta:nth-child(133)::attr(content)').get()
    try:
        filtered = selector.css('body > div.main-wrapper > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div > div > div > meta:nth-child(1)::attr(content)').get()
        print("url: " + filtered)
        offers_data_second_search['url'] = filtered
    except:
        try:
            filtered = selector.css('head > meta:nth-child(128)::attr(content)').get()
            print("url: " + filtered)
            offers_data_second_search['url'] = filtered
        except:
            try:
                filtered = selector.css('head > meta:nth-child(131)::attr(content)').get()
                print("url: " + filtered)
                offers_data_second_search['url'] = filtered
            except:
                filtered = selector.css('head > link:nth-child(11)::attr(href)').get()
                print("url: " + filtered)
                offers_data_second_search['url'] = filtered


# Create a json file to store the offers data
with open('stored_offers_data_second_search.json', 'w', encoding="utf-8") as data_file:
    offers = os.listdir('allegro_offers_second_search')
    for offer in offers:
        offers_data_second_search = {}
        # Print offer file name
        print(offer)
        # Load an offer file data from offer catalog
        data = load_offer(offer)
        # Print searched data of the corresponding offer
        get_details(data)
        # Add searched data to the output list
        output.append(offers_data_second_search)

    # Save offers details to a json's file
    json.dump(output, data_file, indent=4, ensure_ascii=False)
