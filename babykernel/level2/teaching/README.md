In this challenge, there is a `device_ioctl` function instead of `device_write` function.

The `device_ioctl` function performs string comparison and update the `device_state` accordingly.

When you look into the `device_ioctl` function, you will find out which parameter you should give to get the flag.
```
long device_ioctl(file *file,uint cmd,ulong arg)
{
    if (cmd == 1337) {
        iVar1 = strncmp((char *)arg,"nvnhbnfltnkaemuf",16);
    }
}
```

That is why I come up with the following code.
```
ioctl(fd, 1337, buffer);
```

Everything else remains the same as before.

Run these commands to get the flag.
```
gcc -static ioctl.c
./a.out
head -n 1
```
