from OCC_bot.Settings.binance_api import Binance


API_KEY = 'AIWpaNgtcDMM8LV8ZQkcnCEIsfgmHkVxJChftLlVbUroKvBLZfF6dOSHd8isGLXL',
API_SECRET = 'u9khIRbhOb61eEdmjXRjTGYy8T7eFFNN4jsVTmkknsIDMAyCkdOPj8UiqRUH88XP'

period = 14
time_delay = 60

#=========TRADE============
bot = Binance(API_KEY,API_SECRET)
quantity = 0.01
price_difference = 50


#=========TRALLING==========
percent_diff = 1