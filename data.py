import requests
import json 
import mysql.connector


def req(querystring):
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="arena",
	  database="dip"
	)
	url = "https://api.worldtradingdata.com/api/v1/stock"
	response = requests.request("GET", url, params=querystring)
	result = json.loads(response.text)
	for  dat in result["data"]:
		mycursor = mydb.cursor()
		sql = "INSERT INTO data (name, low, high) VALUES (%s, %s, %s)"
		val = (dat["name"], dat["day_low"], dat["day_high"])
		mycursor.execute(sql, val)
		mydb.commit()





querystring = {"symbol":"","api_token":"CeWceEjl8ghLoNTI3D2hvkOyw8yfKcI2qdodwBgXMthC5JBhLnivqTafxMke"}

i=0

file=open("NASDAQ_Symbols.txt","r+")

lines=file.readlines();

for line in lines:
	i=i+1
	
	if(i>499):
		req(querystring)
		querystring["symbol"]=""
		i=0
	
	querystring["symbol"]=line.rstrip("\n")+","+querystring["symbol"]