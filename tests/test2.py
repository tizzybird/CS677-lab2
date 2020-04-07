import requests
import json

with open('../src/config.json') as f:
    CONFIG = json.load(f)

FRONT_IP = CONFIG['ip']['frontend']['addr']
FRONT_PORT = CONFIG['ip']['frontend']['port']

def make_request(host_ip, port, topic):
    # response = requests.get('http://' + host_ip + ":" + port)
    response = requests.get('http://' + host_ip + ":" + port + '/search', params={'withoutUI': True, 'lookupNum': topic})
    with open('test2.txt', 'a') as f:
        f.write(json.dumps(response.json()))


if __name__ == '__main__':
    make_request(FRONT_IP, str(FRONT_PORT), '1')
    make_request(FRONT_IP, str(FRONT_PORT), '2')
