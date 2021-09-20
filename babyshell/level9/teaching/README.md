In this challenge, the `stdin` is closed after reading shellcode.
It makes the file descriptor for opening a flag to 0.
Thus, just modify the shellcode for it.
