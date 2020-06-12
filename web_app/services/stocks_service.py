
import requests
import json

API_KEY = "abc123" # todo: set as env var

symbol = "AMZN" # input("Please choose a stock symbol (e.g. 'AMZN'): ")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
response = requests.get(request_url)

print(type(response))
# <class 'requests.models.Response'>
print(response.status_code) #> 200
print(type(response.text)) #> string


parsed_response = json.loads(response.text)
print(type(parsed_response)) #> dict

breakpoint()

latest_close = parsed_response["Time Series (Daily)"]["2020-05-18"]["4. close"]
print("LATEST CLOSE:", )
