In this challenge, the program randomly skips your shellcode up to 0x800 bytes.
As it is random, we would better to fill the first 0x800 bytes with `nop` instructions, suggested by the challenge.
It would be more robust compared to `inc al` since it is a single byte instruction.

That's it.
