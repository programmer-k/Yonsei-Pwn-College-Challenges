In this problem, you are allowed to use the following system calls.
1. Allowing syscall: read (number 0)
2. Allowing syscall: exit (number 60)

We cannot use the trick for the previous problem.
I think that even though the programmer does not add `x86` architecture to the `seccomp` explicitly, they automatically add it because `x86_64` is compatible with `x86`.

Use the following code to solve this problem.
```
read(3, buf, 0x80);
exit(*(buf + x));
```

What the code above means is that you first read all the flag values and exit the program with a status of a single character value.
The point that you should exploit in this problem is that the status value, which could be the return value in the main function or the status argument in the `exit` function in normal case, can be observed by the parent process.
Unfortunately, you can only send a single byte through this manner.
Thus, I come up with the code above to first read all values and return each byte from the beginning to the end.

This means that we should give the program different shellcode to get the different value at different position.
Since I think it is more convenient to modify the assembly code rather than compiled one, I have created some scripts to do this.
The following code will generate 100 shellcodes which return a single byte of the flag file from index 0 to 99 through `exit` function.
```
mkdir shellcode
./generate_assembly.py
./compile_assembly.py
```

Before going further, I would like to introduce the following command which is really useful.
The option `-f` lets you see the system calls not only from the parent process but also from the child processes.
As we will run the challenge program as a child process, it is really helpful to debug.
The option `-v` and `-s` shows you all the parameters for the system which has been abbreviated before.
With the exercise mode and these options, you can get the flag without reading a single byte one by one and appending it.
```
sudo strace -f -v -s 500 /path/to/executable
```

Now, let's talk about `main.c`.
In fact, I first tried to use the `execve` function, but the problem is it does not support redirection which is needed for giving the shellcode through standard input.
Copying and pasting the shellcode in a GUI environment also does not work at all.
Thus, I come up with the function `system`, which works with redirection.

Then, the problem beomes how should I get the return value.
For the inital version with `execve`, I first forked my program.
Then, the parent process wait until the child process finishes, and the child process runs and returns the value.
After that, the parent process get the return value and print/store it somewhere.
Finally, repeat this until we get all the flag values.

However, as I moved to `system` function, the previous mechanism did not work.
When I look into `strace`, `system` creates more than one process.
Also, the return value gets back to one or two parent process but not to the `main` program.
Then I found out from the Linux manual page that `system` returns the status value through the return value, thus we do not have to wait for it.
Thus, the structure becomes simpler.

What main function does is just running the challenge program, while giving all the assembly code to get each byte.
Running the following commands will lead you to the flag.
```
gcc main.c
./a.out
cat ./flag
```