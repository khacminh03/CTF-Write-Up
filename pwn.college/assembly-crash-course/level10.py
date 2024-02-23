from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
xor rax, rax
and rdi, rsi
xor rax, rdi
'''))
print(p.recvallS())