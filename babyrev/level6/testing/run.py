#!/usr/bin/env python3

# EXPECTED_RESULT is 69 71 74 67 6a 76 61 6d 67.
byte_list = '69 71 74 67 6a 76 61 6d 67 6f 78 70'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()