#!/usr/bin/env bash

i=0
for FILE in /home/ctf/orcs_foo/*; do
    echo "${FILE}"
    echo "/opt/all-binutils/inst/2.11/readelf" >> input.txt
    echo "${FILE}" >> input.txt
    i=$((i + 1))
done

/babyauto_level5_teaching1 < input.txt
