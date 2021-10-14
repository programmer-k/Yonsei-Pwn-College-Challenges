In this challenge, you are only allowed to use a shellcode of `0xc` bytes.
Thus, we have to shrink the previous shellcode.

The key idea of this problem is a symlink.
What I found is that changing the permission of a symlink actually changes the permission of a real file.
Thus, we can use a symlink with a short name.

Use the following command to create one.
```
ln -s /flag f
```

Then, compile the shellcode and run the challenge.
