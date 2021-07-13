#/usr/bin/env bash

i=0
while read line; do
    code=$(objdump -M intel -D "$line" | grep "movabs rdx,0x" | cut -d , -f 2)
    echo $(($code)) > input_to_crash${i}.txt
    i=$((i + 1))
done < program_list.txt
