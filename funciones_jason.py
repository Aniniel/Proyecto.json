import json

# Cargar datos del archivo JSON
with open(r'C:\Users\Dani\Desktop\1-ASIR\LENGUAJE\jason\animes.json', encoding='utf-8') as f:
    data = json.load(f)

# Función para listar títulos, géneros y estudios de anime
def listar_animes():
    for anime in data:
        print("Título:", anime['title']['text'])
        print("Géneros:", ', '.join(anime['genres']))
        print("----------------------")

# Función para contar el total de animes disponibles
def contar_animes():
    return len(data)

# Función para buscar animes por género
def buscar_por_genero(data):
    genero = input("\nIngrese un género de anime: ")
    encontrados = False
    for anime in data:
        if genero in anime['genres']:
            print("Título:", anime['title']['text'])
            print("Géneros:", ', '.join(anime['genres']))
            encontrados = True
    if not encontrados:
        print("No se encontraron animes con este género.")

# Función para buscar animes por estudio
def buscar_por_estudio(data):
    estudio = input("\nIngrese un estudio de anime: ")
    animes_encontrados = False
    for anime in data:
        if anime['studio'] == estudio:
            print("Título:", anime['title']['text'])
            print("Géneros:", ', '.join(anime['genres']))
            animes_encontrados = True
    if not animes_encontrados:
        print("No se encontraron animes del estudio especificado.")

# Función para buscar animes por rango de años
def buscar_por_rango_de_años(año_inicio, año_fin):
    año_inicio = int(input("\nIngrese el año de inicio: "))
    año_fin = int(input("Ingrese el año de fin: "))
    animes_encontrados = False
    for anime in data:
        año_emision = int(anime['start_date'].split(',')[1].strip())
        if año_emision >= año_inicio and año_emision <= año_fin:
            print("Título:", anime['title']['text'])
            print("Géneros:", ', '.join(anime['genres']))
            animes_encontrados = True
    if not animes_encontrados:
        print("No se encontraron animes para ese rango de años.")

# Función del menú
def menu():
    while True:
        print("\nBienvenido al Menú de Gestión de Anime:")
        print("-----------------------------------------")
        print("1. Listar información de anime")
        print("2. Contar el total de animes disponibles")
        print("3. Buscar animes por género")
        print("4. Buscar animes por estudio")
        print("5. Buscar animes por rango de años")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nListar información de anime:",listar_animes())   
        elif opcion == "2":
            print("\nTotal de animes disponibles:", contar_animes())
        elif opcion == "3":
            print("\nBuscar animes por género:")
            buscar_por_genero(data)
        elif opcion == "4":
            print("\nBuscar animes por estudio:",)
            buscar_por_estudio(data)
        elif opcion == "5":
            print("\nBuscar animes por rango de años:",buscar_por_rango_de_años())
            
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

# Ejecutar el menú
menu()
