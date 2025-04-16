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
    raw = pathlib.Path("items.json").read_text()
    items_list = json.loads(raw)["items"]
    return render_template("items.html", items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)