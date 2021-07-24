#!/usr/bin/env bash

#while read program_name; do
#    echo "${program_name}"
#    for FILE in /home/ctf/findings_dir/crashes/*; do
#        echo "${program_name}" >> input.txt
#        echo "${FILE}" >> input.txt
#    done
#done < program_list.txt

program_name="/opt/all-binutils/inst/2.22.51/readelf"
echo "${program_name}"
for FILE in /home/ctf/orcs_foo_dlopen/*; do
    echo "${program_name}" >> input.txt
    echo "${FILE}" >> input.txt
done

(cat input.txt; cat) | /babyauto_level6_teaching1
