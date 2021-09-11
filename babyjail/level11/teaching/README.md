In this problem, you are allowed to use the following system calls.
1. Allowing syscall: read (number 0)
2. Allowing syscall: nanosleep (number 35)

Use the following code to solve this problem.
```
read(3, buf, 0x80);
struct timespec t;
t.tv_sec = *(buf+x);
t.tv_nsec = 0;
nanosleep(&req, NULL);
```

What the code above means is that you first read all the flag values and sleep for each byte value.
By observing the time it sleeps, we can find out which character it has read.
Unfortunately, you can only send a single byte through this manner.
Thus, you should loop the the code above to get the full flag.

This means that we should give the program different shellcode to get the different value at different position.
Since I think it is more convenient to modify the assembly code rather than compiled one, I have created some scripts to do this.
The following code will generate 100 shellcodes which sleeps for a single byte value of the flag file from index 0 to 99 through `nanosleep` function.
```
mkdir shellcode
./generate_assembly.py
./compile_assembly.py
```

Now, let's talk about `main.c`.
It will the challenge program 100 times.
For each execution, it records the current time just before and after the program execution.
Then, it calculates the difference between them. This difference is a single byte value from flag file.

Running the following commands will lead you to the flag.
```
gcc main.c -lm  # lm is for math.h library.
./a.out
cat ./flag
```