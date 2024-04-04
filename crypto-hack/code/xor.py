encode = "label"
flag = "crypto{"
for item in encode:
    flag += chr(ord(item) ^ 13)
print(flag + "}")