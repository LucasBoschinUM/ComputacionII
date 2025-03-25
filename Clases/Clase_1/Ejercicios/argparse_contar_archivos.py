import argparse
import os

def configurar_argumentos():
    parser = argparse.ArgumentParser(
        description='Script para leer un archivo, transformar su contenido y guardar el resultado en otro archivo.'
    )
    
    # Definir el argumento de entrada (obligatorio)
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Nombre del archivo de entrada'
    )
    
    # Definir el argumento de salida (obligatorio)
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Nombre del archivo de salida'
    )
    
    return parser.parse_args()

def verificar_archivo(archivo):
    if not os.path.exists(archivo):
        print(f"Error: El archivo de entrada '{archivo}' no existe.")
        exit(1)  # Sale del script con error

def leer_y_procesar(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    # Transformación: convertir a mayúsculas
    contenido_transformado = contenido.upper()
    return contenido_transformado

def escribir_archivo(archivo, contenido):
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    print(f"El contenido procesado se ha guardado en '{archivo}'.")

def main():
    # Configurar y obtener los argumentos
    args = configurar_argumentos()
    
    # Verificar que el archivo de entrada existe
    verificar_archivo(args.input)
    
    # Leer y procesar el archivo
    contenido_procesado = leer_y_procesar(args.input)
    print("Se ha leído y procesado el archivo de entrada.")
    
    # Escribir el contenido procesado en el archivo de salida
    escribir_archivo(args.output, contenido_procesado)

if __name__ == "__main__":
    main()