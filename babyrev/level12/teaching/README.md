This time you can only modify 1 byte.

To check whether the MD5 hash value is identical to the expected result, the program uses function `memcmp`.
The third parameter is the length to compare, and in this program, it is 24.

When you look into the code, there is a `mov` instruction just before the function call.
It is represented as `ba 18 00 00 00`, and `18` is 24 in decimal form.
If we modify `18` into 0, then it will compare nothing, always resulting in true.

The address offset for this specific byte is `D1C`.
Therefore, all you need to do is enter `D1C` for offset and `0` for value.