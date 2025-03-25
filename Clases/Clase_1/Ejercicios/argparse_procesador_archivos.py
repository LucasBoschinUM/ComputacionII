import argparse
import os

def configurar_argumentos():
    parser = argparse.ArgumentParser(
        description='Script de ejemplo para manejar tipos específicos y argumentos múltiples.'
    )
    
    # Argumentos obligatorios para archivos
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Nombre del archivo de entrada'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Nombre del archivo de salida'
    )
    
    # Argumento obligatorio que espera un número entero
    parser.add_argument(
        '-n', '--number',
        type=int,
        required=True,
        help='Un número entero'
    )
    
    # Argumento opcional que acepta uno o más elementos (lista de strings)
    parser.add_argument(
        '--items',
        nargs='+',
        type=str,
        help='Lista de elementos (uno o más)'
    )
    
    return parser.parse_args()

def verificar_archivo(archivo):
    if not os.path.exists(archivo):
        print(f"Error: El archivo de entrada '{archivo}' no existe.")
        exit(1)

def leer_y_procesar(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    # Transformación: convertir el contenido a mayúsculas
    contenido_transformado = contenido.upper()
    return contenido_transformado

def escribir_archivo(archivo, contenido):
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    print(f"El contenido procesado se ha guardado en '{archivo}'.")

def main():
    # Configurar y obtener argumentos
    args = configurar_argumentos()
    
    # Verificar la existencia del archivo de entrada
    verificar_archivo(args.input)
    
    # Leer y procesar el archivo
    contenido_procesado = leer_y_procesar(args.input)
    print("Se ha leído y procesado el archivo de entrada.")
    
    # Escribir el contenido procesado en el archivo de salida
    escribir_archivo(args.output, contenido_procesado)
    
    # Mostrar el número entero recibido
    print(f"El número entero recibido es: {args.number}")
    
    # Mostrar la lista de elementos si se proporcionó
    if args.items:
        print("Lista de elementos recibida:")
        for item in args.items:
            print(f"- {item}")

if __name__ == "__main__":
    main()