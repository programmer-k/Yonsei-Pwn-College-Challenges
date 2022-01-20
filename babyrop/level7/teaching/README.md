When you run the challenge, it gives you the address of the function `system` located in `libc`.
Furthermore, ASLR is applied to libraries.
The challenge says that you have to use the address to exploit ROP gadgets in `libc`.

Due to the ASLR, I am going to use `pwn` module.

The first thing to do is to find useful ROP gadgets as much as possible.
Again, we will use normal function calls instead of system calls.
Then, you will find some essential ROP gadgets are missing.

Now, it is time to look at the `libc` library.
To specify the library the challenge is using, use the following command.
This will print out all the dynamically linked libraries that the executable makes use of.
```
ldd /babyrop_level7_teaching1
```

Now use the `ROPgadget` tool to find ROP gadgets in `libc` library.
Specifically, I found `pop RDX` and `pop RCX' ROP gadget through this phase.
These two are not available in the challenge executable itself.

Similarly, try to find two functions which are `open` and `sendfile`.
Again, both of them are not available in the executable itself.

Since the address of the function `system` is given by the challenge, we can make use of it to find out the absolute addresses of ROP gadgets that we have found.
Specifically, find out the address difference between the `system` and ROP gadgets and use it to find out absolute address in runtime.

For example, assume that the address of `system` is `0x7fe790471410` in runtime.
Through `objdump`, you can find that the addresses of `system` and `sendfile` are `0x55410` and `0x116100`, repectively.
The difference would be `0x116100 - 0x55410 = 0xC0CF0`.
Then, in runtime, the address of `sendfile` would be `0x7fe790471410 + 0xC0CF0`.

Now, all you need to do is to write down a small script.
Please refer to the source code for more information about the implementation.
