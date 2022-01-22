In this challenge, you have to use stack pivoting.

There are a lot of resources and articles out there but very few explain it well.
Here are some that I found.

[Stack Pivoting](https://ir0nstone.gitbook.io/notes/types/stack/stack-pivoting)

[Hack The Box - Introduction to Binary Exploitation - PwnShop - Stack Pivot, Ret2LIBC [Walkthrough]](https://www.youtube.com/watch?v=i_5VQF18suQ)

As mentioned in the first link, `pop RSP` ROP gadget is the easiest way to do.

It is a little bit tricky to understand but when you try to use it, you will realize it is really simple stuff.
That is, just storing the value, which the `RSP` register points to, into `RSP` register.
As an example, in `leak_libc.py`, `RSP` register will store the value of `0x4040d0`.

Now, the key point is that make the `RSP` register point to the global variable in `bss` section.
You have to be careful about the address to store because it should work well during the stack transition.
That is why I used `0x4040d0` instead of `0x4040c0`.

With gdb, you will see that the stack moved to `bss` section so that we can fully utilize all the input that we have given before.
As always, the first thing to do is to leak the address of `libc`.
We have already handled this topic before, so I will skip this part.

Next, we have to invoke another `read` function.
This should happen after the address leakage so that we can generate payload with proper offset.

Here comes the big obstacle.
If you return to the entry point as before, it will result in segmentation fault.
I guess this is due to the stack transition.

To solve this problem, I came up with restoring the stack and then returning to entry point.
However, due to ASLR, the address of the stack changes every invocation of the process, and we have not leaked the address of the stack yet.
Thus, this was immediately abandoned.

Furthermore, there is no ROP gadget that manipulates `RDX`.
The register `RDX` is set to 0, so we cannot invoke `read` function by ourselves.

Finally, I came up with the idea that uses the `read` invocation in the main function.
Just before the invocation, it sets the `RDX` to `0x1000` so we can achieve what we want, which is reading another payload.
And do not forget to use the address `0x401a23` to set the register values appropriately before the invocation.
So far, I have covered `leak_libc.py`.

The second payload, `ROP.py`, is quite simple.
As always, just use `read`, `open`, `sendfile` to read and print the flag.

The thing that you have to be careful about is the padding of the payload.
This is because the parameters of the `read` function is automatically set and we cannot change them.

When you look into `leak_libc.py`, you will see that there are eight ROP gadgets.
Thus, I thought padding of 64 bytes would be correct but that is not true.
In fact, you have to use padding of 56 bytes.
When you debug with `gdb`, you will find that the segmentation fault occurs just after the `read` function ends.
To be specific, the instruction next to `read` function call in the main function, which is at `0x401a39`.

What really happens is that this `read` function call is an official and normal function call with `call` instruction.
Therefore, it will definitely push the return address, `0x401a39`, in this case.
When we input the second payload, the first instruction in the payload should overwrite this return address.
Pushing the return address to the stack means subtracting the `RSP` by 8 and store the return address.
Hence, the offset should be 56 bytes instead of 64 bytes.
