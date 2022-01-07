In this challenge, the problem is that now you do not get the stack address for free.
Furthermore, due to ASLR, you cannot get the stack address statically.

I firstly struggled with leaking the stack address but I eventually gave up.

To use the system call `open`, I have to store the string `"/flag"` somewhere but not in register.
Stack was the previous target but now it becomes unattackable.
The actual way that I solved this problem is using the global variable instead of stack.

When you look into the binary with `Ghidra`, then you will see there are several global variables.
We could use these global variables to store the string `"/flag"`.

To store the string into the global variable, we can use the `read` system call.
```
read(0, 0x405080, 5);   // 0x405080 is the address of a global variable.
```
The code above will read 5 bytes from the standard input and store the value into the global variable.

After that, we can do the things in the same way as before.
```
open("/flag", 0);  // 0 is O_RDONLY.
sendfile(1, 3, 0, 400);
```

The last thing you should care is that the input should be given twice separately.
The first input is for the payload and the second one is for the string.
To do this, you can use the following command.
```
(cat payload; sleep 3; echo "/flag"; cat) | /babyrop_level5_teaching1
```
You see that the two inputs are given separately using the command `sleep`.
