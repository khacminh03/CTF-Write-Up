from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov al, [0x404000]
'''))
print(p.recvallS())