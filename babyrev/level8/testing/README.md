This program reads the input from UNIX socket.
Its socket will listen on `opiou`.
Thus, we need to connect to that socket.
Unix socket is a little bit different from normal socket, and [this page](https://yaaam.tistory.com/entry/LinuxUDSUnix-Domain-Socket-UDS) explains about it.

It skips 12 bytes and reads 12 bytes.
The expected result is `5f 58 59 59 59 46 4d 4b 44 45 46 53`, which is `_XYYYFMKDEFS`.

The first mangler sorts the input in an ascending order.
The second mangler swaps between the sixth and the twelveth byte.
The third mangler peforms XOR operation with 0x3c.

When you reverse all those mangler, it becomes `cdeeeoqwxyzz`.
Thus, the final answer should be `aaabbbcccdddcdeeeoqwxyzz`.