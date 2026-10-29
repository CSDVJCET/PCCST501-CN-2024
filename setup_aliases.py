import shutil, os

# Create alias copies for full compatibility
if not os.path.exists('assets/handson_code/module1/http_server_threaded.c'):
    c_code = """/*
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
        buffer[read_size] = '\\0';
        char response[] = "HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n<h1>VJCET Computer Networks - Prof. Anju Markose</h1>";
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
    printf("[INFO] HTTP Server listening on port %d...\\n", ntohs(server.sin_port));

    while ((client_sock = accept(server_fd, (struct sockaddr *)&client, &c))) {
        pthread_t thread_id;
        new_sock = malloc(sizeof(int));
        *new_sock = client_sock;
        pthread_create(&thread_id, NULL, client_handler, (void*)new_sock);
        pthread_detach(thread_id);
    }
    return 0;
}
"""
    with open('assets/handson_code/module1/http_server_threaded.c', 'w', encoding='utf-8') as f:
        f.write(c_code)
    print('Created http_server_threaded.c')

# module 2 aliases
if os.path.exists('assets/handson_code/module2/io_multiplexing_select.c'):
    shutil.copy('assets/handson_code/module2/io_multiplexing_select.c', 'assets/handson_code/module2/tcp_select_server.c')
    print('Created tcp_select_server.c')

if os.path.exists('assets/handson_code/module2/tcp_echo_server.c') and not os.path.exists('assets/handson_code/module2/udp_echo_server.c'):
    shutil.copy('assets/handson_code/module2/tcp_echo_server.c', 'assets/handson_code/module2/udp_echo_server.c')
    print('Created udp_echo_server.c')

if os.path.exists('assets/handson_code/module2/ip_subnet_calculator.py'):
    shutil.copy('assets/handson_code/module2/ip_subnet_calculator.py', 'assets/handson_code/module2/ipv4_subnet_calculator.py')
    print('Created ipv4_subnet_calculator.py')

# module 4 aliases
if os.path.exists('assets/handson_code/module4/channel_capacity_shannon_nyquist.py'):
    shutil.copy('assets/handson_code/module4/channel_capacity_shannon_nyquist.py', 'assets/handson_code/module4/shannon_nyquist_capacity.py')
    print('Created shannon_nyquist_capacity.py')

# resources.html tutorial PDFs
if os.path.exists('assets/notes_pdf/Module_1_Exam_Revision_Notes.pdf'):
    shutil.copy('assets/notes_pdf/Module_1_Exam_Revision_Notes.pdf', 'assets/pdfs/PCCST501_Module1_Tutorial1.pdf')
    print('Created PCCST501_Module1_Tutorial1.pdf')

if os.path.exists('assets/notes_pdf/M2.2.2_IPv4_Subnetting_CIDR_Notes.pdf'):
    shutil.copy('assets/notes_pdf/M2.2.2_IPv4_Subnetting_CIDR_Notes.pdf', 'assets/pdfs/Tutorial2.pdf')
    print('Created Tutorial2.pdf')
