from pwn import *
from Crypto.Util.number import *
import json
import base64
def b64Decode(text):
    return base64.b64decode(text).decode('utf-8')
def hexDecode(text):
    return bytes.fromhex(text).decode("utf-8")
def rot13Decode(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result
def bigIntDecode(text):
    transform = int(text, 16)
    return long_to_bytes(transform).decode("utf-8")
def utfDecode(lst):
    return "".join(chr(item) for item in lst)

conn = remote("socket.cryptohack.org", "13377")
for i in range (0, 101):
    data = json.loads(conn.recvline())
    payload = {}
    print(data)
    if data["type"] == "base64":
        payload["decoded"] = b64Decode(str(data["encoded"]))
    elif data["type"] == "hex":
        payload["decoded"] = hexDecode(str(data["encoded"]))
    elif data["type"] == "rot13":
        payload["decoded"] = rot13Decode(str(data["encoded"]))
    elif data["type"] == "bigint":
        payload["decoded"] = bigIntDecode(str(data["encoded"]))
    elif data["type"] == "utf-8":
        payload["decoded"] = utfDecode(data["encoded"])
    print(payload)
    conn.sendline(json.dumps(payload).encode())

