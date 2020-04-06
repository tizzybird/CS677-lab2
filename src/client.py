import json
import os
import random

import time
from datetime import datetime
import requests

SEARCH = 1
LOOKUP = 2
BUY    = 3

with open('config.json') as f:
    CONFIG = json.load(f)

with open('define_frontend.json') as f:
    DEFINE = json.load(f)

if __name__ == '__main__':
    ip_frontend = "http://%s:%d/" % (CONFIG["ip"]["frontend"]["addr"], CONFIG["ip"]["frontend"]["port"])
    actions = [SEARCH, LOOKUP, BUY]

    while True:
        action = random.choice(actions)
        
        if action == SEARCH:
            topic = random.choice(list(DEFINE['topics'].values()))
            print('Searching topic:', topic)
            params = {
                'withoutUI': True,
                'topic': topic
            }
            start_time = datetime.now()
            res = requests.get(ip_frontend + 'search', params=params)
            end_time = datetime.now()
            
            diff = (end_time - start_time).total_seconds()
            with open(CONFIG["log_path"]["client_search"], 'a') as f:
                f.write('%f\n' % diff)

            msg = 'Search request success!' if res.status_code == 200 else 'Search request failed!'
            print(msg + ' Time: %f' % diff)

        elif action == LOOKUP:
            item_num = random.randint(1, 4)
            print('Start a lookup for item number:', item_num)
            params = {
                'withoutUI': True,
                'lookupNum': item_num
            }
            start_time = datetime.now()
            res = requests.get(ip_frontend + 'search', params=params)
            end_time = datetime.now()
            
            diff = (end_time - start_time).total_seconds()
            with open(CONFIG["log_path"]["client_lookup"], 'a') as f:
                f.write('%f\n' % diff)

            msg = 'Search request success!' if res.status_code == 200 else 'Search request failed!'
            print(msg + ' Time: %f' % diff)

        else:
            item_num = random.randint(1, 4)
            print('Going to buy item number:', item_num)
            params = {
                'withoutUI': True,
                'buyNum': item_num
            }
            start_time = datetime.now()
            res = requests.post(ip_frontend + 'buy', params=params)
            end_time = datetime.now()
            
            diff = (end_time - start_time).total_seconds()
            with open(CONFIG["log_path"]["client_buy"], 'a') as f:
                f.write('%f\n' % diff)

            msg = 'Search request success!' if res.status_code == 200 else 'Search request failed!'
            print(msg + ' Time: %f' % diff)

        time.sleep(0.6)