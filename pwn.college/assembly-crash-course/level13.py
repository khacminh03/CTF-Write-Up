from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov [0x404000], rax
'''))
print(p.recvallS())