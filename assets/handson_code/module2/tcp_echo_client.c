/*
 * PCCST501 Computer Networks - Module 2 Hands-on
 * Elementary TCP Echo Client (UNIX / Linux Socket API)
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

#define SERVER_IP "127.0.0.1"
#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sock_fd;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;

    // 1. Create TCP Socket
    if ((sock_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("[-] Socket creation failed");
        exit(EXIT_FAILURE);
    }
    printf("[+] Socket created (fd = %d)\n", sock_fd);

    // 2. Specify Server Address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    if (inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) <= 0) {
        perror("[-] Invalid IP address");
        close(sock_fd);
        exit(EXIT_FAILURE);
    }

    // 3. Connect to Server (Initiates TCP 3-Way Handshake)
    printf("[*] Connecting to TCP server at %s:%d...\n", SERVER_IP, PORT);
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("[-] Connection to server failed");
        close(sock_fd);
        exit(EXIT_FAILURE);
    }
    printf("[+] Connected successfully! Type messages to send (or 'exit' to quit):\n");

    // 4. Interactive send/recv loop
    while (1) {
        printf("\n> ");
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) break;
        
        if (strncmp(buffer, "exit", 4) == 0) {
            printf("[*] Closing connection...\n");
            break;
        }

        // Send to server
        write(sock_fd, buffer, strlen(buffer));

        // Read echo back
        bytes_read = read(sock_fd, buffer, sizeof(buffer) - 1);
        if (bytes_read > 0) {
            buffer[bytes_read] = '\0';
            printf("[Server Echo]: %s", buffer);
        } else {
            printf("[-] Server closed the connection.\n");
            break;
        }
    }

    // 5. Close socket
    close(sock_fd);
    return 0;
}
