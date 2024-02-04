import requests

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url) 
print(response)

tickers = []
price = []
for ticker in response.json():
    if ticker['symbol'] == 'ETHUSDT':
        price = float(ticker['price'])
        tickers.append(ticker)

print(tickers)
print(price)
