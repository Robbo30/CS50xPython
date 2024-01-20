import requests

while True:
    try:
        numOfBitcoin = float(input("Bitcoin: "))
    except ValueError:
        pass
    else:
        break

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass
else:
    rate = float(response.json()["bpi"]["GBP"]["rate"])
    amount = rate * numOfBitcoin
    print(f"${amount:,.4f}")

