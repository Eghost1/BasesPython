#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tutorial de Manejo de Archivos en Python
Autor: Diego
Fecha: 18 de junio de 2025
"""

def imprimir_seccion(titulo):
    """Imprime un título de sección con formato para mejor visualización."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# PARTE 1: CONCEPTOS BÁSICOS DE ARCHIVOS
# ============================================================================

imprimir_seccion("INTRODUCCIÓN A ARCHIVOS EN PYTHON")

print("""
Los archivos son fundamentales para almacenar y recuperar datos de forma persistente.
Python ofrece funciones integradas para trabajar con archivos de texto y binarios.

Operaciones básicas con archivos:
- Abrir un archivo con open()
- Leer contenido con read(), readline(), readlines()
- Escribir contenido con write(), writelines()
- Cerrar el archivo con close()

Modos de apertura comunes:
- 'r': Solo lectura (predeterminado)
- 'w': Escritura (sobrescribe el archivo si existe)
- 'a': Anexar (agregar al final del archivo)
- 'r+': Lectura y escritura
- 'b': Modo binario (añadido a otros modos, ej: 'rb', 'wb')
""")

# -----------------------------------------------------------------------------
# 1. ESCRIBIR EN UN ARCHIVO
# -----------------------------------------------------------------------------

imprimir_seccion("1. ESCRIBIR EN UN ARCHIVO")

print("# Escribir un archivo básico de texto:")

# Método 1: Escribir línea por línea
nombre_archivo = "ejemplo_texto.txt"

# Abrir archivo en modo escritura
archivo = open(nombre_archivo, "w")

# Escribir líneas en el archivo
archivo.write("Hola mundo!\n")
archivo.write("Esta es la segunda línea del archivo.\n")
archivo.write("Esta es la tercera línea.\n")

# Cerrar archivo (importante para liberar recursos)
archivo.close()

print(f"Archivo '{nombre_archivo}' creado con éxito.")

# Método 2: Usar contexto 'with' (recomendado, cierra automáticamente)
print("\n# Usando el contexto 'with' (recomendado):")

frases = [
    "Python es un lenguaje de programación versátil.\n",
    "Con Python puedes desarrollar scripts, aplicaciones web, análisis de datos y más.\n",
    "Este archivo fue creado usando el contexto 'with'.\n"
]

with open("ejemplo_with.txt", "w") as archivo:
    archivo.writelines(frases)

print("Archivo 'ejemplo_with.txt' creado con éxito.")

# Método 3: Escribir datos estructurados
print("\n# Escribir datos en formato estructurado (CSV simple):")

# Lista de series de TV para guardar
series_tv = [
    ["The Office", 2005, 2013, 9.0, "Comedia"],
    ["Breaking Bad", 2008, 2013, 9.5, "Drama"],
    ["Game of Thrones", 2011, 2019, 9.2, "Fantasía"],
    ["Friends", 1994, 2004, 8.9, "Comedia"],
    ["Stranger Things", 2016, 2025, 8.6, "Ciencia ficción"]
]

# Guardar en formato CSV (valores separados por comas)
with open("series_tv.csv", "w") as archivo:
    # Escribir encabezado
    archivo.write("Título,Año inicio,Año fin,Calificación,Género\n")
    
    # Escribir datos
    for serie in series_tv:
        # Convertir cada elemento a string y unir con comas
        linea = ",".join(str(dato) for dato in serie)
        archivo.write(linea + "\n")

print("Archivo 'series_tv.csv' creado con éxito.")

# -----------------------------------------------------------------------------
# 2. LEER DE UN ARCHIVO
# -----------------------------------------------------------------------------

imprimir_seccion("2. LEER DE UN ARCHIVO")

print("# Leer un archivo completo de una vez:")

with open("ejemplo_texto.txt", "r") as archivo:
    contenido = archivo.read()

print("Contenido del archivo 'ejemplo_texto.txt':")
print(f"\n{contenido}")

print("\n# Leer un archivo línea por línea:")

with open("ejemplo_with.txt", "r") as archivo:
    print("Contenido de 'ejemplo_with.txt' línea por línea:")
    
    # Método 1: Usando readline()
    print("\nMétodo 1 - readline():")
    archivo.seek(0)  # Volver al inicio del archivo
    linea = archivo.readline()
    while linea:
        print(f"  {linea}", end="")
        linea = archivo.readline()
    
    # Método 2: Usando readlines()
    print("\n\nMétodo 2 - readlines():")
    archivo.seek(0)  # Volver al inicio del archivo
    lineas = archivo.readlines()
    for i, linea in enumerate(lineas, 1):
        print(f"  Línea {i}: {linea}", end="")
    
    # Método 3: Iterando directamente el archivo (más eficiente)
    print("\n\nMétodo 3 - iteración directa (recomendado):")
    archivo.seek(0)  # Volver al inicio del archivo
    for i, linea in enumerate(archivo, 1):
        print(f"  Línea {i}: {linea}", end="")

