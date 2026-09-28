/*
 * PCCST501 Computer Networks - Module 2 Hands-on
 * Elementary TCP Echo Server (UNIX / Linux Socket API)
 * References: W. Richard Stevens, UNIX Network Programming Vol 1 (Chapters 3-6)
 * Author: Prof. Anju Markose | Dept. of CSE, VJCET
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024
#define BACKLOG 5

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_len = sizeof(client_addr);
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;

    // 1. Create socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("[-] Socket creation failed");
        exit(EXIT_FAILURE);
    }
    printf("[+] TCP Socket created successfully (socket fd = %d)\n", server_fd);

    // Enable SO_REUSEADDR to prevent "Address already in use" errors
    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    // 2. Prepare sockaddr_in structure
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Bind to all interfaces
    server_addr.sin_port = htons(PORT);       // Host to Network Short

    // 3. Bind socket to IP and Port
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("[-] Bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }
    printf("[+] Socket bound to 0.0.0.0:%d\n", PORT);

    // 4. Listen for incoming client connections
    if (listen(server_fd, BACKLOG) < 0) {
        perror("[-] Listen failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }
    printf("[*] TCP Server listening on port %d (Backlog queue: %d)...\n", PORT, BACKLOG);

    // 5. Accept and service client connection
    while (1) {
        printf("[*] Waiting for incoming TCP connection...\n");
        client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &addr_len);
        if (client_fd < 0) {
            perror("[-] Accept failed");
            continue;
        }

        char client_ip[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &client_addr.sin_addr, client_ip, sizeof(client_ip));
        printf("[+] Connection accepted from %s:%d (Client fd: %d)\n",
               client_ip, ntohs(client_addr.sin_port), client_fd);

        // Echo loop
        while ((bytes_read = read(client_fd, buffer, sizeof(buffer) - 1)) > 0) {
            buffer[bytes_read] = '\0';
            printf("[Recv from %s]: %s", client_ip, buffer);
            
            // Send back the echoed data
            write(client_fd, buffer, bytes_read);
        }

        if (bytes_read == 0) {
            printf("[-] Client %s disconnected.\n", client_ip);
        } else if (bytes_read < 0) {
            perror("[-] Read error");
        }

        close(client_fd);
    }

    close(server_fd);
    return 0;
}
