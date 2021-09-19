.global _start
_start:
.intel_syntax noprefix

# write(sock2, "read_file:/flag", 128);
mov rax, 1
mov rdi, 4
mov rsi, read_file
mov rdx, 128
syscall

read_file:
.asciz "read_file:/flag"
