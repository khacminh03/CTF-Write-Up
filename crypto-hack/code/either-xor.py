from Crypto.Util.number import *
value = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
flag_format = b'crypto{'
key = [s1 ^ s2 for (s1, s2) in zip(value, flag_format)] + [ord("y")]
print("The key: " + "".join(chr(item) for item in key))
flag = []
for i in range (len(value)):
    print(chr(value[i] ^ key[i % len(key)]), end="")