The difference between previous challenge and this one is as follows.

```
iVar1 = rand();
...
local_b0 = malloc((long)(iVar1 % 872 + 128));
```

As you can see, it includes some randomness.

At first, I come up with an idea that it does not use `srand` function, which means the `rand` function will always return the same value.

I print the return value of the `rand` function on two computers and they are the same, which is `1804289383`.

Therefore, `1804289383 % 872 + 128`, which is `303` should be the answer.

However, it did not work. I do not know why.

Thus, I made a simple script with bruteforcing from 0 to 999.

By running the script, you will get the flag.
