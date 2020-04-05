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
            topic = random.choice(DEFINE['topics'])
            print('Searching topic:', topic)
            params = {
                'withoutUI': True,
                'topic': topic
            }
            start_time = datetime.now()
            res = requests.get(ip_frontend + 'search', params=params)
            end_time = datetime.now()
            
            with open('../tests/client_search_time.txt', 'a') as f:
                f.write('%f\n' % (end_time - start_time).total_seconds())

            assert res.status_code == 200, 'Search request is failed!'

        elif action == LOOKUP:
            lookupNum = random.randint(1, 4)
            print('Start a lookup for number:', lookupNum)
            params = {
                'withoutUI': True,
                'lookupNum': lookupNum
            }
            start_time = datetime.now()
            res = requests.get(ip_frontend + 'search', params=params)
            end_time = datetime.now()
            
            with open('../tests/client_lookup_time.txt', 'a') as f:
                f.write('%f\n' % (end_time - start_time).total_seconds())

            assert res.status_code == 200, 'Lookup request is failed!'

        # else:
        #     item = random.randint(1, 4)
        #     print('Trying to buy', book_names[str(item)])
        #     r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(item))
        #     print(r.status_code)
        #     assert r.status_code == 200, 'Buy request failed!'
        #     print('Successfully bought', book_names[str(item)])

        # update_stock()

        time.sleep(1)