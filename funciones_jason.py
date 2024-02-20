import json

with open('anime.json') as f:
    data = json.load(f)

# Función para listar títulos, géneros y estudios de anime
def listar_animes():
    for anime in data:
        print("Título:", anime['titulo'])
        print("Géneros:", ', '.join(anime['generos']))
        print("Estudio:", anime['estudio'])
        print("----------------------")

# Función para contar el total de animes disponibles
def contar_animes():
    return len(data)

# Función para buscar animes por género
def buscar_por_genero(genero):
    for anime in data:
        if genero in anime['generos']:
            print("Título:", anime['titulo'])

# Función para buscar animes por estudio
def buscar_por_estudio(estudio):
    for anime in data:
        if anime['estudio'] == estudio:
            print("Título:", anime['titulo'])
            print("Géneros:", ', '.join(anime['generos']))

# Función para buscar animes por rango de años
def buscar_por_rango_de_años(año_inicio, año_fin):
    for anime in data:
        año_emision = anime['año_emision']
        if año_emision >= año_inicio and año_emision <= año_fin:
            print("Título:", anime['titulo'])
            print("Géneros:", ', '.join(anime['generos']))
