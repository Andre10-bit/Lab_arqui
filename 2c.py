import sys
import argparse

def main():
    # Configurar argparse para manejar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Procesar entrada y escribir a un archivo o stdout.")
    parser.add_argument('-o', '--output', type=str, help='Nombre del archivo de salida (opcional)')
    args = parser.parse_args()

    # Determinar si escribir a un archivo o a stdout
    if args.output:
        with open(args.output, "w") as f:
            for line in sys.stdin:
                f.write(line)
    else:
        for line in sys.stdin:
            sys.stdout.write(line)

if __name__ == '__main__':
    main()
