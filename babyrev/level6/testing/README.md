The named pipe, also known as `FIFO`, is created with the name `ozvov`.
The program skips 6 bytes, then it reads 12 bytes.
The first mangler reverses the input.
The second mangler does the same, resulting in the same output with the original input.

The expected result is `69 71 74 67 6a 76 61 6d 67 6f 78 70`, which is `iqtgjvamgoxp`.
Thus, the output should `aaaaaaiqtgjvamgoxp`.