In this challenge, you have to call five functions with an argument.

The first thing to do is retrieving addresses for five functions.
I will not explain this since it is the same procedure that we took before.

Then, you need to get the offset value.
I will not explain it in detail for the same reason.

When you run the challenge with the current payload, it prints the error message due to incorrect parameter and exits.
Now it is time to use `ROPgadget`.
`ROPgadget` is a tool that finds ROP gadget that you can make use of.
You can refer to this [page](https://github.com/JonathanSalwan/ROPgadget) for more information.

You can run the following command to get ROP gadgets.
```
ROPgadget.py --binary babyrop_level3_teaching1
```

When you look into it, there is no a direct solution which would be `mov rdi, 1`.
However, you can find a valuable instruction shown here.
```
0x0000000000402ae3 : pop rdi ; ret
```

Using the previous instruction, we can run each function as follows.
```
payload += pack("<Q", 0x402ae3) # pop rdi ; ret
payload += pack("<Q", 0x1)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x402654) # win_stage_1
```

It works in this way.
As we have already overwritten the original return address, it will first go to `0x402ae3` and run `pop` instruction.
At the time the `pop` instruction is being run, the `RSP` register points to the next eight bytes, which contains `0x1`.
Therefore, `0x1` will be stored at `RDI` register and we can now call the `win_stage_1` function as the argument is set correctly.

You can use the same method for the remaining four functions.
