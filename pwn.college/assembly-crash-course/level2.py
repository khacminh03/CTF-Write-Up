from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov rax, 0x1337
mov r12, 0xCAFED00D1337BEEF
mov rsp, 0x31337'''))
print(p.recvallS())