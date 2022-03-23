In this challenge, the race condition that we should make use of is about file size.

Specifically, there is a file size check as follows.
```
if (256 < local_1a8.st_size) {
    puts("Error: file is too large!");
                    /* WARNING: Subroutine does not return */
    exit(1);
}
```

Moreover, you should look into the following code.
```
iVar1 = open((char *)param_2[1],0);
read(iVar1,local_118,0x1000);
if (local_18 != 0) {
    win();
}
```

The variable `local_18` is 256 bytes after the variable `local_118`.

Therefore, we have to overflow the variable `local_18` to call the `win` function.

In order to do that, we make use of a race condition with two files. One with a small size that can pass the check and the other with a large size that can overflow to the variable.

I firstly tried with `echo` and redirction to make these two files.

However, I do not know exactly but the contents of the file does not show up with the `cat` command.

That is why I come up with simple python scripts that generate a file.
