In this challenge, the difference is that now the first 4096 bytes are not writable at all.
The solution for this is just filling 4096 bytes with meaningless instructions.

`inc al` is two bytes long instruction.
Thus, we can insert this 2048 times at the beginning of our shellcode.

After that, use `hexedit` to evade syscall filtering.
