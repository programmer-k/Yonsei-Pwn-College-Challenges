This program reads the input from TCP socket.
Its socket will listen on the port `45827`.
Thus, we need to connect to this socket.

It skips 12 bytes and reads 10 bytes.
The expected result is `65 67 6a 6c 6d 6f 74 75 77 78`, which is `egjlmotuwx` in ASCII form.

The first mangler swaps between the second and the third byte.
The second mangler reverses the input.
The third mangler swaps between the first and the fourth byte.
The fourth mangler sorts the input in an ascending order.

Thus, the answer should be `111222333444xuwtomejgl`.