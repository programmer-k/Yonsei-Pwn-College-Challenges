This problem is quite different from the previous problems.
In a nutshell, you can only make use of the communication between parent and child process created by the function `socketpair`.
You really should read the explanatory output and the decompiled source code of the given binary.

The binary is kind enough that it shows you how to communicate with the given socket pair and how to send the command from child process to the parent one.
The given example is as follows.
```
write(sock2, "print_msg:Executing the shellcode. Good luck!", 128);
```

The parent process will receive the string and run the following code.
```
puts("Executing the shellcode. Good luck!");
```

As they give us hint, we can easily follow it.
We should generate a shellcode so that the child process gives the following string to the parent process.
```
"read_file:/flag"
```

You can see the shellcode from the file `shellcode1.s`.
After the parent process receives the command above, it will open the file and send the contents of it to the child process through the socket.
Then, what we need is the shellcode for reading and sending to the parent process to print out.
You can refer the the file `shellcode2.s`.

Running the following commands will lead you to the flag.
```
gcc -nostdlib -static shellcode2.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyjail_level13_teaching1 < ~/shellcode-raw
```
