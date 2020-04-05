from flask import Flask, request, jsonify
import threading
import requests
import sys
import csv
app = Flask(__name__)
sem = threading.BoundedSemaphore(1)

# Address of the catalog server
catalogue_addr = sys.argv[1]

# Endpoint for the buy function
@app.route('/buy/<item_no>', methods=['GET'])
def buy(item_no):
    check_availability = requests.get('http://' + catalogue_addr + '/lookup/' + item_no)
    check_availability = check_availability.json()
    if(check_availability['stock'] == 0):
        return jsonify({
            'Buy Status': 'Error',
            'Reason': 'Item out of stock'
        })
    updated_book = requests.put('http://' + catalogue_addr + '/update/' + item_no, json={'stock': check_availability['stock'] - 1})
    return updated_book.json()

if __name__ == "__main__":
    app.run(port=5010, threaded=True)
