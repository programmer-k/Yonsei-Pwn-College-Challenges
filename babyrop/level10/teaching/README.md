In this challenge, `PIE` is turned on.

Here is the given information.

```
Address of function win: 0x55830379e974
Stack address for return address: 0x7ffe5a86cc08
Padding: 48 bytes
Stack address for input buffer: 0x7ffe5a86cbd8
Pointer to win function: 0x7ffe5a86cbd0
```

Here is the idea. Perform stack pivoting to the `Pointer to win function` first.
Then, due to `Pointer to win function`, control flow will naturally move to the `win` function and we will get the flag.

For the padding of 48 bytes, fill the first 40 bytes with arbitrary values.
Then, fill the last 8 bytes with `input_buffer_address - 0x10`, which is the address for stack pivoting.
I will explain in detail how this would work.

Due to `PIE`, we do not know the addresses for instructions.
However, we do know that the instructions have page aligned addresses, so we can make use of nearby instructions by modifying LSB.
To be specific, we are going to focus on the following code snippet.

```
1d4b:       e8 73 fc ff ff          call   19c3 <vuln>
1d50:       48 8d 3d 7c 0d 00 00    lea    rdi,[rip+0xd7c]        # 2ad3 <_IO_stdin_used+0xad3>
1d57:       e8 d4 f3 ff ff          call   1130 <puts@plt>
1d5c:       b8 00 00 00 00          mov    eax,0x0
1d61:       c9                      leave
1d62:       c3                      ret
```

After we call the function `vuln`, the return address should be `0x1d50`, which is the next instruction of the `call` instruction.

To perform stack pivoting, we have to overwrite return address with `leave; ret` gadget.
It is at `0x1d61`.

When you see the original return address (`0x1d50`) and `leave; ret` gadget (`0x1d61`), only the last byte differs.
Therefore, we can accomplish stack pivoting by only modifying a single last byte with `0x61`.

After the first run of `leave; ret` in the `vuln` function, `RBP` will point to `input_buffer_address - 0x10`.
After the second run of `leave; ret` due to overwriting return address, `RIP` will point to the `win` function and run it.

The last thing that you should be careful about is not to use `sendline` function.
It will add an additional newline character represented as `0x0a` and this will make a trouble.
