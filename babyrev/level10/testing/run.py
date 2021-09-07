#!/usr/bin/env python3

byte_list = '6b 43 66 41 62 46 63 45 7a 5e 7b 5e 76 53 75 53 72 56 70 55'.split() # EXPECTED RESULT
result = []
for i in range(len(byte_list)):
    decimal_val = int(byte_list[i], 16)

    # Fourth mangler
    if i % 2 == 0:
        decimal_val = decimal_val ^ int('11', 16)
    else:
        decimal_val = decimal_val ^ int('34', 16)

    result.append(decimal_val)

# Third mangler
result.reverse()

# Second mangler
result[4], result[5] = result[4], result[5]

for i in range(len(result)):
    print(chr(result[i]), end='')
print()