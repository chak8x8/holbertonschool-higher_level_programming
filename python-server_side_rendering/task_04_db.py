#!/usr/bin/env python3

import json, pathlib, csv, sqlite3
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
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
       items_list = data.get("items", [])
    return render_template("items.html", items=items_list)

def load_csv_data(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
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
    except (FileNotFoundError, KeyError):
        return []

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None
    products = []

    base_path = pathlib.Path(__file__).parent
    json_path = base_path / "products.json"
    csv_path = base_path / "products.csv"
    sql_path = base_path / "products.db"

    if source == "json":
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    products = data
                else:
                    products = data.get("products", [])
            if not products:
                error = "Failed to load JSON data"
        except (FileNotFoundError, json.JSONDecodeError):
            products = data.get("products", [])
            error = "Failed to load JSON data"
    elif source == "csv":
        products = load_csv_data(csv_path)
        if not products:
            error = "Failed to load CSV data"
    elif source == "sql":
        products = load_sql_data(sql_path)
        if not products:
            error = "Failed to load SQL data"
    else:
        products = data.get("products", [])
        error = "Wrong source"

    if product_id and not error:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p["id"] == product_id]
            if not filtered_products:
                error = "Product not found"
            else:
                products = filtered_products
            if not filtered_products:
                error = "Product not found"
            else:
                products = filtered_products
        except ValueError:
            error = "Invalid product ID"

    return render_template("product_display.html", products=products, error=error)

def load_sql_data(file_path):
    """Load and parse data from SQLite database."""
    try:
        with sqlite3.connect(file_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, category, price FROM Products')
            rows = cursor.fetchall()
            products = [
                {
                    'id': int(row[0]),
                    'name': row[1],
                    'category': row[2],
                    'price': float(row[3])
                }
                for row in rows
            ]
            return products
    except sqlite3.Error:
        return []


if __name__ == '__main__':
    app.run(debug=True, port=5000)