#!/usr/bin/env python3

with open("shellcode.s", "r") as f1:
    lines = f1.readlines()
    line = lines[15]

    for i in range(100):
        with open("shellcode/shellcode_%d.s" % i, "w") as f2:
            f2.writelines(lines[:15] + [lines[15].replace("x", "%d" % i)] + lines[16:])
            