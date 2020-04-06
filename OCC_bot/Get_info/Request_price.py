import time

import psycopg2

from OCC_bot.Settings.Config import API_KEY, API_SECRET
from OCC_bot.Settings.binance_api import Binance

bot = Binance(
    API_KEY,API_SECRET
)
def Request_Price():
    try:
        conn = psycopg2.connect(database='Bin', user='Bin', password="12345", host="localhost", port="5432")
    except:
        print('failed to connect')
    cursor = conn.cursor()
    cursor.execute('SELECT count(open_time) FROM bars')
    cur = cursor.fetchone()[0]
    new = False
    if(cur < 1):
        dic = bot.klines(symbol='BTCUSDT', interval='2h', endTime = time.time(),  limit=1500)
        new = True
        delete = False
    else:
        cursor.execute('SELECT max(open_time) FROM bars')
        max_OP = cursor.fetchone()[0]
        timeN = round(time.time(),0)
        divergense = timeN - max_OP/1000
        count_Bars = int(divergense // (2*60*60))
        #print(count_Bars)
        if(count_Bars > 0):
            dic = bot.klines(symbol='BTCUSDT', interval='2h', endTime=time.time(), limit=count_Bars)
            new = True
        else:
            dic = bot.klines(symbol='BTCUSDT', interval='2h', endTime = time.time(), limit=1)
            if(max_OP/1000+2*60*60 < time.time()):
                new = True

    i = 0
    while(i < len(dic)):
        jDic = dic[i]
        if(new == True):
            cursor.execute("INSERT INTO bars (open_time,open,high,low,close,volume,close_time) VALUES (%s,%s,%s,%s,%s,%s,%s)", (jDic[0], jDic[1],jDic[2],jDic[3],jDic[4],jDic[5],jDic[6]))
            conn.commit()
            ret = 'Insert new bars'
        else:
            cursor.execute('SELECT max(open_time) FROM bars')
            max_OP = cursor.fetchone()[0]
            cursor.execute("UPDATE bars SET close = %s where open_time = %s",(jDic[4],max_OP))
            conn.commit()
            ret = 'Price Update, new Price is', jDic[4]
        i = i + 1
    conn.close()
    return ret
