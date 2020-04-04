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
            pass
        #     rq.post(CONFIG['ip_catalog'], json=data)

        lookupVal = request.values.get('lookupNum')
        if lookupVal is None:
            lookupVal = ""
        else:
            pass
        # if lookupNum is not None:
        #     rq.post(CONFIG['ip_catalog'], json=data)

    return render_template('homepage.html', topicVal=topicVal, lookupVal=lookupVal)

@app.route('/buy', methods=['POST'])
def buy():
    if request.method == 'POST':
        itemNum = request.values.get('buyNum')
        pass


@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html', isDefault=True, booklist=DEFINE["booklist"])

app.run()