import socket

HOST = 'localhost'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Conectado al servidor. Puede hacer consultas o escribir "salir" para terminar.')
    while True:
        consulta = input('Ingrese su consulta: ')
        s.sendall(consulta.encode('utf-8'))
        if consulta.lower() == 'salir':
            break
        respuesta = s.recv(1024).decode('utf-8')
        print('Respuesta del servidor:', respuesta)
