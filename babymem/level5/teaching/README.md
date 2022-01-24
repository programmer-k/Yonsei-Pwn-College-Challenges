In this challenge, we need buffer overflow of 64 bytes.

However, this seems to impossible due to the following check.
```
record_size * record_num > 16
```

To evade this check, I would use integer overflow.

The input type for `record_size` and `record_num` is `unsigned int`, which is 4 bytes.

If we use `2 ** 31` and `2`, then the multiplication becomes `2 ** 32`, which is actually `0` in `unsigned int`.

You see the point. We can give large enough payload while evading the input size check.

You can use the following command to get the flag.

```
./run.py
(echo "2"; echo "2147483648"; cat payload) | /babymem_level5_teaching1
```