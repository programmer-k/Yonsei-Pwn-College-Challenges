This time you can only modify 2 bytes.
The difference is that now the program calculate the `MD5` hash value of codes before and after you modify the bytes.
If the two hash values are different, abort the program.

To check whether the two MD5 hash values are identical, the program uses function `memcmp`.
The third parameter is the length to compare, and in this program, it is 16.

When you look into the code, there is a `mov` instruction just before the function call.
It is represented as `ba 10 00 00 00`, and `10` is 16 in a decimal form.
If we modify `10` into 0, then it will compare nothing, always resulting in true.
Thus, we can bypass the code integrity check.

The address offset for this specific byte is `aa8`.
Therefore, all you need to do is enter `aa8` for offset and `0` for value.

You can do the same thing for the license key comparison.
The address offset for this specific byte is `dd2`.
Therefore, all you need to do is enter `dd2` for offset and `0` for value.