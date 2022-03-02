from msilib.schema import Error
import os
import requests
from bs4 import BeautifulSoup
import urllib3

BASE_URL = 'https://shop.rammstein.de/en/catalog/product_info.php?products_id='
WHATS_NEW_URL = 'https://shop.rammstein.de/en/catalog/whats-new.html'

def get_image_urls(soup):
    img_urls = []
    return img_urls

def save_page(soup, url):
    title = soup.find_all("li", class_="active hidden-xxs")[0].next
    img_urls = get_image_urls(soup)
    text = f'{url}\n\n{title}\n'
    return 'Files written!'

def save_images(urls):
    pass

#def save_description():
#    pass

def whats_new_scraper():
    pass