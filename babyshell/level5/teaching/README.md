In this challenge, you are not allowed to include `syscall` instruction.
You should insert it during the runtime.
Specifically, we cannot have `0x0f05` in the binary.

Firstly, use the usual shellcode with the labels just before the `syscall`.
After that, use hexedit to find `0x0f05`.
Modify it into `0x0e05`.
Finally, add the code that reads, increment, and write back a single byte using the labels generated previously.

This would evade the runtime check, and restore the instruction after it.
Have fun!
