import csv
import argparse

def leer_registros(filename, severidad):
    registros = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Severidad'] == severidad:
                registros.append(row)
    return registros

def main():
    parser = argparse.ArgumentParser(description="Analizar el log de medidores por severidad.")
    parser.add_argument('severidad', type=str, choices=['WARN', 'INFO', 'ERROR'], help='Nivel de severidad a analizar')
    args = parser.parse_args()

    registros = leer_registros('Log_de_medidores.csv', args.severidad)

    if not registros:
        print(f"No se encontraron registros con severidad {args.severidad}.")
        return

    index = 0
    while True:
        print(f"Fecha-hora: {registros[index]['Fecha-hora']}, Evento: {registros[index]['Evento']}, Severidad: {registros[index]['Severidad']}, Descripción: {registros[index]['Descripción']}")
        
        user_input = input("Ingrese 's' para la siguiente línea o 'p' para parar: ").strip().lower()
        if user_input == 'p':
            print("Fin del programa.")
            break
        elif user_input == 's':
            index += 1
            if index >= len(registros):
                print("No hay más registros con esta severidad.")
                break
        else:
            print("Comando no reconocido. Intente de nuevo.")

if __name__ == '__main__':
    main()
