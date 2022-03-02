import os
import requests
import time
from bs4 import BeautifulSoup
import argparse
from scripts.functions import *

parser = argparse.ArgumentParser(description='RammsteinShop scraper.')
parser.add_argument('--start', type=int, default=0, help='Starting id. Default: 0')
parser.add_argument('--end', type=int, default=10000, help='Ending id. Default: 10.000')
parser.add_argument('--new', action='store_true', help='Enable scraping new items.')

args = vars(parser.parse_args())
start_id = args['start']
end_id = args['end']
scrape_new = args['new']

BASE_URL = 'https://shop.rammstein.de/en/catalog/product_info.php?products_id='
WHATS_NEW_URL = 'https://shop.rammstein.de/en/catalog/whats-new.html'

if scrape_new:
    pass
else:
    for current_id in range(start_id, end_id+1):
        time.sleep(1)
        url = BASE_URL + str(current_id)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        if response.status_code == 200:
            print(f'{current_id} ok')
            print(save_page(soup, url))
        else:
            print(f'{current_id} empty')

