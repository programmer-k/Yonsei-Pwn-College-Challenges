In this problem, you are allowed to use the following system calls.
1. Allowing syscall: close (number 3)
2. Allowing syscall: stat (number 4)
3. Allowing syscall: fstat (number 5)
4. Allowing syscall: lstat (number 6)

The different thing is that there is a new statement for description.
> Adding architecture to seccomp filter: x86

It uses the function `seccomp_arch_add` to do this.
From the manual page, there is a hint for this problem.
> The seccomp_arch_add() and seccomp_arch_remove() add and remove, respectively, architectures from the seccomp filter.
> When a seccomp filter is initialized with the call to seccomp_init(3) the native architecture is automatically added to the filter.

Furthermore, the key point is as follows.
> When adding a new architecture to an existing filter, the existing rules will not be added to the new architecture. However, rules added after adding the new architecture will be added to all of the architectures in the filter.

Thus, when you look into the code, the programmer made a mistake that we can exploit.
He or she called `seccomp_arch_add` after enrolling filterings for native architecture.
Therefore, even though the architecture `x86` was added to the `seccomp`,there is no filtering at all.
Now, we can freely use all the system calls from `x86` architecture.

To solve this problem, we can just open a flag file without anything else because in this time, they did not use `chroot` at all.
Use the following calling conventions for system calls in `x86` architecture.
> ebx ecx edx esi edi ebp

Use the following code to solve this problem.
```
open("/flag", 0);
sendfile(1, 3, 0, 0x80);
```

Running the following commands will lead you to the flag.
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyjail_level9_teaching1 < ~/shellcode-raw
```