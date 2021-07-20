#/usr/bin/env bash

gcc calculate.c -o calculate

i=0
while read line; do
    numbers=$(objdump -M intel -D "$line" | grep "movabs rdx,0x" | cut -d x -f 3)
    
    cnt=$(echo ${numbers} | wc -w)
    cnt=$((cnt - 1))

    echo ${cnt} ${numbers} | ./calculate > input_to_crash${i}.txt
    i=$((i + 1))
done < program_list.txt
