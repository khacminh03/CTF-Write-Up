from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
xor rax,rax
mov rax, rdi
div rsi
xor rax, rax
mov rax, rdx
'''))
print(p.recvallS())
