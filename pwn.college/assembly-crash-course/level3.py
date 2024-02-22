from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''add rdi, 0x331337'''))
print(p.recvallS())
