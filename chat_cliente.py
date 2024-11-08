import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5000)

    print(f"Conectando al servidor en {server_address[0]}:{server_address[1]}")
    sock.connect(server_address)

    try:
        while True:
            # Esperar mensaje del servidor
            data = sock.recv(SOCK_BUFFER).decode('utf-8')
            print(f"Servidor > {data}")
            if data.lower() == "salir":
                break

            # Enviar mensaje del cliente
            mensaje_cliente = input("Cliente > ")
            sock.sendall(mensaje_cliente.encode('utf-8'))
            if mensaje_cliente.lower() == "salir":
                break
    finally:
        sock.close()
        print("Conexión cerrada")
