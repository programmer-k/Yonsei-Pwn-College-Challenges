In this challenge, there is no `vuln` function now.

Instead, buffer overflow vulnerability due to `read` function happens in `main` function.

That means now the return address for `main` function is in `libc` library.

Thus, due to `PIE`, we should use the gadget in `libc` library to modify the return address.

However, the problem is that there is no `leave; ret` gadget near the original return address.

To solve this problem, I modified three bytes instead of two, leading to low success rate, which is 1 over 4096.

For convenience, I added a loop in the source code to run the program until I get the flag.

The script crashes after several thousand times of invocation, so you need to run the script again manually.

Everything else remains the same as before.
