import OCC_bot.Get_info.Get_data
import OCC_bot.Get_info.Request_price
import OCC_bot.Settings.Config
from Indicators import MA

direction = 2
i = 0
period = OCC_bot.Settings.Config.period
demaC = MA.DEMA(OCC_bot.Get_info.Get_data.Get_data()[4], period)
demaO = MA.DEMA(OCC_bot.Get_info.Get_data.Get_data()[1], period)
ema = MA.EMA(OCC_bot.Get_info.Get_data.Get_data()[4], period)
sma = MA.SMA(OCC_bot.Get_info.Get_data.Get_data()[4], period)
close_price = OCC_bot.Get_info.Get_data.Get_data()[4]
ret = []
dir = []
sum = []
while(i < len(demaC)-1):
    if ((demaC[i+1] < demaO[i+1]) and (demaO[i] < demaC[i])):
        direction = 0
    if ((demaC[i+1] > demaO[i+1]) and (demaO[i] > demaC[i])):
        direction = 1
    if (direction == 1):
        ret.append(close_price[len(close_price)-len(demaC)+i])
        dir.append(1)

    if (direction == 0):
        ret.append(close_price[len(close_price)-len(demaC)+i])
        dir.append(0)
    i = i + 1
j = 0
while (j < len(ret)-1):
    if (dir[j] == 1):
        sum.append(ret[j+1] - ret[j])
    if (dir[j] == 0):
        sum.append(ret[j+1] - ret[j])
    j = j + 1
k = 0
itog = 0
while(k < len(sum)):
    itog = itog + sum[k]
    k = k + 1
print(ret)
print(dir)
print(sum)
print(itog)