import re
import cloudscraper
from bs4 import BeautifulSoup as beauty

result = []


def search_products(item):
    scraper = cloudscraper.create_scraper()
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

    return result
