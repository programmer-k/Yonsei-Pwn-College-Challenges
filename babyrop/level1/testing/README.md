Unlike previous testing challenges, the address of the function and offset for `ROP` has changed.
In this time, you have to calculate by yourself.

For the address of the function, you can easily find it by just disassembling with `ghidra`.
For the offset, I do not know a clean way to do.
My approach is to use a random offset and see where it is actually stored.
Manage the offset based on the difference.

I found a useful [article](https://haerinn.tistory.com/59) about the `pwndbg`.
