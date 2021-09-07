#!/usr/bin/env python3
0x6976726670;

byte_list = '64 67 67 67 6a 74 76 76 77 78 79 7a'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()