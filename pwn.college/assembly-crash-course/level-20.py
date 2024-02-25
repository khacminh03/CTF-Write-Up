from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
push rdi
push rsi
pop rdi
pop rsi
'''))
print(p.recvallS())