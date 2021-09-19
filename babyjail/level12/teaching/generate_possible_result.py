#!/usr/bin/env python3

s = 'o6kTGj5su_x?pJlM:I?sDwuUoP9/?XxU?L6?z?'
possible_result = (('P', 'Q'), ('N', 'M'), ('Q', 'R'), ('D', 'E'), ('I', 'J'), ('W', 'X'))

def print_single_character(result, idx, cnt):
    # Escape condition
    if idx == len(s):
        print(result)
        return

    if s[idx] != '?':
        print_single_character(result + s[idx], idx + 1, cnt)
    else:
        print_single_character(result + possible_result[cnt][0], idx + 1, cnt + 1)
        print_single_character(result + possible_result[cnt][1], idx + 1, cnt + 1)


print_single_character('', 0, 0)