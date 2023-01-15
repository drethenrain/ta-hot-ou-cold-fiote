from flask import Flask, request, jsonify
import terabyte
import kabum

app = Flask(__name__)


@app.route('/terabyte/search', methods=['GET'])
def search_terabyte():
    arg = request.args.get('product')

    if len(arg) < 3:
        return {'error': 'Provide a valid product name. Must be more than 3 characters'}

    return jsonify(terabyte.search_products(arg))


@app.route('/kabum/search', methods=['GET'])
def search_kabum():
    product = request.args.get('product')
    page_size = request.args.get('page_size')

    if len(product) < 3:
        return {'error': 'Provide a valid product name. Must be more than 3 characters'}

    return jsonify(kabum.search_products(product, page_size))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
