#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
        char * buffer = "qysmnslwzhhmbgcb";
        int fd = open("/proc/pwncollege", O_WRONLY);
        ioctl(fd, 1337, buffer);
        return 0;
}
