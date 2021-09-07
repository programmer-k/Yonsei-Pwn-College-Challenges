#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

int main(void)
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in addr;
    unsigned int addrLen = sizeof(addr);

    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(42334);
    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);

    if (connect(sock, (struct sockaddr *) &addr, addrLen) < 0)
        printf("Connection Failure!\n");
    
    char * str = "aaaabbbbejjkkoqsyy";
    write(sock, str, strlen(str));
    
    close(sock);
    return 0;
}