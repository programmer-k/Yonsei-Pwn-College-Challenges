In this challenge, you need another way to leak the stack canary.

Specifically, the `fprintf` function that prints user input now uses a format string of `%.298s`, which means that it will print only up to 298 characters.

As the stack canary starts from 314th character, we cannot get it even if we provide correct payload.

However, there is a workaround for this.

Concerning the stack canary is the same value throughout the function call in a process, we can make use of old stack canary value in the stack.

To be specific, before calling `vuln` function, there would be a lot of function invocations and they will leave some data including stack canary.

As you may know, when a function returns, it does not erase the data itself in stack frame.

That is why we can find old stack canary value in the stack and make use of it.

After we leak the stack canary, we can jump to `win` function by overwriting return address partially.

Due to `PIE`, you need to run the script multiple times to get the flag.

