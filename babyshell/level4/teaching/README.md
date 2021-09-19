In this challenge, your shellcode is not allowed to include NULL byte.
`mov` instruction for setting register values includes NULL bytes, so we cannot use it.
The shellcode from the previous problem also contains NULL bytes to push zeros into the stack.

Just use `xor` instruction to set the registers to zero.
The problem is that string should always end with NULL byte to represent the end of string.
As we can modify the value in the memory during the runtime, first set the NULL byte to some value and then subtracting by that value at the runtime will give you NULL byte again.

That's it!
