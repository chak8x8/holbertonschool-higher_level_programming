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

def load_csv_data():
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def load_json_data():
    try:
        with open("products.json") as f:
            data = json.load(f)
            return data.get("products", [])
    except Exception:
        return []

@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None

    if source == "json":
        products = load_json_data()
    elif source == "csv":
        products = load_csv_data()
    else:
        products = []
        error = "Wrong source"

        if product_id and not error:
            filtered_products = []
            for p in products:
                if str(p["id"]) == str(product_id):
                    filtered_products.append(p)

        if not filtered_products:
            error = "Product not found"
        else:
            products = filtered_products


    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
