from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
xor rax, rax
and rdi, 1
xor rdi, 1
or rax, rdi
'''))
print(p.recvallS())