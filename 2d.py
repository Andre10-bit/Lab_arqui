import sys
import argparse

def main():
    # Configurar argparse para manejar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Leer archivo de entrada y escribir a archivo de salida.")
    parser.add_argument('input_file', type=str, help='Nombre del archivo de entrada')
    parser.add_argument('output_file', type=str, help='Nombre del archivo de salida')
    args = parser.parse_args()

    # Leer el contenido del archivo de entrada
    try:
        with open(args.input_file, 'r') as infile:
            contenido = infile.read()
    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{args.input_file}' no existe.")
        sys.exit(1)

    # Escribir el contenido al archivo de salida
    with open(args.output_file, 'w') as outfile:
        outfile.write(contenido)

    print(f"El contenido del archivo '{args.input_file}' se ha copiado a '{args.output_file}'.")

if __name__ == '__main__':
    main()
