import socket

def read_ip_and_port():
    ip = input("Ingresar IP (default: 127.0.0.1): ") or "127.0.0.1"
    port = input("Ingresar puerto (default: 8080): ") or "8080"
    return ip, int(port)

def read_message():
    while True:
        message = input("Ingresar mensaje (max 200 caracteres): ")
        if len(message) <= 200:
            break
        else:
            print("El mensaje es muy largo")
    
    disconnect = (message == "desconectar")
    return message, disconnect

def create_and_bind_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    entered_ip, entered_port = read_ip_and_port()
    return sock, entered_ip, entered_port

try:
    sock, ip, port = create_and_bind_socket()
    print("Socket configurado")
    while True:
        entered_message, is_disconnect = read_message()
        sock.sendto(entered_message.encode(), (ip, port))
        received, server_address = sock.recvfrom(200)
        received_message = received.decode()
        print("Recibido:", received_message)
        if is_disconnect:
            break
except Exception as e:
    print(e)
finally:
    sock.close()
    print("Socket cerrado")
#Pablo Arias, Carlos Cespedes, Carolina Escalona, Diego Poblete