#!/usr/bin/env python3

byte_list = '63 66 6b 6e 72 73'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()