import socket
import csv
import numpy as np

def cargar_datos(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def promedio_ventas(data, tipo_producto):
    ventas = [float(row['TotalSalesAmount']) for row in data if row['ProductType'] == tipo_producto]
    promedio = np.mean(ventas) if ventas else 0
    return f"El promedio de ventas de {tipo_producto} es {promedio:.2f}."

def mejor_canal_venta(data):
    canales = {}
    for row in data:
        canal = row['ChannelSales']
        total_ventas = float(row['TotalSalesAmount'])
        if canal in canales:
            canales[canal]['ventas'] += total_ventas
            canales[canal]['cantidad'] += 1
        else:
            canales[canal] = {'ventas': total_ventas, 'cantidad': 1}
    mejor_canal = max(canales.items(), key=lambda x: x[1]['ventas'])
    return f"El mejor canal de venta fue {mejor_canal[0]} con {mejor_canal[1]['cantidad']} ventas y con un total de {mejor_canal[1]['ventas']:.2f} soles."

def desviacion_estandar(data, tipo_producto):
    ventas = [float(row['TotalSalesAmount']) for row in data if row['ProductType'] == tipo_producto]
    desviacion = np.std(ventas) if ventas else 0
    return f"La desviación estándar de {tipo_producto} es {desviacion:.2f}."

def clientes_superiores_al_promedio(data):
    ventas = [float(row['TotalSalesAmount']) for row in data]
    promedio = np.mean(ventas) if ventas else 0
    clientes = [row['ClientName'] for row in data if float(row['TotalSalesAmount']) > promedio]
    return f"Los clientes con ventas superiores al promedio son: {len(clientes)}."

def distribucion_ventas(data, tipo_producto):
    ventas = [float(row['TotalSalesAmount']) for row in data if row['ProductType'] == tipo_producto]
    if not ventas:
        return f"No hay datos de ventas para {tipo_producto}."
    media = np.mean(ventas)
    mediana = np.median(ventas)
    minimo = np.min(ventas)
    maximo = np.max(ventas)
    return f"Distribución de ventas de {tipo_producto}: media {media:.2f}, mediana {mediana:.2f}, mínimo {minimo:.2f}, máximo {maximo:.2f}."

HOST = 'localhost'
PORT = 5000

data = cargar_datos('orders_data_large.csv')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Servidor en espera de conexiones...')
    conn, addr = s.accept()
    consultas_realizadas = []
    with conn:
        print('Conectado por', addr)
        while True:
            consulta = conn.recv(1024).decode('utf-8')
            if not consulta or consulta.lower() == 'salir':
                break
            consultas_realizadas.append(consulta)
            if 'promedio de ventas de' in consulta:
                tipo_producto = consulta.split('de')[-1].strip()
                respuesta = promedio_ventas(data, tipo_producto)
            elif consulta == 'mejor canal de venta':
                respuesta = mejor_canal_venta(data)
            elif 'desviación estándar de ventas de' in consulta:
                tipo_producto = consulta.split('de')[-1].strip()
                respuesta = desviacion_estandar(data, tipo_producto)
            elif consulta == 'cantidad de clientes con ventas superiores al promedio':
                respuesta = clientes_superiores_al_promedio(data)
            elif 'distribución de ventas de' in consulta:
                tipo_producto = consulta.split('de')[-1].strip()
                respuesta = distribucion_ventas(data, tipo_producto)
            else:
                respuesta = 'Consulta no reconocida.'
            conn.sendall(respuesta.encode('utf-8'))

with open('reporte.txt', 'w') as file:
    file.write('Reporte de consultas realizadas\n')
    file.write('='*50 + '\n')
    for consulta in consultas_realizadas:
        file.write(f'{consulta}\n')
