import os
import zipfile
import csv
import argparse

def descomprimir_zip(nombre_zip, directorio_salida):
    """Descomprimir el archivo ZIP en el directorio de salida."""
    with zipfile.ZipFile(nombre_zip, 'r') as zip_ref:
        zip_ref.extractall(directorio_salida)

def contar_matches(codigo_alumno, nombre_archivo_csv):
    """Contar las veces que el código de alumno hace match de forma horizontal en el archivo CSV."""
    matches = 0
    with open(nombre_archivo_csv, mode='r') as file:
        reader = csv.reader(file)
        for fila in reader:
            linea = ''.join(fila)
            if codigo_alumno in linea:
                matches += 1
    return matches

def main():
    parser = argparse.ArgumentParser(description="Contar los matches de un código de alumno en archivos CSV.")
    parser.add_argument('codigo_alumno', type=str, help='El código de alumno a buscar en los archivos CSV')
    args = parser.parse_args()
    codigo_alumno = args.codigo_alumno

    # Descomprimir los archivos CSV
    nombre_zip = 'archivos_csv.zip'  # Ajusta esto según el nombre del archivo ZIP
    directorio_salida = 'archivos_csv'
    descomprimir_zip(nombre_zip, directorio_salida)

    # Contar los matches en cada archivo CSV
    for archivo_csv in os.listdir(directorio_salida):
        if archivo_csv.endswith('.csv'):
            path_csv = os.path.join(directorio_salida, archivo_csv)
            matches = contar_matches(codigo_alumno, path_csv)
            print(f"Archivo {archivo_csv}: {matches} coincidencias.")

if __name__ == '__main__':
    main()
