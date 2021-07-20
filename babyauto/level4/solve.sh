#!/usr/bin/env bash

i=0
while read line; do
    echo ${line} >> solve.txt
    echo input_to_crash_${i}.txt >> solve.txt
    i=$((i + 1))
done < program_list.txt

/babyauto_level4_teaching1 < solve.txt