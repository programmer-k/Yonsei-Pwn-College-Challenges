#!/usr/bin/env python3

byte_list = '5f 58 59 59 59 46 4d 4b 44 45 46 53'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)

    # Third mangler
    decimal_val = decimal_val ^ int('3c', 16)
    print(chr(decimal_val), end='')

print()