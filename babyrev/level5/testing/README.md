You should create a file named `jdofj`.
The program skips 8 bytes from the input.
Then, it reads 12 bytes from the input.
The first mangler reverses the input.
The second mangler sorts the 12 bytes in ascending order.

The `EXPECTED_RESULT` is `62 64 67 68 6e 6f 71 71 74 76 78 7a`, which is `bdghnoqqtvxz`.
To get the initial input, we have to reverse to operation.
For the sorting mangler, we do not care. As long as the byte values remains the same, it will be sorted and become the `EXPECTED_RESULT`.
For reversing mangler, it becomes `zxvtqqonhgdb`.
Finally, by adding 8 random bytes, it becomes `aaaaaaaazxvtqqonhgdb`.