The programs reads input from the command-line argument `argv[0]`.
However, the problem is that `argv[0]` is fixed as the program name.
Of course you can modify the file name, but then it loses the access to the flag.
Thus, I will use soft link. Please see the commands at the end of this README.

It skips 8 bytes and reads 10 bytes.
The first mangler performs XOR operation with 0x53ba3a.
The second mangler reverses the input.
The third mangler swaps between the first and the second byte.
The fourth mangler performs XOR operation with 0x9dce.

The expected result is `c8 f1 54 fe cd 1d b9 85 5d f8`, which is weird value in ASCII form.
Reversing all those mangler, the original input, which is the answer, should be `112222ezqwijcsol`, considering `./`.

The following commands will lead you to the flag.
```
ln -s /babyrev_level10_teaching1 112222ezqwijcsol
./112222ezqwijcsol
```