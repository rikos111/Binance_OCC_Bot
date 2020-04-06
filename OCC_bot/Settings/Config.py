from OCC_bot.Settings.binance_api import Binance


API_KEY = '',
API_SECRET =''

period = 14
time_delay = 60

#=========TRADE============
bot = Binance(API_KEY,API_SECRET)
quantity = 0.01
price_difference = 50


#=========TRALLING==========
percent_diff = 1