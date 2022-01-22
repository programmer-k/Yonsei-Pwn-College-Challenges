In this challenge, you have to write down non-zero value into some variable through buffer overflow.

I do not fully understand the explanation given by the challenge and will just focus on the problem solving itself.

The challenge says that the stack frame is 176 bytes in total.

Thus, I just entered 176 for the payload size which is a large enough number for this challenge.

For the payload, I just used the following python code.
```
'a' * 176
```
