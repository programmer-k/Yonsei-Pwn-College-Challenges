In this challenge, you have to make use of race conditions.

At the end of challenge, it reads the file given by `argv[1]` and prints it.

However, before doing it, there are several checks and here they are.

```
pcVar2 = strstr(argv[1],"flag");
if (pcVar2 != (char *)0x0) {
    puts("Error: path contains flag!");
    exit(1);
}
```

The code snippet above checks whether `argv[1]` contains a string `flag`.

This means that we cannot give the file name directly. To evade this check, we will use symlink instead.

```
iVar1 = lstat(argv[1],&local_a8);
if (iVar1 == -1) {
    puts("Error: failed to get file status!");
                    /* WARNING: Subroutine does not return */
    exit(1);
}
if ((local_a8.st_mode & 0xf000) == 0xa000) {
    puts("Error: file is a symlink!");
                    /* WARNING: Subroutine does not return */
    exit(1);
}
...
iVar1 = open(argv[1],0);
```

The code snippet above checks whether a file is a symlink.

Now it is time to leverage the race condition.

The key idea is that we can make use of the fact that the check and read do not happen at the same time.

More precisely, even though both `lstat` and `open` use `argv[1]` as a parameter, they can be different at the runtime.

There are two scripts that run in a infinite loop.

while the first script creates a symlink, the other removes the symlink and creates a normal file.

After running these two scripts, you can get the flag by running the challenge program multiple times.

The flag can be printed with the following logic.

At the time of `lstat` invocation, the file was a regular file, thus, passing the check.

After that, at the time of `open` invocation, the file becomes a symlink, thus, printing flag contents.
