import requests
import json
import sys

clientId = sys.argv[1]

with open('../src/config.json') as f:
    CONFIG = json.load(f)

ORDER_IP = CONFIG['ip']['order']['addr']
ORDER_PORT = CONFIG['ip']['order']['port']

def make_buy(host_ip, port, buyNum):
    # response = requests.get('http://' + host_ip + ":" + port)
    response = requests.get('http://' + host_ip + ":" + port + '/buy/' + str(buyNum))
    rs = response.json()
    if(rs['BuyStatus'] == 'Success'):
        with open('test5.txt', 'a') as f:
            msg = "client " + clientId + " buys " + rs['Item'] + '\n'
            f.write(msg)
    else:
        with open('test5.txt', 'a') as f:
            msg = rs['Item'] + " out of stock for client " + clientId + '\n'
            f.write(msg)

if __name__ == '__main__':
    it = 1
    while(it <= 4):
        i = 0
        while(i < 2):
          make_buy(ORDER_IP, str(ORDER_PORT), it)
          i += 1
        it += 1
