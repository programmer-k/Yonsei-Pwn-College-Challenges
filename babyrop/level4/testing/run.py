#!/usr/bin/env python3

import pwn


# Create a process
#binary = pwn.process(['strace', '/babyrop_level4_testing1'])  # Debugging purpose
binary = pwn.process(['/babyrop_level4_testing1'])

# Receive lines
print(binary.recvline_contains("located at: 0x"))

input('Press [Enter] to continue..')

# First input
with open("payload", "rb") as f1:
    binary.sendline(f1.read())

binary.interactive()