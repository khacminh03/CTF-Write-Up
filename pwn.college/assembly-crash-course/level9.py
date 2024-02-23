from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
shl rdi,24
shr rdi,56
mov rax, rdi
'''))
print(p.recvallS())