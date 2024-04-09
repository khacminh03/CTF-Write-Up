from Crypto.PublicKey import RSA
f = open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", mode="r")
key = RSA.importKey(f.read())
print(key.d)