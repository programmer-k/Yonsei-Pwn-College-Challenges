#!/usr/bin/env python3

from pwn import *

p = remote('localhost', 1337)
p.interactive()
