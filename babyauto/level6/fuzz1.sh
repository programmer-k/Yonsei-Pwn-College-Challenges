#!/usr/bin/env bash

unzip Melkor.zip
cd Melkor_ELF_Fuzzer && make && cd ..

#echo | Melkor_ELF_Fuzzer/melkor -a Melkor_ELF_Fuzzer/templates/foo -n 1000
#mv orcs_foo/Report_foo.txt .

echo | Melkor_ELF_Fuzzer/melkor -H -P -D -R -N -Z Melkor_ELF_Fuzzer/templates/foo -n 10000
mv orcs_foo/Report_foo.txt .

echo | Melkor_ELF_Fuzzer/melkor -a Melkor_ELF_Fuzzer/templates/foo.o -n 10000
mv orcs_foo.o/Report_foo.o.txt .

echo | Melkor_ELF_Fuzzer/melkor -a Melkor_ELF_Fuzzer/templates/foo_static -n 10000
mv orcs_foo_static/Report_foo_static.txt .

echo | Melkor_ELF_Fuzzer/melkor -a Melkor_ELF_Fuzzer/templates/libfoo.so -n 10000
mv orcs_libfoo.so/Report_libfoo.so.txt .

echo | Melkor_ELF_Fuzzer/melkor -a Melkor_ELF_Fuzzer/templates/foo_dl_iterate_phdr -n 10000
mv orcs_foo_dl_iterate_phdr/Report_foo_dl_iterate_phdr.txt .

echo | Melkor_ELF_Fuzzer/melkor -a Melkor_ELF_Fuzzer/templates/foo_full_relro -n 10000
mv orcs_foo_full_relro/Report_foo_full_relro.txt .

echo | Melkor_ELF_Fuzzer/melkor -A Melkor_ELF_Fuzzer/templates/foo_stackprotector_execstack -n 10000
mv orcs_foo_stackprotector_execstack/Report_foo_stackprotector_execstack.txt .

echo | Melkor_ELF_Fuzzer/melkor -a Melkor_ELF_Fuzzer/templates/libfoo.o -n 10000
mv orcs_libfoo.o/Report_libfoo.o.txt .

echo | Melkor_ELF_Fuzzer/melkor -A Melkor_ELF_Fuzzer/templates/foo_libfoo -n 10000
mv orcs_foo_libfoo/Report_foo_libfoo.txt .

echo | Melkor_ELF_Fuzzer/melkor -A Melkor_ELF_Fuzzer/templates/foo_dlopen -n 10000
mv orcs_foo_dlopen/Report_foo_dlopen.txt .