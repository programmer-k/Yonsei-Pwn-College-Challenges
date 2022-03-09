```
This challenge is listening for connections on TCP port 1337.
The challenge supports one connection at a time, but unlimited connections.
```

Here are some useful background knowledge before you start.

[Stack Canaries - CTF 101](https://ctf101.org/binary-exploitation/stack-canaries/)

[bufferCanary.png](https://manybutfinite.com/img/stack/bufferCanary.png)

Basically, this challenge is an example of the section `Bruteforcing a Stack canary` from [Stack Canaries - CTF 101](https://ctf101.org/binary-exploitation/stack-canaries/).

You can fork the process as many as possible with socket connections. By leveraging this, you can bruteforce stack canary and return address.

After that, you need to leak the address of `libc` library.

Finally, you can supply ROP gadgets and get the flag.
