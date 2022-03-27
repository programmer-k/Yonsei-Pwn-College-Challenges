#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
        char * buffer = "jsnxzigipkngxzvx";
        int fd = open("/proc/pwncollege", O_WRONLY);
        write(fd, buffer, strlen(buffer));
        return 0;
}
