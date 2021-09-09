In this time, you cannot just enter `./flag` in order to get the flag.
This is because it uses the function `strstr` to find out whether there is a substring `flag` in the input.
This prevents you from directly inputting the value `./flag`.

In fact, the program does nothing about the file that you give through `argv[1]` after opening it.
Thus, for `argv[1]` you can give any value.

What you really should do is creating a shellcode and gives it to the program through standard input.
There is a shellcode in an assembly form. You can refer to it by looking at `shellcode.s`.

Compile it with the following command.
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
```

Then, you can extract the `.text` section.
```
objcopy --dump-section .text=shellcode-raw shellcode-elf​
```

`shellcode.s` performs the following code.
```
open("./flag", O_RDONLY)
sendfile(1, 3, 0, 0x80);
```

Unfortunately, directly using the `shellcode_original.s` is impossible. I do not know the details, but here is the brief explanation. Opening a shell includes the operation of loading a dynamically linked libraries with absolute path. As the jail has been activated, it cannot find the libraries it needs thus always failing to open a shell. Please refer to the related article [here](https://stackoverflow.com/questions/5234088/execve-file-not-found-when-stracing-the-very-same-file).


As the `argv[0]` is useless due to substring check, we should first open the flag and read it. You know that for `x86_64` architecture, parameter passing is done via `RDI`, `RSI`, `RDX`, and `RCX`. Converting the code above into assembly code is not that hard.

By running the following code under top-level directory, you can capture the flag!
```
/babyjail_level2_teaching1 test < ~/shellcode-raw
```

One thing to note is that the file descriptor for `in_fd` is 3. This is due to the fact that I gave `test` as `argv[1]` which does not exist. At the time the codes is being run, file descriptor for fake flag has already been closed. Thus, the file descriptor we are using will become 3.
