#include <fcntl.h>
#include <unistd.h>

int main(void)
{
    char * buf = "aaaaaaiqtgjvamgoxp";
    int fd = open("ozvov", O_WRONLY);
    write(fd, buf, 18);
    close(fd);
    return 0;
}