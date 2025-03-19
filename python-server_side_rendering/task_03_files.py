#!/usr/bin/python3

from flask import Flask, render_template, request
from json import load
import csv

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


@app.route('/items')
def items():
    with open('items.json') as f:
        items = load(f).get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    if source == 'json':
        with open('products.json') as f:
            items = load(f)
    elif source == 'csv':
        with open('products.csv') as csvFile:
            items = [row for row in csv.DictReader(csvFile)]
    else:
        return render_template('product_display.html', message='Invalid source')
    
    if request.args.get('id'):
        filtered_items = [item for item in items if item['id'] == request.args.get('id')]
        if not filtered_items:
            return render_template('product_display.html', message='No items found')
        items = filtered_items
    return render_template('product_display.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
