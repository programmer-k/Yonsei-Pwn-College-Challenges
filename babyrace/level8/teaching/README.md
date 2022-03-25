In this challenge, you have to make use of the signal.

Here are the steps for getting the flag.

1. Run the challenge and use the `login` command.
2. Use the `logout` command after that.
3. After you see the text `Blocking until input!`, use `kill -SIGALRM PID` to trigger the signal handler.
4. Use the `flag` command to get the flag.

I will briefly explain how things are working.

To get the flag, we have to use `flag` command.

As it is blocked by the check, we have to make the variable `privilege_level` `-1`.

There is an instruction that decrements the variable `privilege_level` by `1`.

It can be run after we login, that is why the first step is to login.

At the stage of step 3, we have passed the check for `logout` command and decrementing the variable will always be run.

At this stage, we give a signal to this process so that the variable becomes `0` instead of `1`.

As we continue, the variable will be decremented by `1`, resulting in `-1`.

Now, it is time to run the `flag` command to get the flag as we can pass the check for the `flag` command.

For your information, you can get the process ID with the `top` utility.
