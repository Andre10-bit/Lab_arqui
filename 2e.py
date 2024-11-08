import sys
import argparse

def main():
    # Configurar argparse para manejar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Leer archivo de entrada y escribir a archivo de salida en bloques de tamaño variable.")
    parser.add_argument('input_file', type=str, help='Nombre del archivo de entrada')
    parser.add_argument('output_file', type=str, help='Nombre del archivo de salida')
    parser.add_argument('block_size', type=int, help='Tamaño del bloque en bytes')
    args = parser.parse_args()

    # Leer el archivo de entrada en bloques y escribir en el archivo de salida
    try:
        with open(args.input_file, 'rb') as infile, open(args.output_file, 'wb') as outfile:
            while True:
                # Leer un bloque de datos del archivo de entrada
                bloque = infile.read(args.block_size)
                if not bloque:
                    break
                # Escribir el bloque de datos en el archivo de salida
                outfile.write(bloque)

    except FileNotFoundError:
        print(f"Error: El archivo '{args.input_file}' no existe.")
        sys.exit(1)

    print(f"El contenido del archivo '{args.input_file}' se ha copiado a '{args.output_file}' en bloques de {args.block_size} bytes.")

if __name__ == '__main__':
    main()
