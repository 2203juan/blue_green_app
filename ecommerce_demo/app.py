from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/products')
def products():
    products = [
        {'name': 'Product 1', 'price': 10.99},
        {'name': 'Product 2', 'price': 19.99},
        {'name': 'Product 3', 'price': 29.99},
        {'name': 'Product 4', 'price': 39.99},
        {'name': 'Product 5', 'price': 49.99},
    ]
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run()