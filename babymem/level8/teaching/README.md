Warning! The challenge gives wrong number for padding!

It should be 136 bytes instead of 144 bytes.

In this challenge, there is an addtional copy and check.

Specifically, it uses dynamically allocated memory to get input and then copies it back to the stack.

Between them, there is a length check using `strlen` function.

We have to bypass this check to make buffer overflow happen.

`strlen` finds the position of the `NULL` character to count the length of the given string.

Thus, if we use `NULL` character as a padding, we can fake the check.

Everything else is the same as before.

You can use the following commands to get the flag.

You might have to run the last command multiple times to get the flag.

```
./run.py
(echo "138"; cat payload) | /babymem_level8_teaching1
```