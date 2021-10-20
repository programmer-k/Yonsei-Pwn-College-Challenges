In this challenge, the ASLR, which stands for address space layout randomization, is applied.
And I believe, from my experience, that the code segment is not affected.
The problem is the address of stack is changed every time we run the challenge.

Firstly, there are no guidelines that we can follow.
There are no functions for easy exploitation.
Thus, we have to use the standard method, which is `open` and `sendfile`.

Fortunately, there is a ROP gadget for `syscall`.
Even though there is no `ret` after `syscall` on the output `rop_result.txt`, it actually exists! So, we can use it.

For creating payload, you can refer to `create_payload.py`.
It is the same as the normal shellcode, setting the register values and invoking system calls.

However, there is a problem due to ASLR.
For the `open("/flag", 0)` system call, the first argument is the address of the string `/flag`.
Thus, we first have to write the string to the memory, probably stack, and then get the address of the string.
You see the problem. Due to ASLR, you cannot statically retrieve the address of the string located at stack.

Thus, the script `create_payload.py` reads in the stack address provided by the challenge and calculates the address of the string `flag`.

Now, we have to first run the challenge, and then run the script, and give the payload to the challenge finally.
This kind of procedure cannot be done by simple redirection.
Thus, I used `pwntools`.

The new feature that is really useful for debugging is that you can `strace` within the scripts written in `pwntools`.
Please refer to the line 7 from the file `run.py`.

The procedure is as follows.
Firstly, run the `run.py` to run the challenge.
It will print the address of the stack. Copy it for later use.
Secondly, run the `create_payload.py` and input the address that we have copied from.
It will generate the payload for you.
Lastly, press the enter on the process of `run.py`.
It will reads the payload and send it to the challenge.

All done.
