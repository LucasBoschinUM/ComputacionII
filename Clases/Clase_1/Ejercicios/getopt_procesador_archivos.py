import sys
import getopt
import os

def mostrar_ayuda():
    print("""
Uso: python script_getopt.py -i <archivo_entrada> -o <archivo_salida> -n <numero> [--items item1 item2 ...]

Opciones:
  -i, --input     Archivo de entrada (obligatorio)
  -o, --output    Archivo de salida (obligatorio)
  -n, --number    Un número entero obligatorio
  --items         Lista opcional de elementos
  -h, --help      Muestra esta ayuda
""")
    sys.exit(0)

def main():
    # Valores por defecto
    archivo_entrada = None
    archivo_salida = None
    numero = None
    items = []

    # Definir opciones cortas y largas
    opciones_cortas = "hi:o:n:"
    opciones_largas = ["help", "input=", "output=", "number=", "items="]

    try:
        # Extraer argumentos
        opts, args = getopt.getopt(sys.argv[1:], opciones_cortas, opciones_largas)
    except getopt.GetoptError as err:
        print(f"Error en los argumentos: {err}")
        mostrar_ayuda()

    # Procesar los argumentos
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            mostrar_ayuda()
        elif opt in ("-i", "--input"):
            archivo_entrada = arg
        elif opt in ("-o", "--output"):
            archivo_salida = arg
        elif opt in ("-n", "--number"):
            try:
                numero = int(arg)
            except ValueError:
                print("Error: El argumento de --number debe ser un número entero.")
                sys.exit(1)
        elif opt == "--items":
            items = args  # Captura el resto de los argumentos como lista

    # Verificar que los argumentos obligatorios están presentes
    if not archivo_entrada or not archivo_salida or numero is None:
        print("Error: Faltan argumentos obligatorios.")
        mostrar_ayuda()

    # Verificar si el archivo de entrada existe
    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo de entrada '{archivo_entrada}' no existe.")
        sys.exit(1)

    # Leer el archivo y procesarlo
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        contenido = f.read().upper()  # Convertir a mayúsculas

    # Escribir en el archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(contenido)

    print(f"✅ Archivo procesado y guardado en '{archivo_salida}'.")
    print(f"✅ Número recibido: {numero}")

    # Mostrar los elementos si se pasaron
    if items:
        print("✅ Lista de elementos recibida:")
        for item in items:
            print(f" - {item}")

if __name__ == "__main__":
    main()
