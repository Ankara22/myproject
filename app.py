# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# Product model
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        name = data['name']
        description = data['description']
        price = float(data['price'])  # Ensure price is a float
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

    # Create a new product and add it to the list
    new_product = Product(name, description, price)
    products.append(new_product)

    return jsonify({"message": "Product created", "product": {"name": name, "description": description, "price": price}}), 201

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    # Convert products to a list of dictionaries for JSON response
    product_list = [{"name": p.name, "description": p.description, "price": p.price} for p in products]
    return jsonify(product_list), 200

if __name__ == '__main__':
    app.run(debug=True)