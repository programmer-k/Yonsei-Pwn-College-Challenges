In this challenge, `stat` function changed to `lstat` function.

Therefore, we need a workaround. Specifically, I will use `path/challenges/f` as a command-line argument.

To evade the first check, use the following commands.
```
mkdir -p path/challenges
touch path/challenges/f
```

This will evade the first check for the following reasons.
1. The path does not contain `flag`.
2. We can get file information as it exists.
3. It is not a symlink.

To evade the second check, use the following commands.
```
rm -rf path
ln -s / path
```

I will explain how this is going to work.

As always, `dirname` will return a string `"path/challenges"` and `lstat("path/challenges", ...)` will be invoked.

The key point is that the property of the `lstat` function that does not follow the symlink is only applicable on the file that it tries to investigate.

Therefore, if `challenges` is a symlink, it will investigate the symlink itself.

On the other hand, if `path` is a symlink, it will follow the symlink since `path` is not an interest for `lstat` function.

Coming back to the challenge, `lstat("path/challenges", ...)` is thus equivalent to `lstat("/challenges", ...)`.

As `/challenges` exists and has the equivalent permission as top-level directory, this approach would work.

`/challenges` is not the only option. Instead, you can use other directories in the top-level directory.

Finally, we can get the flag by applying a symlink to the `/flag` file with the following commands.
```
rm -rf path
mkdir -p path/challenges
ln -s /flag path/challenges/f
```
