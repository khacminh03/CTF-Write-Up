from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov ah, 0x42
'''))
print(p.recvallS())
