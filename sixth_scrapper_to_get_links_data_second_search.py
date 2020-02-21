# Standard library imports
import os
import json
import requests


# Open json file with stored links
with open('stored_links_second_search.json', 'r') as data_file:
    data = json.load(data_file)
    for list_with_offers in data:
        for item in list_with_offers:
            print(item)
            offers = os.listdir('allegro_offers_second_search')
            number_of_offers = len(offers)
            i = number_of_offers + 1
            url = item
            response = requests.get(url)
            content = response.text
            if i<10:
                path = f'allegro_offers_second_search/offer_000{i}.html'
            elif i<100:
                path = f'allegro_offers_second_search/offer_00{i}.html'
            elif i<1000:
                path = f'allegro_offers_second_search/offer_0{i}.html'
            else:
                path = f'allegro_offers_second_search/offer_{i}.html'
            # Get offers data and save each offer data as separate html file
            with open(path, 'w', encoding='utf-8') as output_data:
                output_data.write(content)

