#!/usr/bin/env python3

byte_list = 'c8 f1 54 fe cd 1d b9 85 5d f8'.split() # EXPECTED RESULT
result = []
for i in range(len(byte_list)):
    decimal_val = int(byte_list[i], 16)

    # Fourth mangler
    if i % 2 == 0:
        decimal_val = decimal_val ^ int('9d', 16)
    else:
        decimal_val = decimal_val ^ int('ce', 16)

    result.append(decimal_val)

# Third mangler
result[0], result[1] = result[1], result[0]

# Second mangler
result.reverse()

for i in range(len(result)):
    # First mangler
    rem = i % 3
    if rem == 0:
        operand = int('53', 16)
    elif rem == 1:
        operand = int('ba', 16)
    else:
        operand = int('3a', 16)

    result[i] = result[i] ^ operand

    print(chr(result[i]), end='')
print()