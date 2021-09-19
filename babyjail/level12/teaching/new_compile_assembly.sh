#!/usr/bin/env bash

for filename in new_shellcode/*; do
    f1=$(basename $filename)
    f2="${f1%.*}"

    #echo shellcode/${f2}_elf
    #echo $f2
    gcc -nostdlib -static $filename -o new_shellcode/${f2}_elf
    objcopy --dump-section .text=new_shellcode/${f2}_raw new_shellcode/${f2}_elf
done