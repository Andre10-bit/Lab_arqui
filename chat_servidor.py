import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando el servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)
    sock.listen(1)

    print("Esperando conexiones...")
    conn, client_address = sock.accept()
    print(f"Conexión desde {client_address[0]}:{client_address[1]}")

    try:
        while True:
            # Turno del servidor
            mensaje_servidor = input("Servidor > ")
            conn.sendall(mensaje_servidor.encode('utf-8'))
            if mensaje_servidor.lower() == "salir":
                break

            # Turno del cliente
            data = conn.recv(SOCK_BUFFER).decode('utf-8')
            print(f"Cliente > {data}")
            if data.lower() == "salir":
                break
    finally:
        conn.close()
        sock.close()
        print("Conexión cerrada")
