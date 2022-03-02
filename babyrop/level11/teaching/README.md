In this challenge, there are many `nop` instructions before and after the call to `vuln` function.

This means that there is no `leave; ret` gadget nearby the original return address with single byte modification.

Therefore, we will modify two bytes and this will result in a success rate of 1 over 16.

To be specific, the original return address is `0x2552`.

And we will modify it with `0x2324`, which is the `leave; ret` gadget in function `vuln`.

In fact, we only need to modify 12 bits but that is impossible with the `read` function.

Thus, we are modify 2 bytes and that is why we get a success rate of 1 over 16.

Other things remain the same.

Unfortunately, I tried `migrate` function in `pwntools` but it did not work. Thus, I just sticked to the manual way to perform stack pivoting.
