The expected result is `76 6d 68 61 79 61 74 69 6e 74 6e 74 79 65 67 79`, which is `vmhayatintntyegy`.
The program reads the input from the file descriptor 900, but it does not open a file.
Thus, we have to make a program that opens a file and get the file descriptor 900, the program should spawn this challenge program as a child process.

The program skips 6 bytes, swaps between fourth and fifteenth byte value, and reverses twice.
Thus, the original input should be `aaaaaavmhgyatintntyeay`.