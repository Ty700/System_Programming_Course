#include <sys/types.h> 
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>

int main()
{
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    if (server_fd == -1){
        perror("socket");
        exit(EXIT_FAILURE);
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));

    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    char *ip_address = "127.0.0.1";

    inet_pton(AF_INET, ip_address, &addr.sin_addr);

    printf("Connecting to server\n");

    int connect_result = connect(server_fd, (struct sockaddr *)&addr, sizeof(addr));

    if (connect_result == -1){
        perror("connect");
        exit(-1);
    }

while(1){
    //Sending msg to server
    char clientMsg[1024] = {0};
    printf("Msg to send: ");
        fgets(clientMsg, sizeof(clientMsg), stdin);

    if(strncmp(clientMsg, "exit", 4) == 0){
        printf("Closing Connection\n");
        send(server_fd, "exit", strlen("exit"), 0);
        close(server_fd);
        break;
    }

    //If msg != "exit" sends msg
    send(server_fd, clientMsg, strlen(clientMsg), 0);

    //Flushes clientMsg buffer. Without this you get past messages in new messages if 
    //past message length > current message lenght
    //Might be a better way to do this (for sure is)
    for(int i = 0; i < strlen(clientMsg); i++){
        clientMsg[i] = '\0';
    }

    //Reading response from server
    char serverResponse[1024] = {0};
    read(server_fd, serverResponse, sizeof(serverResponse) - 1);

    printf("Received: %s\n", serverResponse);

    }
}
