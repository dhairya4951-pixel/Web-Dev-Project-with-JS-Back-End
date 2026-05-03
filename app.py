from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/products": {"origins": "*"}})

# In-memory storage
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "category": "Electronics",
        "description": "High performance laptop",
        "stock": 24
    },
    {
        "id": 2,
        "name": "Shoes",
        "price": 2500,
        "category": "Fashion",
        "description": "Comfortable running shoes",
        "stock": 24
    },
    {
        "id": 3,
        "name": "Wireless Headphones",
        "price": 8000,
        "category": "Electronics",
        "description": "Premium noise-cancelling wireless headphones",
        "stock":24  
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 6000,
        "category": "Electronics",
        "description": "Fitness tracking smartwatch with heart rate monitor",
        "stock": 15 
    },
    {
        "id": 5,
        "name": "Laptop Stand",
        "price": 2500,
        "category": "Accessories",
        "description": "Ergonomic aluminum laptop stand",
        "stock": 42
    },
    {
        "id": 6,
        "name": "USB-C Hub",
        "price": 1500,
        "category": "Accessories",
        "description": "7-in-1 USB-C hub with HDMI and card reader",
        "stock": 18
    },
    {
        "id": 7,
        "name": "Mechanical Keyboard",
        "price": 6500,
        "category": "Electronics",
        "description": "RGB backlit mechanical keyboard with blue switches",
        "stock": 9 
    },
    {
        "id": 8,
        "name": "Desk Mat",
        "price": 950,
        "category": "Accessories",
        "description": "Large waterproof desk mat",
        "stock": 33
    }
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products), 200


@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    name = data.get("name")
    price = data.get("price")
    category = data.get("category")
    description = data.get("description")
    stock = data.get("stock")

    if not name or not isinstance(name, str):
        return jsonify({"error": "Name is required and must be a string"}), 400

    if price is None:
        return jsonify({"error": "Price is required"}), 400

    try:
        price = float(price)
        if price <= 0:
            return jsonify({"error": "Price must be greater than 0"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Price must be a number"}), 400

    if not category or not isinstance(category, str):
        return jsonify({"error": "Category is required"}), 400

    if not description or not isinstance(description, str):
        return jsonify({"error": "Description is required"}), 400

    if stock is None:
        return jsonify({"error": "Stock is required"}), 400

    try:
        stock = int(stock)
        if stock < 0:
            return jsonify({"error": "Stock cannot be negative"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Stock must be a number"}), 400

    new_product = {
        "id": products[-1]["id"] + 1 if products else 1,
        "name": name,
        "price": price,
        "category": category,
        "description": description,
        "stock": stock
    }

    products.append(new_product)

    return jsonify({
        "message": "Product added successfully",
        "product": new_product
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5001)