# Leer un archivo CSV estructurado
print("\n\n# Leer datos estructurados (CSV):")

with open("series_tv.csv", "r") as archivo:
    # Leer y descartar el encabezado
    encabezado = archivo.readline().strip()
    print(f"Encabezado: {encabezado}")
    
    # Leer los datos
    series = []
    for linea in archivo:
        # Eliminar espacios y saltos de línea, luego dividir por comas
        datos = linea.strip().split(",")
        
        # Convertir los datos a los tipos adecuados
        titulo = datos[0]
        anio_inicio = int(datos[1])
        anio_fin = int(datos[2])
        calificacion = float(datos[3])
        genero = datos[4]
        
        # Guardar como lista
        serie = [titulo, anio_inicio, anio_fin, calificacion, genero]
        series.append(serie)

print("\nSeries leídas del archivo CSV:")
for serie in series:
    print(f"  {serie}")

# -----------------------------------------------------------------------------
# 3. MANEJO DE EXCEPCIONES CON ARCHIVOS
# -----------------------------------------------------------------------------

imprimir_seccion("3. MANEJO DE EXCEPCIONES CON ARCHIVOS")

print("""
Al trabajar con archivos, pueden ocurrir varios errores:
- El archivo puede no existir
- Puede no tener permisos para leer/escribir
- El formato podría ser incorrecto
- Y muchos más...

Es importante manejar estas excepciones adecuadamente:
""")

# Ejemplo de manejo de excepciones
print("\n# Manejo seguro de archivos con try-except:")

try:
    # Intentar abrir un archivo que no existe
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("  ¡Error! El archivo no existe.")
except PermissionError:
    print("  ¡Error! No tienes permisos para acceder al archivo.")
except Exception as e:
    print(f"  ¡Error inesperado! {e}")
finally:
    print("  Esta parte se ejecuta siempre, haya error o no.")

# -----------------------------------------------------------------------------
# 4. TRABAJAR CON RUTAS DE ARCHIVOS
# -----------------------------------------------------------------------------

imprimir_seccion("4. TRABAJAR CON RUTAS DE ARCHIVOS")

import os

print("""
El módulo 'os' y 'os.path' proporcionan funciones para trabajar con rutas:
- os.path.exists(): Verificar si un archivo existe
- os.path.join(): Crear rutas de manera segura
- os.makedirs(): Crear directorios
- Y muchas más...
""")

# Ejemplos de operaciones con rutas
print("\n# Operaciones comunes con rutas:")
print(f"  Ruta actual: {os.getcwd()}")
print(f"  ¿Existe 'ejemplo_texto.txt'?: {os.path.exists('ejemplo_texto.txt')}")
print(f"  ¿Existe 'archivo_inexistente.txt'?: {os.path.exists('archivo_inexistente.txt')}")

# Crear un directorio para archivos
print("\n# Crear un directorio y escribir archivo en él:")

try:
    # Crear directorio si no existe
    if not os.path.exists('datos'):
        os.makedirs('datos')
        print("  Directorio 'datos' creado.")
    else:
        print("  El directorio 'datos' ya existe.")
    
    # Crear una ruta segura usando os.path.join
    ruta_archivo = os.path.join('datos', 'info.txt')
    
    # Escribir en el archivo dentro del directorio
    with open(ruta_archivo, 'w') as archivo:
        archivo.write("Este archivo está dentro de un subdirectorio.\n")
    
    print(f"  Archivo creado en: {ruta_archivo}")

except Exception as e:
    print(f"  Error al trabajar con directorios: {e}")

# ============================================================================
# PARTE 2: TRABAJANDO CON DATOS ESTRUCTURADOS
# ============================================================================

imprimir_seccion("TRABAJANDO CON DATOS ESTRUCTURADOS EN ARCHIVOS")

print("""
En la práctica, a menudo necesitamos guardar y recuperar datos estructurados.
Hay varias formas de hacerlo:
- CSV (valores separados por comas)
- JSON (JavaScript Object Notation)
- Pickle (serialización específica de Python)
- Y muchos otros formatos...
""")

# -----------------------------------------------------------------------------
# 1. TRABAJAR CON ARCHIVOS CSV
# -----------------------------------------------------------------------------

imprimir_seccion("1. TRABAJAR CON ARCHIVOS CSV")

import csv

# Datos más completos para el ejemplo
peliculas = [
    {"titulo": "El Padrino", "director": "Francis Ford Coppola", "año": 1972, 
     "generos": ["Drama", "Crimen"], "calificacion": 9.2, "duracion_min": 175},
    {"titulo": "Pulp Fiction", "director": "Quentin Tarantino", "año": 1994,
     "generos": ["Crimen", "Drama"], "calificacion": 8.9, "duracion_min": 154},
    {"titulo": "Interestelar", "director": "Christopher Nolan", "año": 2014,
     "generos": ["Aventura", "Drama", "Sci-Fi"], "calificacion": 8.6, "duracion_min": 169},
    {"titulo": "El Rey León", "director": "Roger Allers", "año": 1994,
     "generos": ["Animación", "Aventura", "Drama"], "calificacion": 8.5, "duracion_min": 88},
    {"titulo": "Parásitos", "director": "Bong Joon Ho", "año": 2019,
     "generos": ["Comedia", "Drama", "Suspenso"], "calificacion": 8.5, "duracion_min": 132}
]

