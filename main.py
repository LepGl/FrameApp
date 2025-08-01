import requests
from config import MARKET_API

items_url = f'{MARKET_API}items'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive",
    "Platform" : "pc",
    "Crossplay" : "true"
}
print(items_url)
item_list = []


try:
    item_list = requests.get(items_url, headers=headers)
    print(item_list)
except Exception as e:
    print(e)