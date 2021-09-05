#!/usr/bin/env python3

byte_list = '6e 76 6e'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()