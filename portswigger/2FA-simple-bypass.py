import requests
url = "https://0a5900e30349cc3c801b8f89002800a1.web-security-academy.net/"
payload = {
    "username" : "carlos",
    "password" : "montoya" 
}
response = requests.post(url=(url + "/login"), data=payload)
response2 = requests.get(url=(url + "/my-account"), data=payload)
print("You solve the lab")