import OCC_bot.Get_info.Get_data
import OCC_bot.Get_info.Request_price
import OCC_bot.Get_info.Request_price
import OCC_bot.Settings.Config
from Indicators import MA


def Get_signal():
    period = OCC_bot.Settings.Config.period
    OCC_bot.Get_info.Request_price.Request_Price()
    demaC = MA.DEMA(OCC_bot.Get_info.Get_data.Get_data()[4], period)
    demaO = MA.DEMA(OCC_bot.Get_info.Get_data.Get_data()[1], period)
    ema = MA.EMA(OCC_bot.Get_info.Get_data.Get_data()[4], period)
    sma = MA.SMA(OCC_bot.Get_info.Get_data.Get_data()[4], period)

    print(ema[len(ema)-1],ema[len(ema)-2])
    print(sma[len(sma)-1],sma[len(sma)-2])
    print(demaC[len(demaC)-1],demaC[len(demaC)-2])
    print(demaO[len(demaO)-1],demaO[len(demaO)-2])
    direction = 2
    if ((demaC[len(demaC)-2] < demaO[len(demaO)-2]) and (demaO[len(demaO)-1] < demaC[len(demaC)-1])):
        direction = 1
    if ((demaC[len(demaC) - 2] > demaO[len(demaO) - 2]) and (demaO[len(demaO) - 1] > demaC[len(demaC) - 1])):
        direction = 0
    return direction