from flask import Flask, request
from flask import render_template

import json
import requests as rq

# common config
with open('config.json') as f:
    CONFIG = json.load(f)

# frontend defines
with open('define_frontend.json') as f:
    DEFINE = json.load(f)

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        topicVal = request.values.get('topic')
        if topicVal is None:
            topicVal = ""
        else:
            print(topicVal)
            results = []
            for item in DEFINE["booklist"]:
                if item["topic"] == topicVal:
                    results.append(item)

            # return render_template('homepage.html',
                # topicVal=topicVal, results=results)
        #     rq.get("https://%s:%d/" % (CONFIG['ip_catalog'], CONFIG['ip_port']))

        lookupVal = request.values.get('lookupNum')
        if lookupVal is None:
            lookupVal = ""
        else:
            lookupVal = int(lookupVal) - 1
            results = [DEFINE["booklist"][lookupVal]]
            # return render_template('homepage.html',
                # lookupVal=lookupVal, results=results)
        #     rq.get("https://%s:%d/" % (CONFIG['ip_catalog'], CONFIG['ip_port']))
        #     rq.post(CONFIG['ip_catalog'], json=data)

    if request.values.get('withoutUI'):
        results = {
            "results": results
        }
        return json.dumps(results)

    return render_template('homepage.html', results=results,
        topicVal=topicVal, lookupVal=lookupVal)


@app.route('/buy', methods=['POST'])
def buy():
    if request.method == 'POST':
        itemNum = request.values.get('buyNum')
        # rq.post("https://%s:%d/" % (CONFIG['ip_catalog'], CONFIG['ip_port']))
        pass

    if request.values.get('withoutUI'):
        pass


@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html', isDefault=True, booklist=DEFINE["booklist"])

app.run()