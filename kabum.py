import cloudscraper
from operator import itemgetter

base_url = 'https://servicespub.prod.api.aws.grupokabum.com.br'
requester = cloudscraper.create_scraper()


def search_products(item, page_limit=None):
    page_limit = page_limit or 30
    res = requester.get(
        f'{base_url}/catalog/v2/products?query={item}&page_size={page_limit}')
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
            'link': f'https://www.kabum.com.br/produto/{id}',
            'images': images
        })

    return products


def product_details(id):
    res = requester.get(
        f'{base_url}/catalog/v2/products/{id}')
    res = res.json()['attributes']
    # 🥀 SORRIZO RONALDO QUE CHEGOU
    name, price, images, old_price, manufacturer, description, payment_methods, available, discount_percentage, price_with_discount, stock = itemgetter(
        'title', 'price', 'images', 'old_price', 'manufacturer', 'html', 'payment_methods_default',
        'available', 'discount_percentage', 'price_with_discount', 'stock')(res)

    # 🥀
    result = dict({'id': id, 'name': name, 'price': price, 'old_price': old_price,
                   'discount_percentage': discount_percentage, 'price_with_discount': price_with_discount,
                   'available': available, 'stock': stock, 'manufacturer': manufacturer,
                   'link': f'https://www.kabum.com.br/produto/{id}', 'description_html': description,
                   'images': images, 'payment_methods': payment_methods})

    return result
