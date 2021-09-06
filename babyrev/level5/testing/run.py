#!/usr/bin/env python3

# EXPECTED_RESULT is 62 64 67 68 6e 6f 71 71 74 76 78 7a
byte_list = '62 64 67 68 6e 6f 71 71 74 76 78 7a'.split()

for hexadecimal_value in byte_list:
    decimal_val = int(hexadecimal_value, 16)
    print(chr(decimal_val), end='')

print()