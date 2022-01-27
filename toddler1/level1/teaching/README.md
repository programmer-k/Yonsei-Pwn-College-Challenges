In this challenge, the stack is executable.

Thus, you can write shellcode into the buffer and jump into it.

Use the following commands to make the assembly code `shellcode.s` into binary.

```
gcc -nostdlib -static shellcode.s -o shellcode-elf
objcopy --dump-section .text=shellcode-raw shellcode-elf
```

Then, we have to overwrite the return address to point the input buffer.

The address of the input buffer is `0x00007fffffffe520`.

The payload size should be 112 bytes.

The shellcode is 66 bytes, so we have to add the padding of 38 bytes and the return address to overwrite.

Please refer to the `run.py` for this step.

Finally, concatenating all the inputs that we have generated and sending them to the challenge.

```
(echo "112"; cat shellcode-raw) | /toddler1_level1_teaching1
```