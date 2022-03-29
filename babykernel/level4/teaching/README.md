In this challenge, you have to provide shellcode to get the flag.

Specifically, there is a `device_write` function that reads in your input and runs it.

There is a thing you have to take care of in the kernel space.

You cannot invoke system call inside the kernel space.

The system call is for the user space and you should never call system call when you are in the kernel space.

There is a function that you can make use of, which is `run_cmd(char *)`.

With this, you can run your own command similar to the `system` function.

One thing to note is that you should provide full path to the executable that you want to run.

Moreover, you cannot use standard input and output.

This is because we are interacting with `/proc/pwncollege`, not a normal process.

Therefore, we cannot use `/bin/sh` because even if the shell is opened, we do not have a way to interact with it.

Now, let's move on to the solution for this challenge.

Since using `run_cmd("/bin/sh");` failed, I came up with `chmod` command.

Specifically, I used `run_cmd("/bin/chmod 777 /flag");` for my shellcode.

If the shellcode works, then we can print the flag contents anytime.

Setting the register value for the function parameter is what we have always done, so I will not explain it here.

To call a function, we need to know the address of that function.

I used `/proc/kallsyms` to get it.
```
$ cat /proc/kallsyms | grep "run_cmd"
ffffffff81088670 t run_cmd
```

After creating the shellcode, we have to pass it to the `/proc/pwncollege`.

To do that, I created a simple C program that reads the shellcode and writes it to the `/proc/pwncollege`.

After running the program, you will see a segmentation fault but it is a normal result because we did not care a lot about returning to original control flow safely.

When you check the permission for the `/flag` file, you will see that it is set with `777`.
