The challenge uses `mmap`.

This is similar to the previous challenge.

Fill the space with non-NULL bytes.

The output of the challenge shows how many bytes you should enter.

You can use the following command.

```
(echo "28672"; python3 -c "print('a' * 0x7000)") | /babymem_level11_teaching1
```