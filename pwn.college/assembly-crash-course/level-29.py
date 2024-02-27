from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov rax, 0
mov rbx, 0
cmp rdi, 0
je end
jmp str_lower

str_lower:
mov rbx, 0
mov bl, [rdi]

cmp rbx, 0
je end

cmp rbx, 0x5a
jg skip

push rdi
push rax
mov rdi, 0
mov dil, bl

mov rcx, 0x403000
call rcx
mov bl, al 
pop rax
pop rdi
mov [rdi], bl
inc rax
jmp skip

skip:
inc rdi
jmp str_lower

end:
ret
'''))
print(p.recvallS())
