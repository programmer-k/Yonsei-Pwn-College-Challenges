This is challenge is really similar to the that of babymem level 12.

The different thing is that `NX` is disabled and there is no `win` function.

Therefore, we can inject shellcode.

One more thing to do is about return address.

As we write a shellcode into the stack, we need to know the exact address of the stack to run it.

To leak the stack address, I have used the `RBP` register.

On the stack frame for `vuln` function, `RBP` register points to (has an address of) the previous stack frame.

With this information, we can get the address of the shellcode in the stack that we have injected by adding an offset.

Since there is no `NULL` byte between stack canary and `RBP` register, we can leak stack canary and `RBP` register at the same time.

With the first function invocation, we can leak stack canary and `RBP` register.

At the next call, we inject shellcode and return to it.
