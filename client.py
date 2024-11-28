# client.py

import requests
import json

API_URL = "http://127.0.0.1:5000/products"

def add_product(name, description, price):
    """Add a new product to the API."""
    product_data = {
        "name": name,
        "description": description,
        "price": price
    }
    
    response = requests.post(API_URL, json=product_data)

    if response.status_code == 201:
        print("Product added successfully:", response.json())
    elif response.status_code == 400:
        print("Failed to add product:", response.json())
    else:
        print("An error occurred:", response.status_code, response.text)

def get_products():
    """Retrieve and print all products from the API."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        products = response.json()
        print("List of Products:")
        for product in products:
            print(f"Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    else:
        print("An error occurred while retrieving products:", response.status_code, response.text)

if __name__ == "__main__":
    # Example usage
    add_product("Product 1", "Description of Product 1", 19.99)
    add_product("Product 2", "Description of Product 2", 29.99)
    
    get_products()