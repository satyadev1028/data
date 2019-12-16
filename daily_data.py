'''
Api Rate Limit 500 per minute:wq
'''
import requests
import json
url = "https://api.twelvedata.com/time_series"

querystring = {"symbol":"AAPL","interval":"1day","outputsize":"1","apikey":"433d0400af6044699283136b2958166d"}

response = requests.request("GET", url, params=querystring)

result = json.loads(response.text)

print(result["values"][0]["volume"])