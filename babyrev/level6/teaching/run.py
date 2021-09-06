#!/usr/bin/env python3

byte_list = '74 61 76 6a 69 62 71 68 6b'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()