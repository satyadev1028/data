'''
Api Rate Limit 500 per minute:wq
'''
import requests
import json
import  time
import mysql.connector

def getSymbols(MYDB):
    mycursor = MYDB.cursor()
    sql = 'select * from symbols'
    mycursor.execute(sql)
    symbols = mycursor.fetchall()
    return symbols

url = "https://api.twelvedata.com/time_series"

MYDB = mysql.connector.connect(host="localhost", user="root", passwd="root", database="dip")

symbols=getSymbols(MYDB)
count=0
querystring = {"symbol":"AAPL","interval":"1day","outputsize":"1","apikey":"433d0400af6044699283136b2958166d"}
for symbol in symbols:
    querystring["symbol"] = symbol[2]
    response = requests.request("GET", url, params=querystring)
    if (response.status_code != 200):
        continue
    result=json.loads(response.text)

    mycursor = MYDB.cursor()
    sql = "INSERT INTO daily_data (symbol, open, close, high, low, volume, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (symbol[2],result['values'][0]['open'],result['values'][0]['close'],result['values'][0]['high'],result['values'][0]['low'],result['values'][0]['volume'],result['values'][0]['datetime'])

    mycursor.execute(sql, val)
    MYDB.commit()
    count= count+1
    if(count==490):
        time.sleep(60)
        count=0