from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov rax, [rdi]
add rax, [rdi + 8]
mov [rsi], eax
'''))
print(p.recvallS())
