#!/usr/bin/env bash

for filename in shellcode/*; do
    f1=$(basename $filename)
    f2="${f1%.*}"

    #echo shellcode/${f2}_elf
    #echo $f2
    gcc -nostdlib -static $filename -o shellcode/${f2}_elf
    objcopy --dump-section .text=shellcode/${f2}_raw shellcode/${f2}_elf
done