print("# Escribir datos en formato CSV usando el módulo csv:")

# Escribir el archivo CSV usando el módulo csv
with open("peliculas.csv", "w", newline='', encoding='utf-8') as archivo:
    # Definir las columnas
    columnas = ["titulo", "director", "año", "generos", "calificacion", "duracion_min"]
    
    # Crear el escritor CSV
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    
    # Escribir el encabezado
    escritor.writeheader()
    
    # Escribir las filas
    for pelicula in peliculas:
        # Convertir la lista de géneros a string para poder guardarla
        pelicula_copia = pelicula.copy()
        pelicula_copia["generos"] = "|".join(pelicula_copia["generos"])
        escritor.writerow(pelicula_copia)

print("Archivo 'peliculas.csv' creado con éxito.")

# Leer el archivo CSV
print("\n# Leer datos del archivo CSV usando el módulo csv:")

peliculas_leidas = []
with open("peliculas.csv", "r", newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        # Convertir valores a los tipos correctos
        pelicula = {
            "titulo": fila["titulo"],
            "director": fila["director"],
            "año": int(fila["año"]),
            "generos": fila["generos"].split("|"),  # Convertir string a lista
            "calificacion": float(fila["calificacion"]),
            "duracion_min": int(fila["duracion_min"])
        }
        peliculas_leidas.append(pelicula)

print(f"\nSe leyeron {len(peliculas_leidas)} películas del archivo CSV.")
for pelicula in peliculas_leidas[:2]:  # Mostrar solo las 2 primeras para ejemplo
    print(f"  {pelicula['titulo']} ({pelicula['año']}) - {pelicula['calificacion']}/10")
print("  ...")  # Indicar que hay más películas

# -----------------------------------------------------------------------------
# 2. TRABAJAR CON ARCHIVOS JSON
# -----------------------------------------------------------------------------

imprimir_seccion("2. TRABAJAR CON ARCHIVOS JSON")

import json

print("""
JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos 
que es fácil de leer y escribir para humanos y fácil de analizar para máquinas.

Ventajas de JSON:
- Formato estándar, compatible con muchos lenguajes
- Preserva tipos de datos básicos
- Fácil de leer y editar
- Soporta estructuras de datos jerárquicas y complejas
- Ideal para APIs web y configuraciones
""")

# Datos más elaborados para el ejemplo JSON
peliculas_avanzadas = [
    {
        "titulo": "El Padrino",
        "director": "Francis Ford Coppola",
        "año": 1972,
        "generos": ["Drama", "Crimen"],
        "calificacion": 9.2,
        "duracion_min": 175,
        "reparto": [
            {"nombre": "Marlon Brando", "personaje": "Vito Corleone"},
            {"nombre": "Al Pacino", "personaje": "Michael Corleone"},
            {"nombre": "James Caan", "personaje": "Sonny Corleone"}
        ],
        "premios": {
            "oscars": ["Mejor Película", "Mejor Actor", "Mejor Guion Adaptado"],
            "globos_de_oro": ["Mejor Película - Drama", "Mejor Director", "Mejor Guion"],
            "total": 29
        },
        "disponible_en": ["Netflix", "Amazon Prime", "HBO Max"],
        "metadatos": {
            "presupuesto_millones": 6.5,
            "recaudacion_millones": 246.1,
            "idioma_original": "Inglés",
            "clasificacion": "R"
        }
    },
    {
        "titulo": "Interestelar",
        "director": "Christopher Nolan",
        "año": 2014,
        "generos": ["Aventura", "Drama", "Sci-Fi"],
        "calificacion": 8.6,
        "duracion_min": 169,
        "reparto": [
            {"nombre": "Matthew McConaughey", "personaje": "Cooper"},
            {"nombre": "Anne Hathaway", "personaje": "Dra. Amelia Brand"},
            {"nombre": "Jessica Chastain", "personaje": "Murphy Cooper (adulta)"}
        ],
        "premios": {
            "oscars": ["Mejores Efectos Visuales"],
            "globos_de_oro": [],
            "total": 43
        },
        "disponible_en": ["Netflix", "Paramount+"],
        "metadatos": {
            "presupuesto_millones": 165,
            "recaudacion_millones": 677.5,
            "idioma_original": "Inglés",
            "clasificacion": "PG-13"
        }
    }
]

# Escribir datos en formato JSON
print("\n# Escribir datos estructurados complejos en JSON:")

with open("peliculas_detalladas.json", "w", encoding="utf-8") as archivo:
    json.dump(peliculas_avanzadas, archivo, indent=4, ensure_ascii=False)

print("Archivo 'peliculas_detalladas.json' creado con éxito.")

# Leer datos desde archivo JSON
print("\n# Leer datos desde archivo JSON:")

with open("peliculas_detalladas.json", "r", encoding="utf-8") as archivo:
    peliculas_leidas = json.load(archivo)

print(f"Se leyeron {len(peliculas_leidas)} películas del archivo JSON.")

# Mostrar datos de manera estructurada y formateada
print("\n# Visualizando datos jerárquicos complejos:")
for pelicula in peliculas_leidas:
    print(f"\n{'-'*50}")
    print(f"PELÍCULA: {pelicula['titulo']} ({pelicula['año']})")
    print(f"{'-'*50}")
    print(f"Director: {pelicula['director']}")
    print(f"Géneros: {', '.join(pelicula['generos'])}")
    print(f"Calificación: {pelicula['calificacion']}/10")
    print(f"Duración: {pelicula['duracion_min']} minutos")
    
    print(f"\nReparto principal:")
    for actor in pelicula['reparto']:
        print(f"  - {actor['nombre']} como '{actor['personaje']}'")
    
    print(f"\nPremios destacados:")
    if pelicula['premios']['oscars']:
        print(f"  Oscars: {', '.join(pelicula['premios']['oscars'])}")
    else:
        print("  Oscars: Ninguno")
    print(f"  Total de premios: {pelicula['premios']['total']}")
    
    print(f"\nDisponible en: {', '.join(pelicula['disponible_en'])}")
    print(f"Presupuesto: ${pelicula['metadatos']['presupuesto_millones']} millones")
    print(f"Recaudación: ${pelicula['metadatos']['recaudacion_millones']} millones")

# Manipulación avanzada de datos JSON
print("\n# Manipulación y filtrado de datos JSON:")

# 1. Filtrar películas por género
print("\nPelículas de Ciencia Ficción:")
peliculas_scifi = [p for p in peliculas_leidas if "Sci-Fi" in p["generos"]]
for p in peliculas_scifi:
    print(f"  - {p['titulo']} ({p['año']})")

# 2. Calcular estadísticas
calificaciones = [p["calificacion"] for p in peliculas_leidas]
promedio = sum(calificaciones) / len(calificaciones)
print(f"\nCalificación promedio: {promedio:.1f}/10")

# 3. Buscar la película con mayor recaudación
pelicula_mayor_recaudacion = max(peliculas_leidas, key=lambda p: p["metadatos"]["recaudacion_millones"])
print(f"\nMayor recaudación: {pelicula_mayor_recaudacion['titulo']} (${pelicula_mayor_recaudacion['metadatos']['recaudacion_millones']} millones)")

# 4. Transformar datos - Crear una lista de actores y sus películas
print("\n# Transformando datos - Lista de actores:")
actores = {}
for pelicula in peliculas_leidas:
    for actor in pelicula['reparto']:
        if actor['nombre'] not in actores:
            actores[actor['nombre']] = []
        actores[actor['nombre']].append({
            "pelicula": pelicula['titulo'],
            "personaje": actor['personaje'],
            "año": pelicula['año']
        })

# Mostrar algunos actores
print("\nFilmografía por actor:")
for actor, filmografia in list(actores.items())[:2]:  # Mostrar solo algunos actores
    print(f"\n{actor}:")
    for papel in filmografia:
        print(f"  - {papel['pelicula']} ({papel['año']}) como '{papel['personaje']}'")

# Guardar esta nueva estructura en otro archivo JSON
with open("actores_filmografia.json", "w", encoding="utf-8") as archivo:
    json.dump(actores, archivo, indent=4, ensure_ascii=False)
print("\nDatos de filmografía guardados en 'actores_filmografia.json'")

# Ejemplo de actualización de datos JSON
print("\n# Actualizando datos en un archivo JSON:")
# Añadir una nueva película
nueva_pelicula = {
    "titulo": "El Resplandor",
    "director": "Stanley Kubrick",
    "año": 1980,
    "generos": ["Terror", "Drama", "Misterio"],
    "calificacion": 8.4,
    "duracion_min": 146,
    "reparto": [
        {"nombre": "Jack Nicholson", "personaje": "Jack Torrance"},
        {"nombre": "Shelley Duvall", "personaje": "Wendy Torrance"}
    ],
    "premios": {
        "oscars": [],
        "globos_de_oro": [],
        "total": 8
    },
    "disponible_en": ["HBO Max", "Amazon Prime"],
    "metadatos": {
        "presupuesto_millones": 19,
        "recaudacion_millones": 47.3,
        "idioma_original": "Inglés",
        "clasificacion": "R"
    }
}

peliculas_leidas.append(nueva_pelicula)

# Actualizar la calificación de una película existente
for pelicula in peliculas_leidas:
    if pelicula["titulo"] == "El Padrino":
        pelicula["calificacion"] = 9.3
        print(f"Se actualizó la calificación de '{pelicula['titulo']}' a {pelicula['calificacion']}")

# Guardar los cambios
with open("peliculas_actualizadas.json", "w", encoding="utf-8") as archivo:
    json.dump(peliculas_leidas, archivo, indent=4, ensure_ascii=False)

print("Datos actualizados guardados en 'peliculas_actualizadas.json'")

# Trabajar con JSON como configuración
print("\n# Usando JSON como configuración:")
configuracion = {
    "app": {
        "nombre": "Gestor de Películas",
        "version": "1.2.0",
        "tema": "oscuro"
    },
    "usuario": {
        "id": 12345,
        "preferencias": {
            "mostrar_calificacion": True,
            "ordenar_por": "año",
            "ascendente": False
        }
    },
    "conexion": {
        "tiempo_espera": 30,
        "reintentos": 3,
        "servidores": ["srv1.ejemplo.com", "srv2.ejemplo.com"]
    }
}

with open("config.json", "w", encoding="utf-8") as archivo:
    json.dump(configuracion, archivo, indent=4)

print("Archivo de configuración creado")

# Leer configuración
with open("config.json", "r", encoding="utf-8") as archivo:
    config = json.load(archivo)

print(f"Aplicación: {config['app']['nombre']} v{config['app']['version']}")
print(f"Tema: {config['app']['tema']}")
print(f"Ordenar por: {config['usuario']['preferencias']['ordenar_por']} "
      f"({'ascendente' if config['usuario']['preferencias']['ascendente'] else 'descendente'})")

# -----------------------------------------------------------------------------
# 3. ANALIZAR Y PROCESAR DATOS DE ARCHIVOS
# -----------------------------------------------------------------------------

imprimir_seccion("3. ANALIZAR Y PROCESAR DATOS DE ARCHIVOS")

print("# Realizar análisis de los datos leídos:")

# Calcular el promedio de calificaciones
calificaciones = [p["calificacion"] for p in peliculas_leidas]
promedio = sum(calificaciones) / len(calificaciones)
print(f"Calificación promedio de películas: {promedio:.2f}/10")

# Encontrar la película mejor calificada
mejor_pelicula = max(peliculas_leidas, key=lambda x: x['calificacion'])
print(f"Película mejor calificada: {mejor_pelicula['titulo']} ({mejor_pelicula['calificacion']}/10)")

# Encontrar la película más reciente
pelicula_reciente = max(peliculas_leidas, key=lambda x: x['año'])
print(f"Película más reciente: {pelicula_reciente['titulo']} ({pelicula_reciente['año']})")

# Agrupar películas por género
print("\n# Películas por género:")
generos = {}

for pelicula in peliculas_leidas:
    for genero in pelicula['generos']:
        if genero not in generos:
            generos[genero] = []
        generos[genero].append(pelicula['titulo'])

for genero, titulos in sorted(generos.items()):
    print(f"  {genero}: {len(titulos)} películas")
    for titulo in titulos:
        print(f"    - {titulo}")

# Filtrar películas por criterio
print("\n# Filtrar películas posteriores al 2000 con calificación > 8.5:")
filtradas = [p for p in peliculas_leidas if p['año'] > 2000 and p['calificacion'] > 8.5]

for pelicula in filtradas:
    print(f"  {pelicula['titulo']} ({pelicula['año']}) - {pelicula['calificacion']}/10")

# -----------------------------------------------------------------------------
# 4. BÚSQUEDA Y ACTUALIZACIÓN DE DATOS
# -----------------------------------------------------------------------------

imprimir_seccion("4. BÚSQUEDA Y ACTUALIZACIÓN DE DATOS")

print("# Actualizar información en nuestros datos:")

# Buscar y actualizar información
titulo_buscar = "Interestelar"
nueva_calificacion = 9.0

# Buscar la película
encontrada = False
for pelicula in peliculas_leidas:
    if pelicula['titulo'] == titulo_buscar:
        print(f"Película encontrada: {pelicula['titulo']}")
        print(f"  Calificación anterior: {pelicula['calificacion']}")
        pelicula['calificacion'] = nueva_calificacion
        print(f"  Calificación actualizada: {pelicula['calificacion']}")
        encontrada = True
        break

if not encontrada:
    print(f"No se encontró la película '{titulo_buscar}'")

# Guardar los cambios de vuelta en el archivo JSON
with open("peliculas_actualizadas.json", "w", encoding="utf-8") as archivo:
    json.dump(peliculas_leidas, archivo, indent=4, ensure_ascii=False)

print("\nArchivo 'peliculas_actualizadas.json' creado con los datos modificados.")

# Añadir una nueva película
nueva_pelicula = {
    "titulo": "Todo En Todas Partes Al Mismo Tiempo",
    "director": "Daniel Kwan, Daniel Scheinert",
    "año": 2022,
    "generos": ["Aventura", "Comedia", "Sci-Fi"],
    "calificacion": 8.9,
    "duracion_min": 139
}

peliculas_leidas.append(nueva_pelicula)
print(f"\nSe añadió la película: {nueva_pelicula['titulo']}")

# Guardar la lista actualizada
with open("peliculas_actualizadas.json", "w", encoding="utf-8") as archivo:
    json.dump(peliculas_leidas, archivo, indent=4, ensure_ascii=False)

print("Archivo 'peliculas_actualizadas.json' actualizado con la nueva película.")

# ============================================================================
# APLICACIÓN PRÁCTICA: SISTEMA DE GESTIÓN DE PELÍCULAS
# ============================================================================

imprimir_seccion("APLICACIÓN PRÁCTICA: SISTEMA DE GESTIÓN DE PELÍCULAS")

print("""
A continuación veremos una implementación práctica de un sistema completo
para gestionar una colección de películas usando archivos JSON:

Características:
- Cargar y guardar películas en formato JSON
- Buscar películas por diferentes criterios
- Filtrar, ordenar y estadísticas
- Agregar, eliminar y actualizar películas
- Exportar a CSV
""")

def cargar_peliculas(archivo='peliculas.json'):
    """Carga películas desde un archivo JSON"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Se utilizará una lista vacía.")
        return []
    except json.JSONDecodeError:
        print(f"Error al leer {archivo}. El formato no es válido.")
        return []

def guardar_peliculas(peliculas, archivo='peliculas.json'):
    """Guarda la lista de películas en un archivo JSON"""
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(peliculas, f, indent=4, ensure_ascii=False)
    print(f"Datos guardados en {archivo}")

def mostrar_pelicula(pelicula):
    """Muestra la información de una película con formato"""
    print(f"\nTítulo: {pelicula['titulo']}")
    print(f"Director: {pelicula['director']}")
    print(f"Año: {pelicula['año']}")
    print(f"Géneros: {', '.join(pelicula['generos'])}")
    print(f"Calificación: {pelicula['calificacion']}/10")
    print(f"Duración: {pelicula['duracion_min']} minutos")
    
    # Mostrar información adicional si está disponible
    if 'reparto' in pelicula:
        print("\nReparto principal:")
        for actor in pelicula['reparto'][:3]:  # Mostrar solo los 3 primeros actores
            print(f"  - {actor['nombre']} como '{actor['personaje']}'")
    
    if 'premios' in pelicula and isinstance(pelicula['premios'], dict):
        print("\nPremios destacados:")
        if 'oscars' in pelicula['premios'] and pelicula['premios']['oscars']:
            print(f"  Oscars: {', '.join(pelicula['premios']['oscars'])}")
        print(f"  Total de premios: {pelicula['premios'].get('total', 0)}")
    
    if 'metadatos' in pelicula:
        meta = pelicula['metadatos']
        print("\nDatos adicionales:")
        if 'presupuesto_millones' in meta:
            print(f"  Presupuesto: ${meta['presupuesto_millones']} millones")
        if 'recaudacion_millones' in meta:
            print(f"  Recaudación: ${meta['recaudacion_millones']} millones")

def mostrar_todas_peliculas(peliculas, detalle=False):
    """Muestra todas las películas en formato resumido o detallado"""
    if not peliculas:
        print("\nNo hay películas para mostrar.")
        return
        
    print(f"\nLista de películas ({len(peliculas)} encontradas):")
    for i, pelicula in enumerate(peliculas, 1):
        if detalle:
            print(f"\n{i}. {pelicula['titulo']} ({pelicula['año']})")
            print(f"   Director: {pelicula['director']}")
            print(f"   Géneros: {', '.join(pelicula['generos'])}")
            print(f"   Calificación: {pelicula['calificacion']}/10")
        else:
            print(f"{i}. {pelicula['titulo']} ({pelicula['año']}) - {pelicula['calificacion']}/10")

def buscar_pelicula(peliculas, criterio, valor):
    """Busca una película por diferentes criterios"""
    resultados = []
    valor = str(valor).lower()
    
    for pelicula in peliculas:
        if criterio == "titulo" and valor in pelicula['titulo'].lower():
            resultados.append(pelicula)
        elif criterio == "director" and valor in pelicula['director'].lower():
            resultados.append(pelicula)
        elif criterio == "año" and valor == str(pelicula['año']):
            resultados.append(pelicula)
        elif criterio == "genero":
            for genero in pelicula['generos']:
                if valor in genero.lower():
                    resultados.append(pelicula)
                    break
        elif criterio == "calificacion_min" and pelicula['calificacion'] >= float(valor):
            resultados.append(pelicula)
    
    return resultados

def agregar_pelicula(peliculas):
    """Añade una nueva película a la colección"""
    print("\nAgregar nueva película:")
    try:
        titulo = input("  Título: ")
        director = input("  Director: ")
        año = int(input("  Año: "))
        generos_input = input("  Géneros (separados por coma): ")
        generos = [g.strip() for g in generos_input.split(',')]
        calificacion = float(input("  Calificación (0-10): "))
        duracion = int(input("  Duración (minutos): "))
        
        # Datos adicionales - opcionales
        agregar_reparto = input("\n¿Agregar información de reparto? (s/n): ").lower() == 's'
        reparto = []
        if agregar_reparto:
            while True:
                actor = input("  Nombre del actor (o vacío para terminar): ")
                if not actor:
                    break
                personaje = input("  Personaje: ")
                reparto.append({"nombre": actor, "personaje": personaje})
        
        # Crear la nueva película
        nueva_pelicula = {
            "titulo": titulo,
            "director": director,
            "año": año,
            "generos": generos,
            "calificacion": calificacion,
            "duracion_min": duracion
        }
        
        # Añadir campos opcionales si hay información
        if reparto:
            nueva_pelicula["reparto"] = reparto
        
        peliculas.append(nueva_pelicula)
        print("Película añadida con éxito")
        return True
    except ValueError:
        print("Error: Asegúrate de ingresar números válidos para año, calificación y duración.")
        return False

def eliminar_pelicula(peliculas, indice):
    """Elimina una película por su índice"""
    if 0 <= indice < len(peliculas):
        pelicula = peliculas.pop(indice)
        print(f"Película '{pelicula['titulo']}' eliminada.")
        return True
    else:
        print("Índice no válido.")
        return False

def actualizar_pelicula(peliculas, indice):
    """Actualiza la información de una película"""
    if 0 <= indice < len(peliculas):
        pelicula = peliculas[indice]
        print(f"\nActualizando película: {pelicula['titulo']}")
        
        print("Deja en blanco para mantener el valor actual.")
        
        titulo = input(f"Título [{pelicula['titulo']}]: ")
        if titulo:
            pelicula['titulo'] = titulo
            
        director = input(f"Director [{pelicula['director']}]: ")
        if director:
            pelicula['director'] = director
            
        try:
            año_str = input(f"Año [{pelicula['año']}]: ")
            if año_str:
                pelicula['año'] = int(año_str)
                
            generos_actuales = ", ".join(pelicula['generos'])
            generos_input = input(f"Géneros [{generos_actuales}]: ")
            if generos_input:
                pelicula['generos'] = [g.strip() for g in generos_input.split(',')]
                
            calificacion_str = input(f"Calificación [{pelicula['calificacion']}]: ")
            if calificacion_str:
                pelicula['calificacion'] = float(calificacion_str)
                
            duracion_str = input(f"Duración en minutos [{pelicula['duracion_min']}]: ")
            if duracion_str:
                pelicula['duracion_min'] = int(duracion_str)
                
            print("\nPelícula actualizada con éxito.")
            return True
        except ValueError:
            print("Error: Verifica que los valores numéricos sean correctos.")
            return False
    else:
        print("Índice no válido.")
        return False

def exportar_a_csv(peliculas, archivo='peliculas_export.csv'):
    """Exporta la lista de películas a un archivo CSV"""
    try:
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            # Definir columnas basadas en campos comunes
            columnas = ["titulo", "director", "año", "generos", 
                       "calificacion", "duracion_min"]
            
            escritor = csv.DictWriter(f, fieldnames=columnas)
            escritor.writeheader()
            
            for pelicula in peliculas:
                # Crear una copia para modificar
                p_dict = {k: pelicula[k] for k in columnas if k in pelicula}
                
                # Convertir la lista de géneros a string
                if 'generos' in p_dict:
                    p_dict['generos'] = ", ".join(p_dict['generos'])
                
                escritor.writerow(p_dict)
        
        print(f"\nSe exportaron {len(peliculas)} películas a {archivo}")
        return True
    except Exception as e:
        print(f"Error al exportar: {e}")
        return False

def estadisticas_peliculas(peliculas):
    """Muestra estadísticas sobre la colección de películas"""
    if not peliculas:
        print("\nNo hay películas para analizar.")
        return
    
    print("\n=== ESTADÍSTICAS DE LA COLECCIÓN ===")
    
    # Número total de películas
    print(f"Total de películas: {len(peliculas)}")
    
    # Películas por década
    decadas = {}
    for p in peliculas:
        decada = (p['año'] // 10) * 10
        decadas[decada] = decadas.get(decada, 0) + 1
    
    print("\nPelículas por década:")
    for decada in sorted(decadas.keys()):
        print(f"  {decada}-{decada+9}: {decadas[decada]} películas")
    
    # Directores con más películas
    directores = {}
    for p in peliculas:
        directores[p['director']] = directores.get(p['director'], 0) + 1
    
    print("\nDirectores con más películas:")
    top_directores = sorted(directores.items(), key=lambda x: x[1], reverse=True)[:3]
    for director, count in top_directores:
        print(f"  {director}: {count} películas")
    
    # Géneros más comunes
    generos = {}
    for p in peliculas:
        for g in p['generos']:
            generos[g] = generos.get(g, 0) + 1
    
    print("\nGéneros más comunes:")
    top_generos = sorted(generos.items(), key=lambda x: x[1], reverse=True)[:5]
    for genero, count in top_generos:
        print(f"  {genero}: {count} películas")
    
    # Calificación promedio
    calificaciones = [p['calificacion'] for p in peliculas]
    promedio = sum(calificaciones) / len(calificaciones)
    
    print(f"\nCalificación promedio: {promedio:.2f}/10")
    print(f"Calificación más alta: {max(calificaciones)}/10")
    print(f"Calificación más baja: {min(calificaciones)}/10")
    
    # Duración promedio
    duraciones = [p['duracion_min'] for p in peliculas]
    duracion_promedio = sum(duraciones) / len(duraciones)
    
    print(f"\nDuración promedio: {duracion_promedio:.1f} minutos")
    print(f"Película más larga: {max(duraciones)} minutos")
    print(f"Película más corta: {min(duraciones)} minutos")

# Ejemplo de uso del sistema de gestión completo
print("\n# Demostración del sistema de gestión de películas:")

# En este ejemplo usaremos los datos que ya hemos creado
mis_peliculas = peliculas.copy()  # Usar la variable de películas que ya tenemos

print(f"Colección cargada: {len(mis_peliculas)} películas")

# Mostrar todas las películas
mostrar_todas_peliculas(mis_peliculas)

# Buscar películas por criterio
print("\n# Buscando películas por género 'Drama':")
resultados = buscar_pelicula(mis_peliculas, "genero", "Drama")
mostrar_todas_peliculas(resultados)

# Buscar por calificación mínima
print("\n# Buscando películas con calificación mayor o igual a 9:")
resultados = buscar_pelicula(mis_peliculas, "calificacion_min", 9.0)
mostrar_todas_peliculas(resultados)

# Mostrar estadísticas
estadisticas_peliculas(mis_peliculas)

# Ejemplo: añadir película (simulado)
print("\n# Simulando añadir película:")
nueva = {
    "titulo": "Matrix",
    "director": "Lana y Lilly Wachowski",
    "año": 1999,
    "generos": ["Ciencia Ficción", "Acción"],
    "calificacion": 8.7,
    "duracion_min": 136,
    "reparto": [
        {"nombre": "Keanu Reeves", "personaje": "Neo"},
        {"nombre": "Laurence Fishburne", "personaje": "Morpheus"}
    ]
}

mis_peliculas.append(nueva)
print(f"Película '{nueva['titulo']}' añadida")

# Exportar a CSV
exportar_a_csv(mis_peliculas, "peliculas_export.csv")

print("\nEste es un ejemplo de un sistema completo de gestión de películas.")
print("En una aplicación real, se añadiría un menú interactivo y más funcionalidades.")

# ============================================================================
# CONCLUSIÓN
# ============================================================================

imprimir_seccion("CONCLUSIÓN")

print("""
En este tutorial has aprendido a:

1. Trabajar con archivos de texto básicos (abrir, leer, escribir, cerrar)
2. Utilizar el contexto 'with' para manejar archivos de forma segura
3. Manejar excepciones comunes relacionadas con archivos
4. Trabajar con rutas de archivos usando el módulo os
5. Procesar datos estructurados con CSV y JSON
6. Analizar y actualizar información de archivos
7. Implementar un sistema simple de gestión basado en archivos

Recuerda siempre:
- Cerrar los archivos después de usarlos (o usar 'with')
- Manejar las excepciones apropiadamente
- Elegir el formato de archivo adecuado según tus necesidades
- Validar los datos al leerlos de archivos externos

¡Ahora tienes las bases para trabajar con archivos en Python!
""")

# Limpiar archivos de ejemplo (opcional - comentar para evitar)
import os

print("\n# Eliminando archivos de ejemplo creados en este tutorial...")
archivos_ejemplo = [
    "ejemplo_texto.txt", "ejemplo_with.txt", "series_tv.csv",
    "peliculas.csv", "peliculas.json", "peliculas_actualizadas.json"
]

for archivo in archivos_ejemplo:
    try:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"  Eliminado: {archivo}")
    except Exception as e:
        print(f"  Error al eliminar {archivo}: {e}")

# También eliminar el directorio de ejemplo y su contenido
try:
    if os.path.exists(os.path.join('datos', 'info.txt')):
        os.remove(os.path.join('datos', 'info.txt'))
        print("  Eliminado: datos/info.txt")
    
    if os.path.exists('datos'):
        os.rmdir('datos')  # Solo funciona si el directorio está vacío
        print("  Eliminado: directorio 'datos'")
except Exception as e:
    print(f"  Error al eliminar el directorio 'datos': {e}")

print("\n¡Ejemplo completado con éxito!")
