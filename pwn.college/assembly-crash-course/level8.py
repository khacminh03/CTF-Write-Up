from pwn import *
context.arch='amd64'
 
p=process('/challenge/run')
p.recvline()
p.send(asm('''
    mov al, dil
    mov bx, si
    '''.strip()))
print(p.recvallS())