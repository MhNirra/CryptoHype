import requests

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {
        "symbol": "BTCUSDT"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return float(data['price'])

def get_eth_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {
        "symbol": "ETHUSDT"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return float(data['price'])