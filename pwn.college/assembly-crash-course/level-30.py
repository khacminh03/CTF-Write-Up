from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
push rbp
    mov rbp, rsp
    sub rsp, 0xff
    
    mov rax, 0

init: 
    mov rdx, rbp
    sub rdx, rbx
    mov [rdx], rax
    inc rbx
    cmp rbx, 0xfe
    jne init

    mov rax, 1

count_byte:
    dec rsi
    mov bl, [rdi + rsi]
    mov rcx, rbp
    sub rcx, rbx
    add [rcx], rax

    cmp rsi, 0
    jne count_byte

    mov rax, 0
    mov rbx, 0
    mov rcx, 0
    
get_ans:
    mov rdx, 0
    mov rdx, rbp
    sub rdx, rbx
    cmp [rdx], cl
    jle skip
    mov rcx, [rdx]
    mov al, bl

skip:
    inc rbx
    cmp rbx, 0xfe
    jle get_ans
    jmp end

end:
    mov rsp, rbp
    pop rbp 
    ret
''').strip())
print(p.recvallS())
