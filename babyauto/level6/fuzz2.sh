#!/usr/bin/env bash

unzip AFL.zip
cd AFL && make && cd ..

tar -xvf binutils-2.25.tar.bz2
cd binutils-2.25
CC=/home/ctf/AFL/afl-gcc ./configure
make
cd ..

mkdir findings_dir
AFL/afl-fuzz -d -i AFL/testcases/others/elf -o findings_dir /opt/all-binutils/inst/2.25/readelf -a @@