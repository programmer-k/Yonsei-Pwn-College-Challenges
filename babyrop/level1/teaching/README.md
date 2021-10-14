In this challenge, you should use `ROP`, which is return oriented programming.

The challenge describes all the information we need and what we have to do.
In a nutshell, there is a function called `win` that we have to call to get the flag.
It is located at `0x401d06`.

The return address is stored at `0x7ffc76a46768`, which is 88 bytes after the start of your input buffer.
Thus, we should generate 88 bytes of meaningless data followed by the address of the function.

Running the `run.py` will generate the payload for you.
To give a little bit of information, `<` means little endian and `Q` means 8 bytes of unsigned long long integer.

After that, all you need is to run the challenge with the payload.
```
/babyrop_level1_teaching1 < payload
```
