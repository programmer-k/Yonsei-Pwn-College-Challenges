Please refer to the `output_analysis.txt` for detailed information.

Basically, I did not check by myself, but it seems that the challenge checks whether the first 9 bytes that the user gives are identical to the given values.

If they are different, the challenge does something and eventually prints a message and exits.

The values are given below.
```
## MEM[0xd9] = 0xa9
## MEM[0xda] = 0x3a
## MEM[0xdb] = 0x95
## MEM[0xdc] = 0xd1
## MEM[0xdd] = 0xc1
## MEM[0xde] = 0x3b
## MEM[0xdf] = 0xa9
## MEM[0xe0] = 0x48
## MEM[0xe1] = 0x8e
```

Since they are not printable, we have to use the following commands.
```
echo -e "\xa9\x3a\x95\xd1\xc1\x3b\xa9\x48\x8e" | /babyrev_level14_teaching1
```

By the way, it seems that the last 2 bytes that the user gives are ignored.
