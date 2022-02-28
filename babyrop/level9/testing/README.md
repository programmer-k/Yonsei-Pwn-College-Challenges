It takes a long time to solve this challenge. The way that I did on teaching challenge does not work on testing challenge.
I still do not know why. From what I newly found here in this testing challenge, the answer from teaching should not work.

# `leave; ret`
Before we dive into the challenge, I would like to talk about general stack pivoting.

[Stack Pivoting](https://ir0nstone.gitbook.io/notes/types/stack/stack-pivoting)

The link above discusses stack pivoting using `leave; ret` gadget.

I could not understand this previously, but now I got the concept with the help of someone.

The key point is that we are trying to run the `leave; ret` gadget twice, which will lead to stack pivoting.

Thus, the instructions that we are going to run are as follows. 

```
mov rsp, rbp
pop rbp
pop rip
mov rsp, rbp
pop rbp
pop rip
```

Before we write any payload, normal stack would look like this.

```
high memory
...
local variable k
return address
pointer to previous stack frame (<- rbp)
local variable 1
local variable 2
...
... (<-)rsp
...
low memory
```

Now, our target is not only a return address but also a pointer to previous stack frame.

Especially, we are going to overwrite the return address with `leave; ret` gadget and the pointer to previous stack frame with the address for stack pivoting.

When we run the first three instructions, the stack would look like this.

```
high memory
...
previous stack frame (<- rbp, normal situation)
...
local variable k (<- rsp)
return address
pointer to previous stack frame
local variable 1
local variable 2
...
...
bss section (<- rbp, situation of stack pivoting)
...
low memory
```

At this point, the `RIP` register will point to `leave; ret` gadget.
In a normal situation, the `RBP` register now points to previous stack frame.

However, since we overwrote the pointer to previous stack frame with the address for stack pivoting, we can set the value of `RBP` register whatever we want.
Normally, we set `RBP` register to `bss` section.

Finally, when we run the remaining two instructions, the memory would look like this.

```
high memory
...
pointee of bss section (<- rbp)
...
next ROP gadget (<- rsp)
bss section
...
low memory
```

You see? `RSP` register now points to `bss` section!
This is due to the first instruction for `leave` instruction, which is `mov rsp, rbp`.

After this, we are ready to run the next `ROP` gadgets with the last remaining instruction `pop rip`.

In a nutshell, with the first `leave; ret` gadget, we set the `RBP` register to `bss` section. Then, we set the `RSP` register the same as `RBP` register with the second gadget.

I did not apply `leave; ret` gadget in this challenge, but it is really worthwhile to know.
Instead, I use `pop rsp` gadget.

# Set `RBP` register
The first thing that I missed is to set `RBP` register properly.

To be specific, since I used `pop rsp` gadget, I did not care about `RBP` register.
However, it turns out that this causes program crash.

Thus, we need to set `RBP` register properly. Especially, I used `pop rbp` gadget to set `RBP` register to `bss` section.
If I do not do that, it will stay in stack memory. I do not know why but it seems that this results in program crash.

Generally, `RBP` has larger value than `RSP`, thus, I followed it.

# Make sure not to overwrite return address of read function
I could not understand this point for awhile.

In a nutshell, we should be careful about memory because the `bss` section is used as an input buffer and a call stack.
Input buffer written by `read` function can overwrite return address of `read` function, causing program crash.

For this, I used the following code.
This code adds long meaningless gadgets to the payload so that we can make sure that the overlapping between input buffer and call stack does not happen.
```
# Padding to make sure that the return address of read function is not overwritten by the input buffer.
for i in range(100):
    rop(rdi=0)
```

As an example, please consider this case.
We first peform stack pivoting and run the `read` function again by returning to the middle of the `main` function.
```
high memory
...
read return address
...
start of input buffer
low memory
```

After the function call, `RSP` register will grow downward and the `read` function will proceed.

The `read` function will read characters from standard input and write them into input buffer.

If the gap between read return address and start of input buffer is smaller than the input given by the user, it will overwrite the return address of the `read` function.

Then, when the program tries to run `ret` instruction at the end of `read` function, it will return to unexpected address.

To evade this problem, we make this gap large enough, by adding meaningless gadgets between them.
That is what the code above does.

# Do not cross the boundary of writable memory area

Previous code is also related to this topic.

In this challenge, the address of `input` is `0x405080` and the start address of writable memory is `0x405000`.

As we are using the input buffer as call stack, we should be careful about stack size.

To be specific, when we call a function, local variables will be assigned to call stack, which will enlarge stack size.

If it crosses the boundary of writable memory, we will get program crash.

However, with the previous code, we can evade this by making call stack far apart from the bounday.


For anything else, please refer to the source code.
