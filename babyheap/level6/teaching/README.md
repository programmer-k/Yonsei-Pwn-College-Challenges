In this challenge, you have to leak out a secret stored at `0x429521`.

To do that, we will modify the `fd` pointer after freeing the heap memory.

1. Call `malloc` function twice with the same size.
2. Free them.

This will make the `fastbin` consisting of two elements.

3. Call `scanf` function to modify the `fd` pointer of the top element to `0x429521`.
4. Call `malloc` function twice with the same size.

At this point, the first call would be a normal heap memory.

However, the second call will return the address `0x429521`.

This happens because the first call to `malloc` function will pop the top element of `fastbin` and update the top element following the `fd` pointer.

However, as we have modified the `fd` pointer to where we want, the top element of `fastbin` will now point to non-heap area but treat it as a heap memory.

Thus, at the second call, we can get the address `0x429521`.

5. Call `puts` function to read secret data stored at `0x429521`.
6. Use `send_flag` command to get the flag.

In summary, you can access anywhere you want via modifying the `fd` pointer.
