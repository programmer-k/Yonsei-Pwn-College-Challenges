The programs reads input from the command-line argument `argv[0]`.
However, the problem is that `argv[0]` is fixed as the program name.
Of course you can modify the file name, but then it loses the access to the flag.
Thus, I will use soft link. Please see the commands at the end of this README.

It skips 16 bytes and reads 20 bytes.
The first mangler sorts the input in an ascending order.
The second mangler swaps between the fifth and the sixth byte.
The third mangler reverses the input.
The fourth mangler performs XOR operation.
If the byte is a odd number, XOR with 0x34.
Otherwise, XOR with 0x11.

The expected result is `6b 43 66 41 62 46 63 45 7a 5e 7b 5e 76 53 75 53 72 56 70 55`.
Reversing all those mangler, the original input, which is the answer, should be `11111222221234aabcgdggjjjkqrrsuwwz`, considering `./`.

The following commands will lead you to the flag.
```
ln -s /babyrev_level10_testing1 11111222221234aabcgdggjjjkqrrsuwwz
./11111222221234aabcgdggjjjkqrrsuwwz
```