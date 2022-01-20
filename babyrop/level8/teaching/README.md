In this challenge, you have to leak the address of libc by yourself.
There is a hint given in the challenge.

```
An easy way to do this is to do what is known as a `puts(puts)`.
The outer `puts` is puts@plt: this will actually invoke puts, thus initiating a leak.
The inner `puts` is puts@got: this contains the address of puts in libc.
Then you will need to continue executing a new ROP chain with addresses based on that leak.
One easy way to do that is to just restart the binary by returning to its entrypoint.
```

If you do not know what are `PLT` and `GLT`, please refer to the level6 directory.

I would like to denote `puts(puts)` as `<puts@plt>(<puts@GLIBC_2.2.5>);`.

Now, it is easy to get `<puts@plt>`. Just search for it using `objdump`.
Then, in `<puts@plt>`, it would jump to `<puts@GLIBC_2.2.5>`, so now you get two addresses that you need.

If you run with the generated payload, it will probably print non-ascii value.
You have to convert it to some format that you can understand.
I would use hexadecimal format.

The key point is that with the `pwn` module, you can get the print message in bytes.
The following python function will convert it to hexadecimal format.
```
hex(int.from_bytes(libc_address, "little"))
```

The hint explains everything about the theory, so I would rather not talk about this.

To restart the binary as suggested by the challenge, I used the method explained [here](https://stackoverflow.com/a/36165001) to get the entry point of the binary. Putting other values does not work, so please make sure to use the address of entry point.
```
readelf -h /babyrop_level8_teaching1 | grep Entry
```

The `libc` library is the same, so you do not have to find another ROP gadget for this challenge.

Now, `run.py` becomes a little bit more complicated.
You need to give three inputs and extract one intermediate output.
That's it.