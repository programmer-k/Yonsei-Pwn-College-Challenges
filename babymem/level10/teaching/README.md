The challenge reads flag value but does not print it.

You need to find a way to print the flag value.

At the end of the `vuln` function, there is a `fprintf` function call that prints the following string.

```
"You said: %s\n"
```

How can we utilize this function call?

The answer lies in the ordering of the local variables.

Here is the simple structure of the stack.

```
[Top]
...
buffer_ptr
...
flag_buffer
...
buffer
...
[Bottom]
```

We know that `%s` reads and prints the value until it sees `NULL` character.

Therefore, if we write up to just before the `flag_buffer`, two strings, which are the input we gave and the flag value, would be printed together.

Then, we have to know how long we should input.

You can find it by `gdb`.

```
flag_buffer: 0x7ffd1855a2e1
buffer: 0x7ffd1855a2d0
```

`0x7ffd1855a2e1` - `0x7ffd1855a2d0` = `0x11`

Thus, if we input exactly 17 bytes, then the flag value will be printed.

You can use the following command.

```
(echo "17"; echo "aaaaaaaaaaaaaaaaa") | /babymem_level10_teaching1
```