In this challenge, your shellcode is not allowed to include `H` byte.
Thus, the previous shellcode does not work for this problem.

When you uses `objdump` to see the byte values of the shellcode, `H` byte, which is `0x48`, exists in `mov` and `lea`.
`xor` and `inc` also contain `0x48`, so we cannot use it.
`push` and `pop` do not contain `0x48`, so we can use it.

Please see the `shellcode.s` for detailed implementation.
