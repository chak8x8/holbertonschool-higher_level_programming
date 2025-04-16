#!/usr/bin/env python3

import json, pathlib
from flask import Flask, render_template

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
    # 1. locate items.json next to this .py file
    json_path = pathlib.Path(__file__).with_name("items.json")

    try:
        data = json.loads(json_path.read_text())      # may raise FileNotFoundError or JSONDecodeError
        items_list = data.get("items", [])            # safe lookup; default to []
        if not isinstance(items_list, list):          # ensure it's really a list
            items_list = []
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []                               # fallback if anything goes wrong

    return render_template("items.html", items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)