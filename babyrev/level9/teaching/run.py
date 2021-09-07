#!/usr/bin/env python3

byte_list = '33 0d c4 0b 3d 08 cc 13 3c 1e'.split()

for i in range(len(byte_list)):
    decimal_val = int(byte_list[i], 16)

    # Third mangler
    rem = i % 4
    if rem == 0:
        operand = int('56', 16)
    elif rem == 1:
        operand = int('67', 16)
    elif rem == 2:
        operand = int('bd', 16)
    else:
        operand = int('60', 16)

    decimal_val = decimal_val ^ operand

    print(chr(decimal_val), end='')

print()