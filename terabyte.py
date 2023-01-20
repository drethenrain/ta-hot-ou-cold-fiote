import re
import cloudscraper
from cloudscraper.exceptions import CloudflareChallengeError
from bs4 import BeautifulSoup as beauty
import time

result = []


def scrap_info(scraper, item):
    info = scraper.get(
        f'https://www.terabyteshop.com.br/busca?str={item}').text
    soup = beauty(info, 'html.parser')

    products = soup.find_all('div', {'class': 'commerce_columns_item_inner'})
    prices = soup.find_all('div', {'class': 'prod-new-price'})

    for product, price_raw in zip(products, prices):
        name = product.a['title']
        link = product.a['href']
        image = re.sub('\/cdn-cgi\/mirage\/.+\/\d+\/', '', product.img['src'])

        price = str(price_raw.span).strip(
            '</span>').replace('R$ ', '').replace('.', '').replace(',', '.')
        price = float(price)

        result.append({
            'name': name,
            'price': price,
            'link': link,
            'image': image
        })


def search_products(item):
    try:
        scraper = cloudscraper.create_scraper()
        scrap_info(scraper=scraper, item=item)
    except CloudflareChallengeError:
        for index in range(1, 11):
            # lento pra luto
            time.sleep(2)
            scraper = cloudscraper.create_scraper()
            try:
                scrap_info(scraper=scraper, item=item)
            except CloudflareChallengeError:
                return dict({
                    'error': 'deu ruim filho ai tu foi de comes e bebes tlgd'
                })
    return result
