import socket 
def read_ip_and_port():
    ip = input("Ingresar IP (default: 127.0.0.1): ") or "127.0.0.1"
    port = input("Ingresar puerto (default: 8080): ") or "8080"
    return ip, port

def read_message():
    while True:
        message = input("Ingresar mensaje(max 200 caracteres): ")
        if len(message) <= 200:
            break
        else:
            print("El mensaje es muy largo")
    
    disconnect = (message == "desconectar")
    return message, disconnect

def create_and_connect_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    entered_ip, entered_port = read_ip_and_port()
    sock.connect((entered_ip, int(entered_port)))
    return sock

try:
    sock = create_and_connect_socket()
    print("Conexion exitosa")
    while True:
        entered_message, is_disconnect = read_message()
        sock.send(entered_message.encode())
        received = sock.recv(200).decode()
        print("Recibido:", received)
        if(is_disconnect): break
except Exception as e:
    print(e)
finally:
    sock.close()
    print("Conexion cerrada")
#Pablo Arias, Carlos Cespedes, Carolina Escalona, Diego Poblete