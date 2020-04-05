from flask import Flask, request, jsonify
import threading
import sys
import csv
app = Flask(__name__)
sem = threading.BoundedSemaphore(1)



# This is the catalog. Rows are stored as [item_no, book_name, stock, cost, topic]
catalog_file = sys.argv[1]
catalog = open(catalog_file, 'r+')
catalog = list(csv.reader(catalog))

# Preprocessing on the input catalog
inventory = []

for row in catalog:
    tmp = [col.strip() for col in row]
    tmp[0] = int(tmp[0])
    tmp[2] = int(tmp[2])
    tmp[3] = int(tmp[3])
    inventory.append(tmp)

print(inventory)


x = 1
y = 1
z = 1

@app.route('/', methods=['GET'])
def change():
    sem.acquire()
    global x
    global y
    global z
    x += 1
    y += 1
    z += 1
    return jsonify({
        'x': x,
        'y': y,
        'z': z
    })

# Endpoint for search
@app.route('/search/<topic>', methods=['GET'])
def search(topic):
    sem.acquire()
    print("Incoming search request for topic " + topic, file = open('catalog_log.txt', 'a'))
    result = list(filter(lambda item: item[4] == topic, inventory))
    result = list(map(lambda book: {'item_no': book[0], 'book_name': book[1],'stock': book[2], 'cost': book[3], 'topic': book[4] }, result))
    sem.release()
    return jsonify({
        'books': result
    })

# Endpoint for lookup
@app.route('/lookup/<item_no>', methods=['GET'])
def lookup(item_no):
    sem.acquire()
    print("Incoming lookup request for item " + item_no, file = open('catalog_log.txt', 'a'))
    for books in inventory:
        if(books[0] == int(item_no)):
            res = {
                'book_name': books[1],
                'stock': books[2],
                'cost': books[3]
            }
            break
    sem.release()
    return jsonify(res)

# Endpoint for update
@app.route('/update/<item_no>', methods=['PUT'])
def update(item_no):
    sem.acquire()
    req = request.get_json()
    for books in inventory:
        if(books[0] == int(item_no)):
            books[2] = req['stock']
            print("Stock for item " + item_no, "reduced to " + str(req['stock']), file = open('catalog_log.txt', 'a'))
            sem.release()
            return jsonify({'item_no': books[0], 'book_name': books[1],'stock': books[2], 'cost': books[3], 'topic': books[4] })



if __name__ == '__main__':
    app.run(threaded=True)
