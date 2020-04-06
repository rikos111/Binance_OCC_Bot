from datetime import datetime

import psycopg2


def Get_data():
    try:
        conn = psycopg2.connect(database='Bin', user='Bin', password="12345", host="localhost", port="5432")
    except:
        print('failed to connect')
    cursor = conn.cursor()
    cursor.execute('SELECT count(open_time) FROM bars')
    cur_count = cursor.fetchone()[0]

    cursor.execute('SELECT * FROM bars')
    i = 0
    open_time = []
    OP = []
    CP = []
    HP = []
    LP = []
    OT = cursor.fetchall()
    while (i < cur_count):
        open_time.append(datetime.fromtimestamp((OT[i][0])/1000).strftime('%Y-%m-%dT%H:%M:%SZ'))
        OP.append(OT[i][1])
        HP.append(OT[i][2])
        LP.append(OT[i][3])
        CP.append(OT[i][4])
        i = i + 1
    return open_time,OP,HP,LP,CP