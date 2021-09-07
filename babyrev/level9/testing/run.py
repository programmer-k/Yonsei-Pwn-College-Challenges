#!/usr/bin/env python3

byte_list = '65 67 6a 6c 6d 6f 74 75 77 78'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()