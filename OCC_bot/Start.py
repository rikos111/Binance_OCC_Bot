import time

import OCC_bot.Settings.Config
import OCC_bot.Strategy.OCC

#print(OCC_bot.Get_info.Request_price.Request_Price())
timing = time.time()
while True:
    if time.time() - timing > OCC_bot.Settings.Config.time_delay:
        timing = time.time()
        print(OCC_bot.Strategy.OCC.Get_signal())


#result = OCC_bot.Trade.Post_order.Post_Sell()
#buyId = result[1]
#price = result[2]
#print(buyId, price)
#print(OCC_bot.Trade.tralling_stop.trall(price,1))
#print (OCC_bot.Trade.Post_order.Get_order(buyId))


