from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov rax, 0
mov rbx, rsi
call loop_func
loop_func:
dec rsi
add rax, [rdi + rsi * 8]
cmp rsi, 0
jne loop_func
jmp end
end:
div rbx
'''))
print(p.recvallS())
