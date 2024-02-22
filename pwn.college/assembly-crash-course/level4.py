from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
xor rax,rax
imul rdi,rsi
mov rax,rdi
add rax,rdx'''))
print(p.recvallS())