from sanic import Sanic
from sanic.response import json

import terabyte
import kabum

app = Sanic(__name__)


@app.route('/terabyte/search', methods=['GET'])
def search_terabyte(request):
    arg = request.args.get('product')

    if len(arg) < 3:
        return {'error': 'Provide a valid product name. Must be more than 3 characters'}

    return json(terabyte.search_products(arg))


@app.route('/kabum/search', methods=['GET'])
def search_kabum(request):
    product = request.args.get('product')
    page_size = request.args.get('page_size')

    if len(product) < 3:
        return {'error': 'Provide a valid product name. Must be more than 3 characters'}

    return json(kabum.search_products(product, page_size))


@app.route('/kabum/product/<id>', methods=['GET'])
def product_kabum(request, id):
    return json(kabum.product_details(id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, auto_reload=True)
