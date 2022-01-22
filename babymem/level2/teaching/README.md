Now, the problem moves to the heap memory.

Again, I do not know the details but the challenge says as follows.

```
The "win" variable is stored at 0x561f29b1dc20, 432 bytes after the start of your input buffer.
```

I tried 432 bytes payload but did not work.
Then, I tried 864 bytes and 436 bytes payloads, and both of them worked.

I think 432 bytes payload writes just before the win variable, so we need another 4 bytes.