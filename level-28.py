from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov rax, 0
cmp rdi, 0
jne loop
jmp end
loop:
mov bl, [rdi]
cmp bl, 0
je end

inc rax
inc rdi

jmp loop

end:
nop
'''))
print(p.recvallS())
