.global _start
_start:
.intel_syntax noprefix

# read(0, buf, 3000);
xor rax, rax
push 0
pop rdi
mov esi, 0x133700d
syscall
