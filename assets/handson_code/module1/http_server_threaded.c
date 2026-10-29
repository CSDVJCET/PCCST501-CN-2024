/*
 * PCCST501 Computer Networks - Multi-threaded HTTP Server in C
 * Department of Computer Science & Engineering, VJCET
 * Faculty: Prof. Anju Markose
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/socket.h>
#include <netinet/in.h>

void *client_handler(void *socket_desc) {
    int sock = *(int*)socket_desc;
    free(socket_desc);
    char buffer[1024];
    int read_size = recv(sock, buffer, sizeof(buffer) - 1, 0);
    if (read_size > 0) {
        buffer[read_size] = '\0';
        char response[] = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>VJCET Computer Networks - Prof. Anju Markose</h1>";
        send(sock, response, strlen(response), 0);
    }
    close(sock);
    return NULL;
}

int main(int argc, char *argv[]) {
    int server_fd, client_sock, *new_sock;
    struct sockaddr_in server, client;
    socklen_t c = sizeof(struct sockaddr_in);

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(argc > 1 ? atoi(argv[1]) : 8080);

    bind(server_fd, (struct sockaddr *)&server, sizeof(server));
    listen(server_fd, 5);
    printf("[INFO] HTTP Server listening on port %d...\n", ntohs(server.sin_port));

    while ((client_sock = accept(server_fd, (struct sockaddr *)&client, &c))) {
        pthread_t thread_id;
        new_sock = malloc(sizeof(int));
        *new_sock = client_sock;
        pthread_create(&thread_id, NULL, client_handler, (void*)new_sock);
        pthread_detach(thread_id);
    }
    return 0;
}
