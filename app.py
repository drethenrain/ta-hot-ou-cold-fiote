from sanic import Sanic
from sanic.response import json

import terabyte
import kabum

app = Sanic(__name__)


@app.route('/terabyte/search', methods=['GET'])
def search_terabyte(request):
    arg = request.args.get('product')

    if len(arg) < 3:
        return json({'error': 'Provide a valid product name. Must be more than 3 characters'}, 400)

    try:
        return json(terabyte.search_products(arg))
    except:
        return json({error: 'Could not find products with this name'}, 404)


@app.route('/kabum/search', methods=['GET'])
def search_kabum(request):
    product = request.args.get('product')
    page_limit = request.args.get('page_limit')

    if len(product) < 3:
        return json({'error': 'Provide a valid product name. Must be more than 3 characters'}, 400)

    try:
        return json(kabum.search_products(product, page_limit))
    except:
        return json({'error': 'Could not find products with this name'}, 404)


@app.route('/kabum/product/<id>', methods=['GET'])
def product_kabum(request, id):
    try:
        return json(kabum.product_details(id))
    except:
        return json({'error': 'Product not found'}, 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, auto_reload=True)
