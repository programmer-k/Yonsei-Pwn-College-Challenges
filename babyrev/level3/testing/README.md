The program terminates when you do not give a valid environmental variable.
It can be easily found by reverse engineering and the name of it is `lbscj`.

When you run `run.py`, then you can get the string `ghhmsjwi`.
This is the value that will be compared in the end.

`0x5555555553a` is the starting point that modify the data given by the user.
The assembly code is quite complicated, so it is quite hard to understand immediately.

When you carefully read the code and test the program with gdb, the given data is changed in the following form.

1. Remove first two characters.

2. Swap between third and fifth character.

Thus, to get identical value to `ghhmsjwi`, first add two random values, in my case `aa`, and add two and swap values.
Then it becomes `aaghsmhjwi`.

All done!
After type the following command, you will get the flag!

`lbscj=aaghsmhjwi /babyrev_level3_testing1`