In this challenge, the program sorts your shellcode in granularity of 8 bytes.
Just to make sure, it does not perform a byte comparison throughout 8 bytes.
Instead, it compares between two 8 bytes for the entire shellcode.

Firstly, make every instruction span 8 bytes so that they are not mixed during sorting operation.
To be specific, use `nop` instruction.
`mov` and `lea` are 7 bytes long instructions and `syscall` is 2 bytes long instruction.

Now, the problem is that two syscalls moves to the end of the shellcode.
This is because `syscall` has the instruction code of `0x0f05`, which is bigger than that of `0x48..` for `mov` and `lea`.
Thus, manage the `nop` which has the instruction code of `0x90`.

This phase is really a trial and error, so take some time to do that.
However, I would like to mention some useful tips.
The first thing is that there are a lot of ways to set register.
If you want to set `RAX` to 1, all following assembly code would work.
```
# First way
mov rax, 1

# Second way
xor rax, rax
inc rax

# Third way
xor rax, rax
add rax, 1

# Fourth way
xor rax, rax
add al, 1
```

The different thing among them is the instruction length and instruction code.
For example, the first one is 7 bytes long. My advice is that first try to use the shorter one.
It would let you have more freedom to manipulate with `nop`.
To be specific, if you have more bytes that you can set freely, then you can reorder the instructions within 8 bytes to evade sorting operation.

The next thing is be careful about the `lea` instruction.
If you use, for example, `lea rdi, [rip+flag]`, then it will give the wrong address when the position of this instruction changes.
Make sure to fix the position of `lea` instruction!

In summary, I first shrink the instruction length and insert `nop` instruction to avoid sorting.
That's all.
