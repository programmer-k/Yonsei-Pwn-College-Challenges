Now, the problem is that the program uses `seccomp` to block some system calls.
Fortunately, system calls that we have been using, which are `openat` and `sendfile` is allowed.
Thus, we can use the same code for this problem.

However, I do not know the reason but it only outputs a single character for each `sendfile` function.
When you look deep into it using `strace`, the assembly code looks perfect but what `strace` prints is different from the code.
```
sendfile(1, 4, NULL, 1p);
```

`1p` probably is the reason for a single character output.
The simplest way to solve is making a loop to print all the flag values.

Run the following commands to capture the flag!
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyjail_level4_teaching1 / < ~/shellcode-raw
```