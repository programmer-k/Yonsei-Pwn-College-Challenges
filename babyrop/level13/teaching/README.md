In this challenge, both stack canary and `PIE` is enabled and there is no `win` function.

You can read arbitrary 8 bytes and the address of your input buffer is provided.

With the read operation of the arbitrary 8 bytes, you are able to get the stack canary or the return address.

However, you cannot get both of them at the same time.

The solution for this is a partial overwrite of the return address to run the main function again.

When you look into the `__libc_start_main` function, you will notice that there are some important instructions that you have to take care.
```
27099:       48 8b 05 10 3e 1c 00    mov    rax,QWORD PTR [rip+0x1c3e10]        # 1eaeb0 <__environ@@GLIBC_2.2.5-0x4430>
270a0:       48 8b 74 24 08          mov    rsi,QWORD PTR [rsp+0x8]
270a5:       8b 7c 24 14             mov    edi,DWORD PTR [rsp+0x14]
270a9:       48 8b 10                mov    rdx,QWORD PTR [rax]
270ac:       48 8b 44 24 18          mov    rax,QWORD PTR [rsp+0x18]
270b1:       ff d0                   call   rax
270b3:       89 c7                   mov    edi,eax
```

`0x270b3` is the return address from the `main` function.

Then, obviously, `0x270b1` would be the address that invokes the `main` function. `mov` instructions before that would be ones that set the function arguments.

Therefore, to run the main function again, we should partially overwrite the return address to `0x27099`.

More precisely, a single byte would be sufficient which is `0x99`.

With this manner, we have multiple chances to leak arbitrary data.

In the first chance, we need to leak the stack canary to overwrite the return address.

In the second chance, we now can leak the full return address.

After that, we now know the address of the `libc` library, we can perform a ROP attack as usual.

One thing to note is that it would be better to use input buffer instead of `bss` section because we do not know the address due to `PIE`.

An interesting point from this challenge was we can re-run the main function without knowing the address of the main function or that of an entry point.
