import os
import requests
from bs4 import BeautifulSoup
import argparse
from scripts import functions

parser = argparse.ArgumentParser(description='Style Transfer')
parser.add_argument('--start', default=0, help='Starting id. Default: 0')
parser.add_argument('--end', default=10000, help='Ending id. Default: 10.000')
parser.add_argument('--new', action='store_true', help='Enable scraping new items.')

args = vars(parser.parse_args())
start_id = args['start']
end_id = args['end']
scrape_new = args['new']

BASE_URL = 'https://shop.rammstein.de/en/catalog/product_info.php?products_id='
WHATS_NEW_URL = 'https://shop.rammstein.de/en/catalog/whats-new.html'