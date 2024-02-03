import socket
import threading
import json

def handle_client(client_socket, remote_host, remote_port):
    print(f'[+] Conexão iniciada para {remote_host}:{remote_port}')

    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    data_exchange = {'client_to_server': [], 'server_to_client': []}

    while True:
        client_data = client_socket.recv(4096)
        if not client_data:
            break
        remote_socket.sendall(client_data)
        data_exchange['client_to_server'].append(client_data.decode('utf-8'))

    while True:
        remote_data = remote_socket.recv(4096)
        if not remote_data:
            break
        client_socket.sendall(remote_data)
        data_exchange['server_to_client'].append(remote_data.decode('utf-8'))

    with open('data/data_exchange.json', 'w') as json_file:
        json.dump(data_exchange, json_file, indent=4)

    client_socket.close()
    remote_socket.close()
    print(f'[+] Conexão encerrada para {remote_host}:{remote_port}')

def start_proxy(bind_host, bind_port, remote_host, remote_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_host, bind_port))
    server.listen(5)

    print(f'[+] Proxy escutando em {bind_host}:{bind_port}')

    while True:
        client_socket, addr = server.accept()
        print(f'[+] Conexão recebida de {addr[0]}:{addr[1]}')
        proxy_thread = threading.Thread(target=handle_client, args=(client_socket, remote_host, remote_port))
        proxy_thread.start()

if __name__ == '__main__':
    BIND_HOST = '127.0.0.1'
    BIND_PORT = 8080
    REMOTE_HOST = 'destino.com'
    REMOTE_PORT = 80

    start_proxy(BIND_HOST, BIND_PORT, REMOTE_HOST, REMOTE_PORT)

# Execute: python3 -m http.server 8080
# No terminal, isso cria um servidor com a porta "http://127.0.0.1:8080/"
# Acessando pelo navegador conseguirá navegar nesse diretório