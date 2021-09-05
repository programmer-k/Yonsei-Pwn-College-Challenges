#!/usr/bin/env python3

# EXPECTED_RESULT is 6d 72 71
byte_list = '6d 72 71'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()