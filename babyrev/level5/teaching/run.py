#!/usr/bin/env python3

byte_list = '76 73 6f 72 6c 61'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()