#!/usr/bin/env python3

byte_list = '76 6d 68 61 79 61 74 69 6e 74 6e 74 79 65 67 79'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()