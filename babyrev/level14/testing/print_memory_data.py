#!/usr/bin/env python3

# From MEM[0x80] to MEM[0x85]
s = "0x2f 0x66 0x6c 0x61 0x67 0x0"

for element in s.split():
    print(chr(int(element, 16)), end='')
print()
