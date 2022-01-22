The executable checks whether your input is larger than 55.
If so, the process will be terminated.

However, 55 bytes payload is not enough to buffer overflow the return address.

When you look into the code, it uses `%i` to read payload size given by the user.

`%i` is for signed integer.

Thus, you can give a negative number to evade input check.

When invoking the `read` function, the `count` parameter is an unsigned integer type.

It means that the negative number we previously gave will be viewed as an unsigned integer, which would be large enough for the payload.

Here are the commands that I used.

```
./run.py
(echo "-1"; cat payload; cat) | /babymem_level4_teaching1
```
