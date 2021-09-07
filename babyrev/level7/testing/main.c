#include <unistd.h>
#include <fcntl.h>

int main(void)
{
    int fd;

    for (int i = 0; i < 679; i++)
        fd = open("input", O_RDONLY);

    execve("/babyrev_level7_testing1", NULL, NULL);
    return 0;
}