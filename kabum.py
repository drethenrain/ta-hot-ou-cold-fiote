import cloudscraper
from operator import itemgetter

base_url = 'https://servicespub.prod.api.aws.grupokabum.com.br'


def search_products(item, page_size=None):
    page_size = page_size or 30

    requester = cloudscraper.create_scraper()
    res = requester.get(
        f'{base_url}/catalog/v2/products?query={item}&page_size={page_size}')
    res = res.json()['data']

    products = []
    for product in res:
        id = product['id']
        name, price, images = itemgetter(
            'title', 'price', 'images')(product['attributes'])

        products.append({
            'id': id,
            'name': name,
            'price': price,
            'images': images
        })

    return products
