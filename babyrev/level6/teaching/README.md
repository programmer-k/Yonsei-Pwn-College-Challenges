In this problem, the program uses named pipe, which is also known as FIFO.
The filename created for the named pipe is `llgwv`.

Firstly, read 6 bytes from the named pipe and store it in the buffer. (Skipping)
And then, do the same thing with the following 9 bytes.

I wrote a simple C code that writes to the named pipe, so that the target program can read it.
After reading the input, the program swaps between third and the fifth byte.
Then, it agains swaps between the first and the second byte.

The expected output is `74 61 76 6a 69 62 71 68 6b`, which is `tavjibqhk`.
Cancelling those swapping operations, it becomes `atijvbqhk`.
Adding 6 random bytes, the final input is `bbbbbbatijvbqhk`.