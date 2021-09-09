This program uses the function `chroot` to jail the user.
However, `chroot` does not change the current working directory.
Thus, the following command will fail, whereas the next command will succeed.
```
/babyjail_level1_teaching1 /flag    # Fail
```

```
/babyjail_level1_teaching1 ./flag
```