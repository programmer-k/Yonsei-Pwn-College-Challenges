#!/usr/bin/env bash

i=0
while read line; do
    strings "$line" | grep "Input:" -B 1 | head -n 1 > input_to_crash${i}.txt
    i=$((i + 1))
done < program_list.txt