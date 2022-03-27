In this challenge, you have to deal with the Linux kernel.

However, the region of interest is not the kernel itself, instead, it is a kernel module.

There is a kernel module provided at the top-level directory and you need to exploit the vulnerability to get the flag.

One thing to note is that you do not have to perform `insmod` and `rmmod` by yourself. Instead, it is done automatically when you run the `launch` binary.

To get the flag, basically, you have to run the `launch` binary and perform some operations inside virtual machine.

As described in the kernel ring buffer, you have to interact with `/proc/pwncollege`.

When you look into the kernel module, specifically the `init_module` function, you will find out that it reads the `/flag` file and store the data in a buffer.

Moreover, there are two major functions that you have to take care, which are `device_read` and `device_write`.

As described in the challenge description, you can open, read, write, and close this device as you would any other file.

`device_read` will be run when you try to read some data from the `/proc/pwncollege` and `device_write` will be run when you try to write some data to the `/proc/pwncollege`.

From the `device_write` function, there is a critical part as follows.
```
iVar1 = strncmp(buffer,"jsnxzigipkngxzvx",16);
device_state = (iVar1 == 0) + '\x01';
```

It compares two strings and update the `device_state` based on the previous comparison.

I could not fully understand the `device_read` function, but it seems that a valid `device_state` would return the `flag` data to the user space.

There is a simple C program that write the string into the `/proc/pwncollege`.

After running it, you can get the flag by reading the `/proc/pwncollege`.

Here are the commands that you should run.

```
gcc -static write.c
./a.out
head -n 1
```

In a virtual machine, there are no `gcc` and many libraries. Hence, you have to build the source code with `-static` option.
