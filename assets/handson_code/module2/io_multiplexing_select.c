/*
 * PCCST501 Computer Networks - Module 2 Hands-on
 * I/O Multiplexing TCP Server using select()
 * References: W. Richard Stevens, UNIX Network Programming Vol 1 (Chapter 6)
 * Handles multiple simultaneous client connections without multi-threading/forking.
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
#include <sys/select.h>
#include <errno.h>

#define PORT 8080
#define MAX_CLIENTS 30
#define BUFFER_SIZE 1024

int main() {
    int server_fd, client_sockets[MAX_CLIENTS], max_sd, activity, i, valread, sd;
    int new_socket;
    struct sockaddr_in address;
    char buffer[BUFFER_SIZE];
    fd_set readfds;

    // Initialize all client socket descriptors to 0
    for (i = 0; i < MAX_CLIENTS; i++) {
        client_sockets[i] = 0;
    }

    // Create Master TCP socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("[-] Socket creation failed");
        exit(EXIT_FAILURE);
    }

    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, (char *)&opt, sizeof(opt));

    // Bind configuration
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("[-] Bind failed");
        exit(EXIT_FAILURE);
    }
    printf("[+] Master Socket bound to port %d\n", PORT);

    if (listen(server_fd, 10) < 0) {
        perror("[-] Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("[*] select() Multiplexed Server waiting for connections...\n");

    int addrlen = sizeof(address);

    while (1) {
        // Clear socket set
        FD_ZERO(&readfds);

        // Add master socket to set
        FD_SET(server_fd, &readfds);
        max_sd = server_fd;

        // Add active child sockets to set
        for (i = 0; i < MAX_CLIENTS; i++) {
            sd = client_sockets[i];
            if (sd > 0)
                FD_SET(sd, &readfds);
            if (sd > max_sd)
                max_sd = sd;
        }

        // Wait for an activity on one of the sockets (timeout is NULL = wait indefinitely)
        activity = select(max_sd + 1, &readfds, NULL, NULL, NULL);

        if ((activity < 0) && (errno != EINTR)) {
            printf("[-] select error\n");
        }

        // Check if activity is on Master socket -> Incoming new connection
        if (FD_ISSET(server_fd, &readfds)) {
            if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) {
                perror("[-] accept error");
                exit(EXIT_FAILURE);
            }

            printf("[+] New connection: socket_fd=%d, ip=%s, port=%d\n",
                   new_socket, inet_ntoa(address.sin_addr), ntohs(address.sin_port));

            // Send welcome greeting
            char *welcome_msg = "Welcome to PCCST501 Stevens select() Multiplexed Echo Server!\r\n";
            send(new_socket, welcome_msg, strlen(welcome_msg), 0);

            // Add new socket to array
            for (i = 0; i < MAX_CLIENTS; i++) {
                if (client_sockets[i] == 0) {
                    client_sockets[i] = new_socket;
                    printf("[*] Registered socket in slot index %d\n", i);
                    break;
                }
            }
        }

        // Else activity is I/O operation on some client socket
        for (i = 0; i < MAX_CLIENTS; i++) {
            sd = client_sockets[i];
            if (FD_ISSET(sd, &readfds)) {
                // Check if it was for closing, and also read the incoming message
                if ((valread = read(sd, buffer, BUFFER_SIZE - 1)) == 0) {
                    // Client disconnected
                    getpeername(sd, (struct sockaddr *)&address, (socklen_t *)&addrlen);
                    printf("[-] Host disconnected: ip=%s, port=%d (fd=%d)\n",
                           inet_ntoa(address.sin_addr), ntohs(address.sin_port), sd);
                    close(sd);
                    client_sockets[i] = 0;
                } else {
                    // Echo back message
                    buffer[valread] = '\0';
                    printf("[Slot %d - fd %d]: %s", i, sd, buffer);
                    send(sd, buffer, valread, 0);
                }
            }
        }
    }

    return 0;
}
