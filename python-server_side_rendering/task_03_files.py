#!/usr/bin/env python3

import json, pathlib, csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/items")
def items():
    json_path = pathlib.Path(__file__).with_name("items.json")
    try:
        data = json.loads(json_path.read_text())
        items_list = data.get("items", [])
        if not isinstance(items_list, list):
            items_list = []
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template("items.html", items=items_list)

def load_csv_data(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            products = [
                {
                    'id': int(row['id']),  # Convert id to int for consistency
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])  # Convert price to float
                }
                for row in reader
            ]
            return products
    except (FileNotFoundError, KeyError):
        return []

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None
    products = []

    # Use pathlib for reliable file paths
    base_path = pathlib.Path(__file__).parent
    json_path = base_path / "products.json"
    csv_path = base_path / "products.csv"

    if source == "json":
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
                products = data.get("products", [])
            if not products:
                error = "Failed to load JSON data"
        except (FileNotFoundError, json.JSONDecodeError):
            products = []
            error = "Failed to load JSON data"
    elif source == "csv":
        products = load_csv_data(csv_path)
        if not products:
            error = "Failed to load CSV data"
    else:
        products = []
        error = "Wrong source"

    if product_id and not error:
        try:
            product_id = int(product_id)  # Convert to int for comparison
            filtered_products = [p for p in products if p["id"] == product_id]
            if not filtered_products:
                error = "Product not found"
            else:
                products = filtered_products
        except ValueError:
            error = "Invalid product ID"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)