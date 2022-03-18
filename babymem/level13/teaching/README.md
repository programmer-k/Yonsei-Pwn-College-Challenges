In this challenge, there is a `verify_flag` function, which is called just before the invocation of `vuln` function.

The function opens the flag file, reads it, and verify it.

In this case, we can exploit that the stack is shared over function invocations and the data in the stack do are alive after function return.

Luckily, the flag data is located after 48 bytes from the start of the buffer.

Therefore, if we give 48 bytes of random string, we could get the flag easily.

Use the following command to get the flag.
```
(echo "48"; python -c "print('a' * 48)") | /babymem_level13_teaching1
```
