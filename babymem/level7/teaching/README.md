In this challenge, `PIE` is enabled.

As far as I know, `ASLR` makes memory regions such as stack and heap randomized while `PIE` makes code section randomized.

Therefore, we do not know the absolute address to to `win` function.

As the page aligns with `0x1000`, we know that the LSB of the address is fixed.

For the short jump, we can just modify LSB instead of full address.

For the jump that exceeds LSB limit, we know the half of second LSB and do not know the rest of it.

Thus, we can brute force until we succeed since the possibility is 1 / 16, which is high enough.

You can use the following commands to get the flag.

You might have to run the last command multiple times to get the flag.

```
./run.py
(echo "122"; cat payload) | /babymem_level7_teaching1
```