import OCC_bot.Get_info.Get_data
import OCC_bot.Settings.Config
from Indicators import MA


def trall(price, direction):
    period = OCC_bot.Settings.Config.period // 2
    price_diff = OCC_bot.Settings.Config.percent_diff
    Last_price = OCC_bot.Get_info.Get_data.Get_data()[4][len(OCC_bot.Get_info.Get_data.Get_data()[4])-1]
    dema = MA.DEMA(OCC_bot.Get_info.Get_data.Get_data()[4],period)
    Change_price = dema[len(dema)-1]*((100+price_diff)/100)
    return Change_price
