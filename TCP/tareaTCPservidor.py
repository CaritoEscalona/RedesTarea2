import socket

def create_and_listen_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    entered_port = input("Ingresa un puerto (default: 8080): ")
    port = int(entered_port) if entered_port else 8080
    sock.bind(("127.0.0.1", port))
    sock.listen(5)
    return sock

sock = create_and_listen_socket()
while True:
    print("Esperando cliente")
    ip,port = sock.accept()
    print('Cliente conectado desde ', port)
    while True:
      data = ip.recv(200).decode()
      print("Mensaje recibido:", data)
      ip.send(data.encode())
      if(data == "desconectar"):
          ip.close()
          print("Cliente desconectado")
          break
#Pablo Arias, Carlos Cespedes, Carolina Escalona, Diego Poblete