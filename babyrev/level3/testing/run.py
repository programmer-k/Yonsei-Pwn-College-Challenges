#!/usr/bin/env python3

# EXPECTED_RESULT is 67 68 68 6d 73 6a 77 69
byte_list = '67 68 68 6d 73 6a 77 69'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()