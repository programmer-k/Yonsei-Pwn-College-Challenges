#!/usr/bin/env python3

# EXPECTED_RESULT is 69 76 7a
byte_list = '69 76 7a'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()