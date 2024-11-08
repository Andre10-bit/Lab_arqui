import sys

# Abre el archivo en modo de escritura
with open("output_parte2b.txt", "w") as f:
    # Leer líneas desde la entrada estándar
    for line in sys.stdin:
        # Escribir cada línea en el archivo
        f.write(line)
