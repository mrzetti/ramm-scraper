import os
from bs4 import BeautifulSoup
import re

BASE_URL = 'https://shop.rammstein.de/en/catalog/product_info.php?products_id='
WHATS_NEW_URL = 'https://shop.rammstein.de/en/catalog/whats-new.html'

def get_image_urls(soup, id):
    img_urls = []
    img_list = soup.find_all('img', class_='lazy main-image')
    img_list.extend(soup.find_all('img', class_='lazy transparent'))

    for element in img_list:
        link_str = str(re.findall('"src":"(.*)",', str(element))[0])
        link = f'https://shop.rammstein.de/img/katalog/{id}/3000/{link_str}'
        img_urls.append(link)

    return img_urls

def save_page(soup, url, id):
    if not os.path.exists('RammsteinShop'):
        os.makedirs('RammsteinShop')

    title = soup.find_all("li", class_="active hidden-xxs")[0].next

    if not os.path.exists(f'RammsteinShop/{id} {title}'):
        os.makedirs(f'RammsteinShop/{id} {title}')
    
    img_urls = get_image_urls(soup, id)
    img_str = ''
    for element in img_urls:
        img_str += f'{url}\n'

    text = f'{url}\n\n{title}\n{img_str}'

    file = open(f'RammsteinShop/{id} {title}/info.txt', 'w')
    file.write(text)
    file.close()
    
    return f'{id}: Files written!'

def save_images(urls):
    pass
    

#def save_description():
#    pass

def whats_new_scraper():
    pass