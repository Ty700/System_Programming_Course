#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>

int main()
{
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1){
        perror("Error: Socket");
        exit(EXIT_FAILURE);
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    addr.sin_port = htons(8080);

    int bind_result = bind(server_fd, (struct sockaddr *)&addr, sizeof(addr));

    if (bind_result == -1){
        perror("Error: Bind");
        exit(EXIT_FAILURE);
    }

    int listen_result = listen(server_fd, 1);
    if (listen_result == -1){
        perror("Error: Listen");
        exit(EXIT_FAILURE);
    }

    int addrlen = sizeof(addr);

    printf("Waiting for client to connect\n");

    int client_fd = accept(server_fd, (struct sockaddr *)&addr, &addrlen);
    if (client_fd == -1){
        perror("Error: Accept");
        exit(EXIT_FAILURE);
    }

    printf("Connected to client\n");

    while(1){
        char clientResponse[1024] = {0};

        read(client_fd, clientResponse, sizeof(clientResponse) - 1);
        printf("server received: %s\n", clientResponse);
        
        char serverResonse[1024] = {0};

        if(strncmp(clientResponse, "exit", 4) == 0){
            printf("Closing Connection\n");
            strcpy(serverResonse, "exit");
            send(client_fd, serverResonse, strlen(serverResonse), 0);
            printf("Responding with: %s\n", serverResonse);
            close(server_fd);
            close(client_fd);
            break;
        } else if(strncmp(clientResponse, "hello", 5) == 0){
            strcpy(serverResonse, "world");     
        } else {
            strcpy(serverResonse, "Not programmed to do anything :)\n");
        }
        send(client_fd, serverResonse, strlen(serverResonse), 0);
        printf("Responding with: %s\n", serverResonse);  
    }

    return 0;
}