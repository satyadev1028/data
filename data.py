import requests
import json 
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="arena",
  database="dip"
)

url = "https://api.worldtradingdata.com/api/v1/stock"

querystring = {"symbol":"SNAP","api_token":"CeWceEjl8ghLoNTI3D2hvkOyw8yfKcI2qdodwBgXMthC5JBhLnivqTafxMke"}



response = requests.request("GET", url, params=querystring)

result = json.loads(response.text)

for  dat in result["data"]:
	mycursor = mydb.cursor()
	sql = "INSERT INTO data (name, low, high) VALUES (%s, %s, %s)"
	val = (dat["name"], dat["day_low"], dat["day_high"])
	mycursor.execute(sql, val)
	mydb.commit()
	print(dat["name"])