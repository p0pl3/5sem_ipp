import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"

res = requests.get(url).json()

wallets = res["Valute"]

for wallet in wallets:
    info = "Валюта: {}\nПокупка: {}\nПродажа: {}".format(wallets[wallet]["Name"],
                                                         wallets[wallet]["Previous"],
                                                         wallets[wallet]["Value"])
    print(info)




