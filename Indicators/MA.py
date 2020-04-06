
def SMA(data,period):
    ret = []
    k = len(data) - 300
    while(k < len(data)-period+1):
        i = 0
        sum = 0
        while(i < period):
            sum = sum + data[k+i]
            i = i + 1
        ret.append(round((sum/period),8))
        k = k + 1
    return(ret)
def EMA(data,period):
    ret = []
    mult = 2 / (period + 1)
    sma = SMA(data,period)[len(SMA(data,period))-1]
    k = len(data) - 300
    while (k < len(data)-1):
        if(k == len(data) - 300):
            ema = mult*float(data[k+1])+(1-mult)*float(data[k])
            ret.append(ema)
        else:
            ema = mult*float(data[k+1])+(1-mult)*ema
            ret.append(ema)
        k = k + 1
    return (ret)
def DEMA(data,period):
    ret = []
    ema = EMA(data,period)
    ema_ema = EMA(ema,period)
    i = 0
    while (i < len(ema)):
        ret.append(2*ema[i] - ema_ema[i])
        i = i + 1
    return ret
#sma0 = SMA(CP,14)[len(SMA(CP,14))-2]
#sma1 = SMA(CP,14)[len(SMA(CP,14))-1]
#ema0 = EMA(CP,14)[len(EMA(CP,14))-2]
#ema1 = EMA(CP,14)[len(EMA(CP,14))-1]
#demaC0 = DEMA(CP,14)[len(DEMA(CP,14))-2]
#demaC1 = DEMA(CP,14)[len(DEMA(CP,14))-1]
#demaO0 = DEMA(OP,14)[len(DEMA(OP,14))-2]
#demaO1 = DEMA(OP,14)[len(DEMA(OP,14))-1]
#print(DEMA(CP,14))
#print(ema0,ema1)
#print(sma0,sma1)
#print(demaC0,demaC1)
#print(demaO0,demaO1)
