#!/usr/bin/env python3

import json
import csv
import pathlib
from flask import Flask, render_template, request

app = Flask(__name__)

def load_json_data(file_path):
    """Load and parse JSON data from the specified file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            # Handle case where JSON has a top-level key like 'products'
            return data.get('products', []) if isinstance(data, dict) else data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return []

def load_csv_data(file_path):
    """Load and parse CSV data from the specified file."""
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # Ensure consistent data types (e.g., convert id to int, price to float)
            products = [
                {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                for row in reader
            ]
            return products
    except (FileNotFoundError, KeyError) as e:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    json_path = pathlib.Path(__file__).parent / 'items.json'
    items = load_json_data(json_path)
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    # Determine the file path relative to the script
    base_path = pathlib.Path(__file__).parent
    json_path = base_path / 'products.json'
    csv_path = base_path / 'products.csv'

    # Load data based on source
    if source == 'json':
        products = load_json_data(json_path)
        if not products:
            error = 'Failed to load JSON data'
    elif source == 'csv':
        products = load_csv_data(csv_path)
        if not products:
            error = 'Failed to load CSV data'
    else:
        error = 'Wrong source'

    # Filter by product_id if provided
    if product_id and not error:
        try:
            product_id = int(product_id)  # Ensure id is an integer
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                error = 'Product not found'
            else:
                products = filtered_products
        except ValueError:
            error = 'Invalid product ID'

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)