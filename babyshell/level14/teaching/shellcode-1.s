.global _start
_start:
.intel_syntax noprefix

# read(0, 0x1337000, 1000);
mov esi, edx
xor edi, edi
syscall
