The value of stack canary is the same throughout a process regardless of each function invocation.

In this challenge, stack canary is enabled.

Therefore, we need to know it before overwriting return address.

We can get it with buffer overflow.

After the user input, there is a print instruction that prints the user input.
```
fprintf(local_70,"You said: %s\n",local_88)
```

As stack canary starts with `0x00`, this will only print the user input in a normal situation.

However, when you overwrite up to the first byte of stack canary, which is `0x00`, we can leak the stack canary.

The next step is to invoke the function again.

This can be done via a backdoor as shown below.
```
pcVar2 = strstr((char *)local_88,"REPEAT");
if (pcVar2 == (char *)0x0) {
puts("Goodbye!");
uVar3 = 0;
}
else {
puts("Backdoor triggered! Repeating vuln()");
uVar3 = vuln(local_9c,local_a0);
}
```

`strstr` will return `NULL` if the user input does not contain `REPEAT`.

To invoke the function again, we have to contain a string `REPEAT`. The position of this string does not matter.

Then, we have another chance to give an input again.

This time, we know the stack canary. Thus, we can modify the return address without messing it up.

You might have to run the script multiple times due to `PIE`.

Also, to get the flag, the return address should be the instruction after checking the parameter, which is `0x19fd`.
