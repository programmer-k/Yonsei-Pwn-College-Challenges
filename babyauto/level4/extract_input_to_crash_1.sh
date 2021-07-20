#!/usr/bin/env bash

i=0
while read line; do
    answer=$(strings "$line" | grep "Input:" -B 1 | head -n 1)
    
    if ! [[ "$answer" =~ [^a-zA-Z] ]]; then
        echo "${answer}" > input_to_crash_${i}.txt
    fi

    i=$((i + 1))
done < program_list.txt