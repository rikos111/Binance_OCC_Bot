import hashlib
import hmac
import time
import urllib
from urllib.parse import urlparse

import requests


class Binance():
    methods = {
        # public methods
        'ping': {'url': 'fapi/v1/ping', 'method': 'GET', 'private': False},
        'time': {'url': 'fapi/v1/time', 'method': 'GET', 'private': False},
        'exchangeInfo': {'url': 'fapi/v1/exchangeInfo', 'method': 'GET', 'private': False},
        'orderBook': {'url': 'fapi/v1/depth', 'method': 'GET', 'private': False}, #Symbol, limits
        'klines': {'url': 'fapi/v1/klines', 'method': 'GET', 'private': False},#Symbol, interval = '1m'
        'markPrice': {'url': 'fapi/v1/premiumIndex', 'method': 'GET', 'private': False},#Symbol,
        'tickerPrice': {'url': 'fapi/v1/ticker/price', 'method': 'GET', 'private': False},  # Symbol,
        'tickerBook': {'url': '/fapi/v1/ticker/bookTicker', 'method': 'GET', 'private': False},  # Symbol,
        'openInterest': {'url': '/fapi/v1/openInterest', 'method': 'GET', 'private': False},  # Symbol,
        'aggTrade': {'url': '/fapi/v1/aggTrades', 'method': 'GET', 'private': False},  # Symbol,

        # private methods
        'account': {'url': '/fapi/v1/account', 'method': 'GET', 'private': True},  # timestamp,
        'accountBalance': {'url': '/fapi/v1/balance', 'method': 'GET', 'private': True},  # timestamp,
        'positionRisk': {'url': '/fapi/v1/positionRisk', 'method': 'GET', 'private': True},  # timestamp,
        'trades': {'url': '/fapi/v1/userTrades', 'method': 'GET', 'private': True},  # Symbol timestamp,
        'allOrders': {'url': '/fapi/v1/allOrders', 'method': 'GET', 'private': True}, # Symbol timestamp,
        'curAllOrders': {'url': '/fapi/v1/openOrders', 'method': 'GET', 'private': True},  # Symbol timestamp,
        'querryOrder': {'url': '/fapi/v1/order', 'method': 'GET', 'private': True},  # Symbol timestamp,

        'deleteOrders': {'url': '/fapi/v1/order', 'method': 'DELETE', 'private': True},  # Symbol timestamp,




       #'trades': {'url': 'api/v1/trades', 'method': 'GET', 'private': False},
       # 'historicalTrades': {'url': 'api/v1/historicalTrades', 'method': 'GET', 'private': False},
       # 'aggTrades': {'url': 'api/v1/aggTrades', 'method': 'GET', 'private': False},
       # 'ticker24hr': {'url': 'api/v1/ticker/24hr', 'method': 'GET', 'private': False},
       # 'tickerPrice': {'url': 'api/v3/ticker/price', 'method': 'GET', 'private': False},
       # 'tickerBookTicker': {'url': 'api/v3/ticker/bookTicker', 'method': 'GET', 'private': False},
    }

    def __init__(self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = bytearray(API_SECRET, encoding='utf-8')
        self.shift_seconds = 0

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            kwargs.update(command=name)
            return self.call_api(**kwargs)

        return wrapper

    def set_shift_seconds(self, seconds):
        self.shift_seconds = seconds

    def call_api(self, **kwargs):

        command = kwargs.pop('command')
        api_url = 'https://fapi.binance.com/' + self.methods[command]['url']

        payload = kwargs
        headers = {}

        payload_str = urllib.parse.urlencode(payload)
        if self.methods[command]['private']:
            payload.update({'timestamp': int(time.time() + self.shift_seconds) * 1000})
            payload_str = urllib.parse.urlencode(payload).encode('utf-8')
            sign = hmac.new(
                key=self.API_SECRET,
                msg=payload_str,
                digestmod=hashlib.sha256
            ).hexdigest()

            payload_str = payload_str.decode("utf-8") + "&signature=" + str(sign)
            headers = {"X-MBX-APIKEY": self.API_KEY}

        if self.methods[command]['method'] == 'GET' or self.methods[command]['url'].startswith('sapi'):
            api_url += '?' + payload_str

        print(api_url, payload_str, self.methods[command])
        response = requests.request(method=self.methods[command]['method'], url=api_url,
                                    data="" if self.methods[command]['method'] == 'GET' else payload_str,
                                    headers=headers)

        if 'code' in response.text:
            print(response.text)
        return response.json()