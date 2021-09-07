This program reads the input from UNIX socket.
Its socket will listen on `pfrvi`.
Thus, we need to connect to that socket.
Unix socket is a little bit different from normal socket, and [this page](https://yaaam.tistory.com/entry/LinuxUDSUnix-Domain-Socket-UDS) explains about it.

It skips 9 bytes and reads 12 bytes.
The first mangler swaps between the second and the twelveth character.
The second mangler reverses the input.
The third mangler sorts the input in an ascending order.

The expected result is `64 67 67 67 6a 74 76 76 77 78 79 7a`, which is `dgggjtvvwxyz`.
When you reverse all those mangler, it becomes `zdxwvvtjgggy`.
Thus, the final answer should be `aaaaaaaaazdxwvvtjgggy`.