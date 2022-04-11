In this challenge, you can manage up to 16 unique allocations.

However, previous attack does not work now.

Please refer to the following code snippets.
```
// read_flag command
iVar1 = open("/flag",0);
read(iVar1,local_138 + 2,0x80);
```

```
// puts_flag command
if (*local_138 == 0) {
    puts("Not authorized!");
}
else {
    puts((char *)(local_138 + 2));
}
```

As you can see, the flag data is written to the heap memory beginning from index 2.

This means the first two bytes remain zero.

Consequently, we cannot pass the check for `puts_flag` command and the program will prints `Not authorized!`.

To overcome this problem, we will come up with the behavior of the fastbin.

After we free the heap memory, the first 16 bytes of heap data would store `fd` and `bk`.

We will utilize these variables to modify the first two bytes into non-zero values.

`fastbin` works in a `LIFO` manner.

```
a = malloc(160);
b = malloc(160);
free(a);
free(b);
```
Therefore, if we perform `malloc` and `free` twice, the fastbin would look like this.

```
...
fastbin[159]
// fastbin for 160 bytes of data
fastbin[160] -> b -> a
fastbin[161]
...
```

It is a linked list with a next pointer of `fd`.

`fd` in `b` points to next node, which is `a`.

After that, we perform `read_flag`.

Then, `b` would be popped out since fastbin works in a `LIFO` manner.
```
// fastbin for 160 bytes of data
fastbin[160] -> a
```

We can free it because we have an address for `b`.

After that, the fastbin would look like this.
```
fastbin[160] -> b -> a
```

At this point, `fd` in `b` points to `a`, which means the first two bytes have non-zero values.

Thus, we can get the flag.

Please note that there should be `a`. If not, `fd` in `b` will point to `NULL` which means we cannot get the flag.
