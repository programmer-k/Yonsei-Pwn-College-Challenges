This challenge is listening for connections on TCP port 1337.

This is a multi-thread program as it creates a new thread for each connection.

There are 5 functionalities that you can use. They are login, logout, sudo, flag, and quit.

Our objective is to get the flag with `flag` command.

However, before opening and printing the flag file there is a check as follows.
```
if (privilege_level == 0) {
    fwrite("You are not logged in!\n",1,0x17,param_2);
}
else if (privilege_level == 1) {
    fwrite("Your privilege level is too low!\n",1,0x21,param_2);
}
```

This means that the `privilege_level` should not be 0 or 1 to get the flag.

Firstly, we have to use the `login` command.

The `login` command will set the `privilege_level` to 1.

After that, we have to run the `logout` command with two connections nearly at the same time.

Please refer to the following code snippets from `logout` command.
```
if (privilege_level == 0) {
    fwrite("You are not logged in!\n",1,0x17,param_2);
}
else {
    fwrite("Dropping one privilege level.\n",1,0x1e,param_2);
    fwrite("Blocking until input!\n",1,0x16,param_2);
    __isoc99_fscanf(param_1,"%127s",local_a8);
    privilege_level = privilege_level - 1;
}
```

As you can see, `privilege_level` decreases by 1 with the `logout` commmand.

However, there is a condition for this. You should be logged in beforehand.

Therefore, with a single connection, there is no way to make the `privilege_level` setting to -1 as the second command does not take any effects.

That is why we are using the two connections.

There is a user input just before the decrease in `privilege_level`, which makes the exploitation easy.

With two connections, we run `logout` command.

As the current `privilege_level` is 0, the else body will be run for both connections.

After that, we give any input to continue.

Then, `privilege_level` will decrease by 1 twice and it will eventually become -1.

Finally, we can get the flag data with `flag` command.
