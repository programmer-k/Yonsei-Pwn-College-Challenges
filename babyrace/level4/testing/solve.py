#!/usr/bin/env python3

from pwn import *

FILENAME = '/babyrace_level4_testing1'

while True:
    try:
        p = process([FILENAME, 'f'])
        p.recvline_startswith(b'You win!')
        print(p.recvline())
        break
    except EOFError:
        p.close()
