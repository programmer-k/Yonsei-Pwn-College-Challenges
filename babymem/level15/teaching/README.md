This challenge is about bruteforcing stack canary and return address.

The challenge have to be accessed via socket and the server forks to handle client request.

As the stack canary and return address remains identical after fork, we can bruteforce them.

One thing to note is that the output is printed to the server side, not a client side.

To figure out the input length to the stack canary, we should analyze the assembly.

To be specific, the program uses the value stored in a local variable as a parameter for `read` function.

Thus, you have to go a little bit up and check what value is stored in that local variable.
