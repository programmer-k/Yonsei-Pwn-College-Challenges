#/usr/bin/env bash

gcc calculate.c -o calculate

i=0
while read line; do
    numbers=$(objdump -M intel -j .text -D "$line" | grep "movabs rdx,0x" | cut -d x -f 3)
    
    cnt=$(echo ${numbers} | wc -w)
    cnt=$((cnt - 1))

    answer=$(echo ${cnt} ${numbers} | ./calculate)
    if [ $answer != 0 ]; then
        echo ${answer} > input_to_crash_${i}.txt
    fi

    i=$((i + 1))
done < program_list.txt
