This challenge closes three basic channels, which are standard input, standard output, and standard error.
Thus, passing a 2-stage shellcode is impossible.

Since we need a way to output the flag value, my first approach is to use `execve`.
However, I am not sure but I do not think the standard output will be newly created after `execve`.

Thus, my approach is that opening two files. One for reading the flag and the other for writing the flag.
Here is the source code for it.
```
open("/flag", 0) // 0 is O_RDONLY
open("out", 1) // 1 is O_WRONLY
sendfile(1, 0, 0, 0x80);
```

Writing a corresponding shellcode and passing it to the challenge will net you to the flag.
