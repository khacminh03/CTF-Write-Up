from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
pop rax
sub rax, rdi
push rax
'''))
print(p.recvallS())