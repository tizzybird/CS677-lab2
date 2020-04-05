from flask import Flask, request, jsonify
import threading
import requests
from datetime import datetime
import sys
import csv
app = Flask(__name__)
sem = threading.BoundedSemaphore(1)

# Address of the catalog server
catalogue_addr = sys.argv[1]

# Endpoint for the buy function
@app.route('/buy/<item_no>', methods=['GET'])
def buy(item_no):
    start_time = datetime.now()
    sem.acquire()
    print("Buy request for item " + item_no, file = open('order_log.txt', 'a'))
    check_availability = requests.get('http://' + catalogue_addr + '/lookup/' + item_no)
    check_availability = check_availability.json()
    if(check_availability['stock'] == 0):
        sem.release()
        end_time = datetime.now()
        with open('buy_item_times.txt', 'a') as f:
            f.write('%f\n' % (end_time - start_time).total_seconds())
        return jsonify({
            'BuyStatus': 'Error',
            'Reason': 'Item out of stock'
        })
    updated_book = requests.put('http://' + catalogue_addr + '/update/' + item_no, json={'stock': check_availability['stock'] - 1})
    sem.release()
    end_time = datetime.now()
    with open('buy_item_times.txt', 'a') as f:
        f.write('%f\n' % (end_time - start_time).total_seconds())
    return jsonify({
        'BuyStatus': 'Success',
        'Item': updated_book.json()['book_name']
    })

if __name__ == "__main__":
    app.run(port=5010, threaded=True)
