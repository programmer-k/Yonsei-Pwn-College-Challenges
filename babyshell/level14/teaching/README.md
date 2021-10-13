In this challenge, you are only allowed to give shellcode of six bytes.
However, the challenge now does not remove write permission so you can perform two stage payload.

You can see the first shellcode at `shellcode-1.s`.
Among six bytes, two bytes are used for `syscall` instruction, setting `RDI` to 0, and setting the address of buffer at `RSI`.
You can omit other parameters because it has already been set.
For the setting the address of buffer, `mov esi, 0x137006` is too long.
The solution for it is in gdb.
When you debug the challenge with it, `RDX` register already has the value we need, which is `0x1337000`.
We can just use it.

For the second shellcode, it is a normal shellcode so I will not explain it in detail.

Then, all you need is to provide the two shellcodes to the challenge.
It can be done by the following command.
```
(cat shellcode-raw-1; cat shellcode-raw-1; cat shellcode-raw-2) | /babyshell_level14_teaching1
```

The reason that I used `shellcode-raw-` twice is related to the buffer address `0x1337000`.
The `RIP` will point to `0x1337006` after running the first shellcode.
However, we write the second shellcode beginning from `0x1337000`, which is six bytes ahead.
Since the first shellcode is exactly six bytes, we can write the second shellcode in a proper position by giving the first shellcode twice.

