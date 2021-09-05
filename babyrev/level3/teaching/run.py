#!/usr/bin/env python3

byte_list = '68 69 6d 7a'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()