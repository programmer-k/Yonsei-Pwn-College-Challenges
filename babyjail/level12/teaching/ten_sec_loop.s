.global _start
_start:
.intel_syntax noprefix

# Loop for 10 seconds (on the server yonsei.pwn.college)
# The counter value is register rsi
# It uses register rdi for spending some time

mov rsi, 0
jmp one_sec_loop_start

one_sec_loop_back:
inc rsi

one_sec_loop_start:
mov rdi, 0x7A8000000
cmpq rsi, rdi
jl one_sec_loop_back
