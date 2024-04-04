from Crypto.Util.number import *
value = long_to_bytes(int("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d", 16)).decode("utf-8")
print("".join(chr(ord(character) ^ 16) for character in value))