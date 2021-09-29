This challenge requires that every byte in your shellcode is unique!
The first thing that come to my mind is that we should use two `syscall`.

The solution for this problem is to use 2 stage payload.
This is because the second stage payload is free from constraint.

Thus, firstly write a short shellcode that tries to read the second stage payload.
The first shellcode must follow the constraint.
You can see the shellcode in `shellcode_1.s`.
I did not set `RDX` register because it is set to large enough number due to previous code.

In this challenge, I newly introduce `pwntools`.
This is because the redirection cannot decide when to send input.
The best way is to firstly give the first shellcode and give the second shellcode after that.

The second shellcode does not have any constraint to follow.
Thus, it is just standard shellcode to read the flag.

Finally, `run.py` sends the first shellcode and sends the second one after that.
It will lead you to the flag.
