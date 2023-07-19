import socket

def create_and_bind_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    entered_port = input("Ingresa un puerto (default: 8080): ")
    port = int(entered_port) if entered_port else 8080
    sock.bind(("127.0.0.1", port))
    return sock

sock = create_and_bind_socket()
while True:
    print("Esperando mensaje")
    data, client_address = sock.recvfrom(200)
    data = data.decode()
    print("Mensaje recibido:", data, ", desde", client_address)
    sock.sendto(data.encode(), client_address)
    if data == "desconectar":
        print("Un cliente se ha cerrado")
#Pablo Arias, Carlos Cespedes, Carolina Escalona, Diego Poblete