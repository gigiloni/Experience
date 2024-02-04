import requests


try:
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    btc_price = response.json()['price']
    btc_price = float(btc_price)
    print(btc_price)
except requests.exceptions.ConnectionError as error:
    print(f'Something goes wrong: {error}')
    print('Hey man, check ur damn wifi')
