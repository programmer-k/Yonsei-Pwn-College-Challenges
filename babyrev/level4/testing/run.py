#!/usr/bin/env python3

# EXPECTED_RESULT is 72 70 67 70 62 69 7a 6d.
byte_list = '72 70 67 70 62 69 7a 6d'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()