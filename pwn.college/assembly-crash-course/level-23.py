from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
jmp address
.rept 0x51
nop
.endr
address:
mov rax, 0x1
'''))
print(p.recvallS())
