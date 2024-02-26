from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
cmp rdi, 3
jle here
jmp [rsi + 32]
here:
jmp [rsi + rdi * 8]
'''))
print(p.recvallS())
