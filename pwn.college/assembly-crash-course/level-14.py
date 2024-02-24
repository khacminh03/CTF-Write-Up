from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov rax, [0x404000]
mov rbx, [0x404000]
add rbx, 0x1337
mov [0x404000], rbx
'''))
print(p.recvallS())