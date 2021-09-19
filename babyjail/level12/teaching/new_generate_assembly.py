#!/usr/bin/env python3

with open("new_shellcode.s", "r") as f1:
    lines = f1.readlines()

    for i in range(100):
        for j in range(128):
            with open("new_shellcode/new_shellcode_%d_%d.s" % (i, j), "w") as f2:
                f2.writelines(lines[:13] + [lines[13].replace("x", "%d" % i)]  + lines[14:16] + [lines[16].replace("y", "%d" % j)] + lines[17:])
