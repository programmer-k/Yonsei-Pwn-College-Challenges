In this challenge, you can perform five operations which are `malloc`, `free`, `puts`, `read_flag`, and `quit`.
You need to get the flag using these operations.

You can solve the challenge with the following command.
```
(cat input.txt; cat) | /babyheap_level1_teaching1
```

I will briefly explain what it does.

`read_flag` command internally allocates 581 bytes and writes the flag data into newly allocated region.

We can exploit this.

Firstly, with the `malloc` command, dynamically allocate 581 bytes and then free it.

I do not well, but it seems that the allocator remembers deallocated memory region and tries to reuse it.

Secondly, run `read_flag` command.

With the first phase, we have prepared deallocated memory region.

Thus, the allocator will reuse the memory region.

This will make two pointer variables in the stack (one for `malloc` and `free`, another one for `read_flag`) identical.

In other words, they will point to the same location in the heap.

This can be identified with the output from the binary.

For example, `allocations[0]` and `flag_buffer` points to the same location, which is `0x55f20b8966c0`.
```
[*] Function (malloc/free/puts/read_flag/quit): Size: [*] allocations[0] = malloc(581)
[*] allocations[0] = 0x55f20b8966c0
[*] Function (malloc/free/puts/read_flag/quit): [*] free(allocations[0])
[*] Function (malloc/free/puts/read_flag/quit): [*] flag_buffer = malloc(581)
[*] flag_buffer = 0x55f20b8966c0
```

After the `read_flag` command, the heap memory will be filled with flag data.

This can be access with previously deallocated dangling pointer.

Therefore, `puts` command will show you the flag.
