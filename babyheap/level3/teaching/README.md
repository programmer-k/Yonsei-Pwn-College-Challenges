In this challenge, `read_flag` calls two `malloc` functions.

Thus, we have to prepare two `malloc` calls before `read_flag`.

```
[*] Function (malloc/free/puts/read_flag/quit): malloc
Index: 0
Size: 165
[*] allocations[0] = malloc(165)
[*] allocations[0] = 0x5624ae129ac0
[*] Function (malloc/free/puts/read_flag/quit): malloc
Index: 1
Size: 165
[*] allocations[1] = malloc(165)
[*] allocations[1] = 0x5624ae129b70
[*] Function (malloc/free/puts/read_flag/quit): free
Index: 0
[*] free(allocations[0])
[*] Function (malloc/free/puts/read_flag/quit): free
Index: 1
[*] free(allocations[1])
[*] Function (malloc/free/puts/read_flag/quit): read_flag
[*] flag_buffer = malloc(165)
[*] flag_buffer = 0x5624ae129b70
[*] flag_buffer = malloc(165)
[*] flag_buffer = 0x5624ae129ac0
[*] read the flag!
[*] Function (malloc/free/puts/read_flag/quit): puts
Index: 0
[*] puts(allocations[0])
Data: pwn_college{...}
```

When you look into the output, you can figure out that `malloc` chooses memory in a LIFO manner.

That is why the order becomes reversed.

```
for (local_134 = 0; local_134 < 2; local_134 = local_134 + 1) {
    printf("[*] flag_buffer = malloc(%d)\n",165);
    local_128 = malloc(0xa5);
    printf("[*] flag_buffer = %p\n",local_128);
}
```
Moreover, when you decompile the binary with `Ghidra`, `read_flag` does not use the memory given by the first `malloc` call.

Thus, we should print the data at `0x5624ae129ac0`, which is given by the second `malloc` invocation.

In other words, index 0 is our target.
