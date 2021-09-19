In this problem, you are allowed to use the following system call.
1. Allowing syscall: read (number 0)

I firstly used the following code to solve this problem.
```
read(4, buf, 0x80);
int temp;
for (int i = 0; i < 100; i++)
    for (int j = 0; j < buf[i] - 33; j++)
        // Loop that takes 10 seconds
        for (int k = 0; k < 0x7A8000000; k++)
            temp++;
```

To get the loop that takes 10 seconds, I did trial and error to get `0x7A8000000`.
Furthermore, `cmp` operation with large immediate value results in compile error, so I first `mov` immediate value into register and used `cmp` operation.
You can see the assembly code in `ten_sec_loop.s`.

Now, the problem is you do not have any means to transfer the data up to the parent process nor to print the data in the buffer.
However, there is always a way to do.
Use the similar method to the previous problem.
For each byte, do compute intensive work proprotional to the byte value.
Measuring the time difference will lead you to the flag.

We should give the program different shellcode to get the different value at different position.
Since I think it is more convenient to modify the assembly code rather than compiled one, I have created some scripts to do this.
The following code will generate 100 shellcodes which sleeps for a single byte value of the flag file from index 0 to 99 through 10 seconds loop.
In fact, I first tried with 1 second loop, but it did not work. Thus, I moved to 10 seconds.
```
mkdir shellcode
./generate_assembly.py
./compile_assembly.sh
```

Now, let's talk about `main.c`.
It will the challenge program 100 times.
For each execution, it records the current time just before and after the program execution.
Then, it calculates the difference between them. This difference is a single byte value from flag file.
The difference is that it uses `chrono` standard library.
`difftime` returns value of type double, but it is actually an integer that contains trailing zeros.
Since I need more accurate time measurement, I used `chrono` that I can extract time with millisecond granularity.

Run the following commands.
```
g++ main.cpp
./a.out
cat ./flag
```

Then, I got the following result that you can also see from the file `answer.txt`.
You need to be patient to wait for the result because it takes at least several hours.
```
pwn_college{o6kTGj5su_xQpJlM:INsDwuUoP9/RXxUEL6IzW} # First trial
pwn_college{o6kTGj5su_xPpJlM:IMsDwuUoP9/QXxUDL6JzX} # Second trial
pwn_college{o6kTGj5su_x?pJlM:I?sDwuUoP9/?XxU?L6?z?} # Combine first and second, setting ? as different.
```

As you can see, there is some error, so there are many candidates.
Thus, I have created short python script called `generate_possible_result.py`, which create all possible result.
I put all the 64 flags into the web, but all of them are wrong.

What's the problem?
As you can see, all the `?` values are capital letters, which have smaller ASCII codes compared to lowercase letters.
It means they loop less than lowercase letters, which might result in wrong character.
The key point is that even though we have found the value that runs nearly 10 seconds, we do not know the server situation since we are not the only one using. Thus, there always could be some errors due to CPU scheduling and so on.

We need another approach to get exact flag values!

Here is the simple explanation for new approach implemented in `new_main.cpp`.
For each flag byte value, run the challenge program 128 times.
For each iteration, give the shellcode which performs the following.
If the given flag byte value is equal to the iteration time, runs loop the programs for 10 seconds, otherwise, exit immediately.

Thus, now we need to provide different shellcode not only for each byte value but also for each iteration.
We need to create 12800 shellcodes.
100 (the number of byte values) * 128 (the number of iterations for each byte value) = 12800

The following command will make 12800 shellcodes for you.
```
mkdir new_shellcode
./new_generate_assembly.py
./new_compile_assembly.sh
```

Run the following commands will lead you to the flag!
```
g++ main.cpp
./a.out > output.txt
cat ./flag
```

After that, we can observe the results with the following commands.
```
# Run these two commands in separate two shells, respectively.
tail -f flag
tail -f output.txt
```

I do not know, but sometimes it gets the wrong value.
For confirmation, please run several times.
I have run three times and compared the results and get the actual flag.
Please refer to the `answer.txt'.