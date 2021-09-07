#!/usr/bin/env python3

byte_list = 'ca 11 fb 99 5d aa c9 0c'.split()

for i in range(len(byte_list)):
    decimal_val = int(byte_list[i], 16)

    # Third mangler
    rem = i % 3
    if rem == 0:
        operand = int('1a', 16)
    elif rem == 1:
        operand = int('99', 16)
    else:
        operand = int('2e', 16)

    decimal_val = decimal_val ^ operand

    # Second mangler
    decimal_val = decimal_val ^ int('76', 16)

    # First mangler
    if i % 2 == 0:
        decimal_val = decimal_val ^ int('d7', 16)
    else:
        decimal_val = decimal_val ^ int('99', 16)

    print(chr(decimal_val), end='')

print()