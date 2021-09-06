#include <fcntl.h>
#include <unistd.h>

int main(void)
{
    char * buf = "bbbbbbatijvbqhk";
    int fd = open("llgwv", O_WRONLY);
    write(fd, buf, 15);
    close(fd);
    return 0;
}