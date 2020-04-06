from OCC_bot.Settings.Config import *
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.model.constant import *


def Post_BUY():
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    quant = quantity
    price_diff = price_difference
    message = bot.aggTrade(symbol='BTCUSDT', limit=1)
    a = round(float(message[0]['p']))
    buy = a + price_diff
    result = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.STOP_MARKET, quantity=quant, stopPrice=buy)
    buyId = result.orderId
    price = result.stopPrice
    return result, buyId, price
def Post_Sell():
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    quant = quantity
    price_diff = price_difference
    message = bot.aggTrade(symbol='BTCUSDT', limit=1)
    a = round(float(message[0]['p']))
    sell = a - price_diff
    result = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP_MARKET,
                                       quantity=quant, stopPrice=sell)
    buyId = result.orderId
    price = result.stopPrice
    return result,buyId, price
def Get_order(buyId):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_order(symbol="BTCUSDT", orderId=buyId)
    return result.status
def Cancel_order(buyId):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.cancel_order(symbol="BTCUSDT", orderId=buyId)
    return result