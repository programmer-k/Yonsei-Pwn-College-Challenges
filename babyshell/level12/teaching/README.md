In this challenge, You are only allowed to give a shellcode of `0x12` bytes.
It is too short to do something.

I have tried several approaches to solve this problem.

The first one is invoking `mprotect` system call to restore write operation for `0x4096` bytes and reading more shellcode.
However, it failed because `0x12` bytes are too short to do that.
We have to invoke at least two system calls, which are `mprotect` and `read`.

The second idea comes from using the memory after `0x4096` bytes, which are writable.
We can jump into there and read more shellcode.
However, I think it is implausible because the program only `mmap` `0x4096` bytes.

The third idea is to create a shell using `execve` system call.
It succeeded, but was not useful since it does not have root permission.
I found out that you first need to invoke `setuid` before running `execve` to get the root permission.
Please refer to [here](https://stackoverflow.com/questions/20684607/setuid-on-an-executable-doesnt-seem-to-work) for more information.

The solution for this problem is to use `chmod` system call.
This solution works because you only need a single system call.

To make the length of the shellcode less than `0x12`, I used the following code.
```
push 0x67616c66
push rsp
pop rdi
```

`0x67616c66` is hexadecimal representation of `galf`.
You first push it to the stack, then push rsp register to the stack, which is the address of the string `flag`.
Finally, pop that address to any register, in this case, `rdi`.

After running the shellcode, the file permission would change so that you can print it without root privilege.
