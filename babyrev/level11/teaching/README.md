The program reads the input from command-line `argv[1]`.
It skips 15 bytes and reads 18 bytes.

At first this program lets you modify 5 bytes in the program.
Then, it uses MD5 mangler to mangle your input.
The expected output is `ae 34 c3 1b 08 89 0e 05 0e ba 88 16 b1 6c 29 17 00 00`.

To reach to the code that reads and prints the flag value, you should first pass the string match condition.
It is done by the standard C library function `strncmp`.
The third parameter of this function is the length of the string to be compared.
If we change this value from 18 to 0, then the string match will always become true.

In my case, The instruction address for parameter setting is `0x555555555b2d`.
The instruction code is represented as `ba 12 00 00 00`.
Even if we do not know the exact manner to translate the byte encoded assembly code, it seems that the second byte `12`, which is 18 in decimal form, matches the original parameter 18.
Thus, we will modify `12` into `00`.

When you calculate it, the offset to `12` is `b2e`.
Thus, for the offset `b2e`, set the value 0. Then, the program will give you a flag value.