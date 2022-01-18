If you apply the same method that you used in the previous challenge, then you will face the problem of finding proper ROP gadgets.
Especially, you will not find the following ROP gadgets.

```
pop rax ; ret
syscall ; ret
pop r10 ; ret
```

In this challenge, you have to use different approach, which is to use the functions defined in dynamically linked libraries.
To be specific, you have to look at the section of `.plt.sec` with `objdump`.

```
Disassembly of section .plt.sec:

0000000000401150 <read@plt>:
  401150:       f3 0f 1e fa             endbr64
  401154:       f2 ff 25 e5 3e 00 00    bnd jmp QWORD PTR [rip+0x3ee5]        # 405040 <read@GLIBC_2.2.5>
  40115b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]
```

Here is one example. In this section, there are `read`, `open`, `sendfile` functions which are all we need to perform ROP.
If you do not know about `plt`, please refer to the following [article](https://bpsecblog.wordpress.com/2016/03/07/about_got_plt_1/).
Now, you will see the intention of this challenge.
Instead of using system calls directly, we should utilize the given functions.
That is why three previous ROP gadgets are not present in the challenge.

Since we are going to use the normal functions instead of system calls, we should use different schemes for parameter passing.

```
System calls: RDI RSI RDX R10 R8 R9
Normal calls: RDI RSI RDX RCX .....
```

Due to permission, it does not print the flag but the following command is helpful for debugging.

```
(cat payload; sleep 3; echo "/flag"; cat) | strace /babyrop_level6_teaching1
```

All done! now you have to do the same thing as before.