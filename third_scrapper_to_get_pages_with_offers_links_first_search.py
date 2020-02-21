# Standard library imports
import json
import requests

# 3rd party imports
from parsel import Selector


# Create required lists
url_list_first_search = ['https://allegro.pl/listing?string=butelka%20lovi%20250%20ml&bmatch=baseline-eyesa2-dict43-bab-1-4-0205']
first_search_range = 5
links_data_list = []

# Function to get links of pages where you can find links to the offers
def get_next_page_with_links():
    # Get page links where you can find offer links
    url = url_list_first_search[0]
    for i in range(first_search_range):
        response = requests.get(url)
        content = response.text
        selector = Selector(text=content)

        # Get next page url
        next_page_url = selector.css('a[data-analytics-click-value="next"]::attr(href)').get()
        # next_page_url = selector.css('._13q9y._8hkto._1us1q._1yk0g._1yr5c._1bo4a._sizcr::attr(href)').get()
        print(next_page_url)
        url_list_first_search.append(next_page_url)
        url = next_page_url

# Get page links where you can find offer links
get_next_page_with_links()

# Function to get offer links
def get_links(url):
    # Get page from url
    response = requests.get(url)
    content = response.text

    # Get offer links from url
    selector = Selector(text=content)
    links_data = selector.css('.ebc9be2 > a::attr(href)').getall()
    links_data_list.append(links_data)

for url in url_list_first_search:
    get_links(url)

# Create a json file to store the page data
with open('stored_links_first_search.json', 'w', encoding="utf-8") as stored_links:
    # Save offers links to json's file
    json.dump(links_data_list, stored_links, indent=4, ensure_ascii=False)