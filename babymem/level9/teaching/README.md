Warning! The value given by the challenge is incorrect. Please calculate by yourself.

Now, the stack canary is enabled.

To evade it, we first have to look into the input mechanism that the challenge uses.

```
while (n < size) {
    n += read(0, input + n, 1);
}
```

`n` is a local variable so that we can buffer overflow to evade stack canary.

To be specific, the variable `n` is stored 40 bytes after the buffer.

Thus, we use padding of 40 bytes.

The next byte that we give will overwrite the `LSB` of the variable `n`.

We can skip the stack canary by giving `0x47`.

Firstly, `0x47` will be stored in the variable `n`, and then due to the part `n += ...`, the variable `n` would eventually become `0x48`, which is the offset to the return address from the input buffer.

You see the point. We have just skipped some parts and directly jumped into the address that points to return address.

The last thing is writing two bytes for the return address as usual.

You can use the following commands to get the flag.

You might have to run the last command multiple times to get the flag.

```
./run.py
(echo "74"; cat payload) | /babymem_level9_teaching1
```