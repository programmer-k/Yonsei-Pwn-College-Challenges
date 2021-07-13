#!/usr/bin/env bash

i=0
while read line; do
    echo ${line} >> solve.txt
    echo input_to_crash${i}.txt >> solve.txt
    i=$((i + 1))
done < program_list.txt

/babyauto_level1_teaching1 < solve.txt