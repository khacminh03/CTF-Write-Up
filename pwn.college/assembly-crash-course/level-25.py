from pwn import *
context.arch = "amd64"
p = process("/challenge/run")
p.recvline()
p.send(asm('''
mov eax, [rdi]
mov ebx, [rdi + 4]
mov ecx, [rdi + 8]
mov edx, [rdi + 12]
 
cmp eax, 0x7f454c46
je con1
 
cmp eax, 0x00005A4D
je con2
 
imul ebx, ecx
imul ebx, edx
jmp done
 
con1:
add ebx, ecx
add ebx, edx
jmp done
 
con2:
sub ebx, ecx
sub ebx, edx
done:
mov eax, ebx
'''))
print(p.recvallS())
