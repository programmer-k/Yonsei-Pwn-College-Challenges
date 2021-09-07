#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int sock = socket(AF_UNIX, SOCK_STREAM, 0);
    //printf("%d %d", AF_UNIX, SOCK_STREAM);

    struct sockaddr_un addr;
    unsigned int addr_len = sizeof(addr);

    memset(&addr, 0, sizeof(addr));
    addr.sun_family = AF_UNIX;
    snprintf(addr.sun_path, sizeof(addr.sun_path), "%s", "opiou");

    if (connect(sock, (struct sockaddr *) &addr, addr_len))
        printf("Connection Failure!");
    
    char * str = "aaabbbcccdddcdeeeoqwxyzz";
    write(sock, str, strlen(str));
    
    close(sock);
    return 0;
}