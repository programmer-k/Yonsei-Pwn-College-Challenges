The program reads the input from command-line `argv[1]`.
It skips 10 bytes and reads 12 bytes.

At first this program lets you modify 5 bytes in the program.
Then, it uses MD5 mangler to mangle your input.

To reach to the code that reads and prints the flag value, you should first pass the string match condition.
Instead of the standard C library function `strncmp`, it uses `cmp` function.
When you look at the code for it, if both of the first byte is a null character, then it will lead you to the flag.
However, this cannot be done since the variable for address input is only two bytes.
Thus, you can only modify the instructions.

When you look into the code for function `cmp`, there is a one `ret` code at the end.
Also, at the beginning of the function, after some `mov` operations for local variables, there is a jump statement.
If we modify the jump statement to jump to the `ret` operation, (`mov` operation precisely, because we need to set return value, which is `EAX` register, and pop the `RBP` register.) then the function will always return 0 without performing any work.
Jump operation is represented as `eb 7c`, and when you observe the code, `7c` represents the offset to jump.
The address difference between original destination and `mov` operation is `f`.
Thus, adding `f` to `7c` results in `8b`. We should input the value is `8b` to replace `7c`.

For the address part, when you calculate carefully, you can easily find that the offset is `4a7`.
Therefore, the answers are `Offset: 4a7` and `Value: 8b`.

However, this did not work at all.
The reason is that jump instruction starts with `eb` is a short jump, which means that it can only goes up to +128.
`7c` is 124 in decimal and `8b` is 139 in decimal. Thus, it is interpreted as negative values and go to previous instruction.
Please see more detailed explanation [here](https://c9x.me/x86/html/file_module_x86_id_147.html).

There is another jump instruction, which is executed when the two values are not identical.
In a nutshell, the only case that the function does not return 0 is when two values are not identical.
All other cases return 0. Then, can we just modify this one to return 0?
If we do so, regardless of the input values, it will always return 0 because there are only codes that return 0.

The jump instruction is represented as `eb 40` and goes to `pop` instruction.
We subtract it by 5, (which is the size of the one instruction `mov` which sets the `EAX` register to 0.) resulting `3b`.
The offset is `4f7`. Calculating the offset is managable. You can just calculate the difference between the base address and the address you want to change.
Also, please note that the program adds `0x1000` so you have to consider it.

Finally, we get to the answer.
Therefore, the answers are `Offset: 4f7` and `Value: 3b`.