"""Functions for the ramm_scraper.py"""
import os
#from bs4 import BeautifulSoup
import re
import requests

BASE_URL = 'https://shop.rammstein.de/en/catalog/product_info.php?products_id='
WHATS_NEW_URL = 'https://shop.rammstein.de/en/catalog/whats-new.html'

def get_image_urls(soup, id):
    """Returns a list of image urls from the page."""
    img_urls = []
    img_list = soup.find_all('img', class_='lazy main-image')
    img_list.extend(soup.find_all('img', class_='lazy transparent'))

    for element in img_list:
        link_str = str(re.findall('"src":"(.*)",', str(element))[0])
        link = f'https://shop.rammstein.de/img/katalog/{id}/3000/{link_str}'
        img_urls.append(link)

    return img_urls

def save_page(soup, url, id):
    """Main function. Saves the info.txt and images."""
    if not os.path.exists('RammsteinShop'):
        os.makedirs('RammsteinShop')

    title = soup.find_all("li", class_="active hidden-xxs")[0].next
    price = soup.find_all('span', class_='neverwrap')[0].next

    if soup.find_all('span', class_='neverwrap color-lifad') != []:
        price_lifad = soup.find_all('span', class_='neverwrap color-lifad')[0].next
    else:
        price_lifad = ''

    if not os.path.exists(f'RammsteinShop/{id} {title}'):
        os.makedirs(f'RammsteinShop/{id} {title}')

    img_urls = get_image_urls(soup, id)
    img_str = ''
    for element in img_urls:
        img_str += f'{element}\n'

    text = f'{url}\n\n{title}\n\nPrice: {price}\nLIFAD: {price_lifad}\n\n\n{img_str}'

    file = open(f'RammsteinShop/{id} {title}/info.txt', 'w')
    file.write(text)
    file.close()

    save_images(img_urls, id, title)

    return f'{id}: Files written!'

def save_images(urls, id, title):
    """Saves all images from the webpage."""
    x = 1
    for element in urls:
        response = requests.get(element)

        file = open(f'RammsteinShop/{id} {title}/{x}.{element[-3:]}', "wb")
        file.write(response.content)
        file.close()
        x += 1

def save_description():
    """Returns the description of the item."""
    pass

def whats_new_scraper():
    """Scrapes the 'Whats New' page."""
    pass
