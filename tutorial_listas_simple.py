#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tutorial de Listas en Python (Versión Simplificada)
Autor: Diego
Fecha: 4 de junio de 2025
"""

import copy  # Para copias profundas

# Función para imprimir secciones con formato
def imprimir_seccion(titulo):
    """Imprime un título de sección con formato para mejor visualización."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# PARTE 1: LISTAS BÁSICAS
# ============================================================================

# SECCIÓN 1: INTRODUCCIÓN A LAS LISTAS
imprimir_seccion("INTRODUCCIÓN A LAS LISTAS")

print("""
Una lista en Python es una colección ordenada y mutable de elementos.
Puede contener elementos de diferentes tipos: números, cadenas, booleanos,
incluso otras listas u objetos.
""")

# Creación de listas
print("# Formas de crear listas:")

lista_vacia = []
print(f"Lista vacía: {lista_vacia}")

numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

mixta = [1, "Hola", True, 3.14]
print(f"Lista con diferentes tipos: {mixta}")

# Creación con list()
rango_lista = list(range(1, 6))  # Convierte un rango a lista
print(f"Lista desde un rango: {rango_lista}")

caracteres = list("Python")  # Convierte una cadena a lista de caracteres
print(f"Lista de caracteres: {caracteres}")

# Listas por comprensión
cuadrados = [x**2 for x in range(1, 6)]
print(f"Lista por comprensión (cuadrados): {cuadrados}") #lista de cuadrados

pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Lista por comprensión (números pares): {pares}") #lista de números pares


# SECCIÓN 2: ACCEDER A ELEMENTOS DE UNA LISTA
imprimir_seccion("ACCEDER A ELEMENTOS DE UNA LISTA")

frutas = ["manzana", "banana", "cereza", "durazno", "fresa"]
print(f"Lista de frutas: {frutas}")

# Acceso por índice (inicia en 0)
print("\n# Acceso por índice:")
print(f"Primera fruta: {frutas[0]}")
print(f"Segunda fruta: {frutas[1]}")
print(f"Última fruta: {frutas[4]}")

# Índices negativos (cuentan desde el final)
print("\n# Índices negativos:")
print(f"Última fruta: {frutas[-1]}")
print(f"Penúltima fruta: {frutas[-2]}")

# Sublistas (slicing)
print("\n# Sublistas con slicing [inicio:fin:paso]:")
print(f"Primeras tres frutas: {frutas[0:3]}")        # Elementos 0, 1, 2
print(f"Forma alternativa: {frutas[:3]}")           # Inicio omitido = 0
print(f"Desde la tercera hasta el final: {frutas[2:]}") # Fin omitido = hasta el final
print(f"Últimas dos frutas: {frutas[-2:]}")
print(f"Todas excepto la primera y última: {frutas[1:-1]}")
print(f"Lista completa: {frutas[:]}")                # Copia de la lista

# Slicing con paso
print("\n# Slicing con paso:")
print(f"Elementos alternos: {frutas[::2]}")          # Paso 2: 0, 2, 4...
print(f"Lista inversa: {frutas[::-1]}")              # Paso -1: invierte la lista


# SECCIÓN 3: MODIFICAR LISTAS
imprimir_seccion("MODIFICAR LISTAS")

colores = ["rojo", "verde", "azul"]
print(f"Lista original: {colores}")

# Cambiar un elemento específico
colores[1] = "amarillo"
print(f"Después de cambiar el segundo elemento: {colores}")

# Añadir elementos
print("\n# Añadir elementos:")

colores.append("morado")  # Añade al final
print(f"Después de append('morado'): {colores}")

colores.insert(1, "naranja")  # Inserta en posición específica
print(f"Después de insert(1, 'naranja'): {colores}")

otros_colores = ["blanco", "negro"]
colores.extend(otros_colores)  # Añade otra lista al final
print(f"Después de extend(['blanco', 'negro']): {colores}")

# Eliminar elementos
print("\n# Eliminar elementos:")

colores.remove("azul")  # Elimina por valor
print(f"Después de remove('azul'): {colores}")

eliminado = colores.pop()  # Elimina y retorna el último elemento
print(f"Elemento eliminado con pop(): {eliminado}")
print(f"Lista después de pop(): {colores}")

eliminado_pos = colores.pop(1)  # Elimina y retorna el elemento en índice 1
print(f"Elemento eliminado con pop(1): {eliminado_pos}")
print(f"Lista después de pop(1): {colores}")

del colores[0]  # Elimina por índice
print(f"Después de del colores[0]: {colores}")

colores.clear()  # Vacía la lista
print(f"Después de clear(): {colores}")


# SECCIÓN 4: RECORRER LISTAS
imprimir_seccion("RECORRER LISTAS")

animales = ["perro", "gato", "conejo", "pez", "tortuga"]
print(f"Lista de animales: {animales}")

# Recorrer con for
print("\n# Recorrer con for:")
print("for animal in animales:")
for animal in animales:
    print(f"  - {animal}")

# Recorrer con índice
print("\n# Recorrer con range y len:")
print("for i in range(len(animales)):")
for i in range(len(animales)):
    print(f"  - Índice {i}: {animales[i]}")

# Recorrer con enumerate
print("\n# Recorrer con enumerate (método recomendado para índices):")
print("for indice, animal in enumerate(animales):")
for indice, animal in enumerate(animales):
    print(f"  - Índice {indice}: {animal}")

# Recorrer con enumerate con inicio personalizado
print("\n# Recorrer con enumerate comenzando desde 1:")
print("for num, animal in enumerate(animales, start=1):")
for num, animal in enumerate(animales, start=1):
    print(f"  - Animal #{num}: {animal}")


# SECCIÓN 5: BUSCAR EN LISTAS
imprimir_seccion("BUSCAR EN LISTAS")

numeros = [10, 20, 30, 10, 40, 50, 10, 60]
print(f"Lista de números: {numeros}")

# Verificar si un elemento está en la lista
print("\n# Verificar existencia con 'in':")
print(f"¿Está el 30 en la lista? {'Sí' if 30 in numeros else 'No'}")
print(f"¿Está el 35 en la lista? {'Sí' if 35 in numeros else 'No'}")

# Contar ocurrencias de un elemento
print("\n# Contar ocurrencias:")
print(f"El número 10 aparece {numeros.count(10)} veces")

# Encontrar índice de un elemento
print("\n# Encontrar índice:")
try:
    print(f"Índice del primer 10: {numeros.index(10)}")
    print(f"Índice del primer 30: {numeros.index(30)}")
    
    # Buscar a partir de una posición específica
    print(f"Índice del primer 10 a partir de la posición 1: {numeros.index(10, 1)}")
    
    # Si el elemento no existe, lanza ValueError
    print(f"Índice del 100: {numeros.index(100)}")
except ValueError as e:
    print(f"Error: {e}")

# Búsqueda manual
print("\n# Búsqueda manual con bucle:")
valor_buscar = 10
indices = []
for i, num in enumerate(numeros):
    if num == valor_buscar:
        indices.append(i)
print(f"Índices donde aparece el {valor_buscar}: {indices}")


# SECCIÓN 6: ORDENAR Y OTRAS OPERACIONES
imprimir_seccion("ORDENAR Y OTRAS OPERACIONES")

calificaciones = [85, 90, 75, 95, 70, 80]
print(f"Lista original: {calificaciones}")

# Ordenar
calificaciones_ordenadas = sorted(calificaciones)  # Devuelve nueva lista ordenada
print(f"Lista ordenada con sorted(): {calificaciones_ordenadas}")
print(f"Lista original sin cambios: {calificaciones}")

calificaciones.sort()  # Modifica la lista original
print(f"Lista ordenada con .sort(): {calificaciones}")

# Ordenar descendente
calificaciones.sort(reverse=True)
print(f"Lista ordenada descendente: {calificaciones}")

# Revertir lista (no ordena, solo invierte)
calificaciones.reverse()
print(f"Lista invertida con .reverse(): {calificaciones}")

# Estadísticas básicas
print("\n# Estadísticas básicas:")
print(f"Mínimo: {min(calificaciones)}")
print(f"Máximo: {max(calificaciones)}")
print(f"Suma: {sum(calificaciones)}")
print(f"Promedio: {sum(calificaciones) / len(calificaciones)}")

# Longitud
print(f"Número de elementos: {len(calificaciones)}")


# SECCIÓN 7: COPIAR LISTAS
imprimir_seccion("COPIAR LISTAS")

original = [1, 2, 3, 4, 5]
print(f"Lista original: {original}")

# Asignación directa (crea una referencia, no una copia)
print("\n# Asignación directa (referencia):")
referencia = original
print(f"Lista por referencia: {referencia}")

referencia[0] = 99  # Cambia ambas listas
print(f"Después de cambiar referencia[0] = 99:")
print(f"Original: {original}")  # Cambió también
print(f"Referencia: {referencia}")

# Restaurar lista
original = [1, 2, 3, 4, 5]
print(f"\nLista original restaurada: {original}")

# Copia superficial (shallow copy)
print("\n# Copia superficial:")

# Método 1: usando [:]
copia1 = original[:]
print(f"Copia usando [:]: {copia1}")

# Método 2: usando list()
copia2 = list(original)
print(f"Copia usando list(): {copia2}")

# Método 3: usando copy()
copia3 = original.copy()
print(f"Copia usando .copy(): {copia3}")

# Probar la independencia de las copias
copia1[0] = 99
print(f"\nDespués de cambiar copia1[0] = 99:")
print(f"Original: {original}")  # No cambió
print(f"Copia1: {copia1}")      # Sí cambió

# Copia profunda (deep copy) - necesaria para listas anidadas
lista_anidada = [1, 2, [3, 4]]
print(f"\nLista anidada original: {lista_anidada}")

copia_superficial = lista_anidada.copy()
copia_profunda = copy.deepcopy(lista_anidada)

# Modificar la lista interna
lista_anidada[2][0] = 99
print(f"\nDespués de modificar lista_anidada[2][0] = 99:")
print(f"Original: {lista_anidada}")
print(f"Copia superficial: {copia_superficial}")  # La sublista también cambia
print(f"Copia profunda: {copia_profunda}")  # La sublista no cambia


# ============================================================================
# PARTE 2: LISTAS DE LISTAS 
# ============================================================================

# SECCIÓN 8: INTRODUCCIÓN A LISTAS DE LISTAS
imprimir_seccion("INTRODUCCIÓN A LISTAS DE LISTAS")

print("""
Las listas de listas son estructuras de datos que contienen otras listas como elementos.
Son extremadamente útiles para representar:
- Datos estructurados (como una tabla de información)
- Información jerárquica (como árboles o categorías anidadas)
- Registros con múltiples campos (similar a una base de datos)
- Datos heterogéneos (diferentes tipos de información en cada sublista)
""")

# Crear lista de series de TV (ejemplo práctico y real)
print("# Creación de una lista de listas con datos de series de TV:")
series = [
    ["The Office", 2005, 2013, 9, 770815, ["Comedia"]],
    ["Breaking Bad", 2008, 2013, 9.5, 2314919, ["Crimen", "Drama", "Suspenso"]],
    ["Band of Brothers", 2001, 2001, 9.4, 559518, ["Acción", "Drama", "Histórica"]],
    ["Game of Thrones", 2011, 2019, 9.2, 2422280, ["Acción", "Aventura", "Drama"]],
    ["The Simpsons", 1989, "NA", 8.6, 451961, ["Animación", "Comedia"]]
]
print("Lista de series de TV (primeras 5):")
for serie in series:
    print(f"  {serie}")

print("\n# Explicación de la estructura:")
print("  [Título, Año inicio, Año fin, Calificación, Número de votos, [Géneros]]")

# Crear lista de listas por comprensión
print("\n# Lista de listas con valores por comprensión:")
tabla_comp = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print(f"Lista de listas por comprensión:")
for fila in tabla_comp:
    print(f"  {fila}")

# Lista de listas con elementos heterogéneos
print("\n# Lista de listas con elementos heterogéneos:")
datos_mixtos = [
    ["Juan", 25, ["Python", "JavaScript"], True],
    ["Ana", 30, ["Java", "C++", "SQL"], False],
    ["Carlos", 22, ["HTML", "CSS"], True]
]
print(f"Lista de datos personales:")
for persona in datos_mixtos:
    print(f"  {persona}")


# SECCIÓN 9: ACCEDER A ELEMENTOS EN LISTAS DE LISTAS
imprimir_seccion("ACCEDER A ELEMENTOS EN LISTAS DE LISTAS")

# Usar el ejemplo de series de TV definido anteriormente
print("# Accediendo a datos de series de TV:")
print(f"Lista completa de series: {len(series)} series")

# Acceder por índices
print("\n# Acceso por índices [serie][dato]:")
print(f"Primera serie, título: {series[0][0]}")  # The Office
print(f"Segunda serie, calificación: {series[1][3]}")  # 9.5
print(f"Tercera serie, año inicio: {series[2][1]}")  # 2001

# Acceder a elementos anidados (lista dentro de lista)
print("\n# Acceso a elementos dentro de sublistas:")
print(f"Géneros de Game of Thrones: {series[3][5]}")  # ['Acción', 'Aventura', 'Drama']
print(f"Primer género de Breaking Bad: {series[1][5][0]}")  # Crimen

# Acceder a un registro completo
print("\n# Acceso a un registro completo:")
breaking_bad = series[1]
print(f"Datos de Breaking Bad: {breaking_bad}")

# Extraer columnas específicas (todos los títulos, todas las calificaciones)
print("\n# Extraer columnas (datos específicos de todas las series):")
titulos = [serie[0] for serie in series]
calificaciones = [serie[3] for serie in series]
print(f"Títulos: {titulos}")
print(f"Calificaciones: {calificaciones}")

# Acceder a una porción de la lista de series
print("\n# Acceder a las primeras 3 series:")
primeras_series = series[:3]
for serie in primeras_series:
    print(f"  {serie[0]} ({serie[1]}-{serie[2]})")


# SECCIÓN 10: MODIFICAR LISTAS DE LISTAS
imprimir_seccion("MODIFICAR LISTAS DE LISTAS")

# Copia de trabajo de las series para modificar
series_trabajo = series.copy()
print("Lista de series original (primeras 3):")
for i in range(3):
    print(f"  {series_trabajo[i]}")

# Modificar un elemento específico
print("\n# Modificar un elemento específico:")
series_trabajo[0][3] = 9.1  # Cambiar calificación de The Office
series_trabajo[1][5].append("Thriller")  # Añadir un género a Breaking Bad
print("Después de modificar elementos específicos:")
print(f"  The Office con nueva calificación: {series_trabajo[0]}")
print(f"  Breaking Bad con género añadido: {series_trabajo[1]}")

# Modificar un registro completo
print("\n# Modificar un registro completo:")
series_trabajo[0] = ["The Office (US)", 2005, 2013, 9.1, 770815, ["Comedia", "Sitcom"]]
print("Después de reemplazar el primer registro:")
print(f"  {series_trabajo[0]}")

# Añadir un nuevo registro
print("\n# Añadir un nuevo registro:")
nueva_serie = ["Stranger Things", 2016, "NA", 8.6, 1435806, ["Drama", "Fantasía", "Terror"]]
series_trabajo.append(nueva_serie)
print(f"Después de añadir una nueva serie (ahora hay {len(series_trabajo)} series):")
print(f"  Nueva serie añadida: {series_trabajo[-1]}")

# Eliminar un registro
print("\n# Eliminar un registro:")
serie_eliminada = series_trabajo.pop(2)  # Elimina la tercera serie
print(f"Serie eliminada: {serie_eliminada[0]}")
print(f"Después de eliminar una serie (ahora hay {len(series_trabajo)} series)")

# Insertar un registro en una posición específica
print("\n# Insertar un registro en una posición específica:")
serie_nueva = ["31 minutos", 2002, 2014, 9.1, 1710, ["Comedia", "Familiar", "Fantasía"]]
series_trabajo.insert(2, serie_nueva)  # Inserta en la posición 2
print("Después de insertar una serie en la posición 2:")
print(f"  Serie insertada: {series_trabajo[2]}")


# SECCIÓN 14: CASOS DE USO AVANZADOS
imprimir_seccion("CASOS DE USO AVANZADOS")


# Representación de datos tabulares
print("\n# Ejemplo 1: Datos tabulares (estudiantes y calificaciones)")
estudiantes = [
    ["Ana", 85, 90, 92],
    ["Juan", 75, 80, 85],
    ["María", 95, 92, 88]
]

print("Datos de estudiantes [Nombre, Matemáticas, Ciencias, Historia]:")
for estudiante in estudiantes:
    print(f"  {estudiante[0]}: {estudiante[1:]}")

# Calcular promedio por estudiante
print("\nPromedio por estudiante:")
for estudiante in estudiantes:
    nombre = estudiante[0]
    calificaciones = estudiante[1:]
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"  {nombre}: {promedio:.2f}")




# SECCIÓN 15: MEJORES PRÁCTICAS
imprimir_seccion("MEJORES PRÁCTICAS AL TRABAJAR CON LISTAS DE LISTAS")

print("""
1. Usar nombres descriptivos
   - lista_series en lugar de ls
   - datos_estudiantes en lugar de d
   - Documentar la estructura de tus datos, especialmente cuando son complejos

2. Al recorrer listas de listas:
   - Usar nombres significativos para las variables:
     • for serie in series_tv:
     • for estudiante in datos_estudiantes:

4. Al buscar en listas de listas:
   - Usar comprensiones de listas para filtrar:
     • series_comedia = [serie for serie in series if "Comedia" in serie[5]]
   - Crear funciones auxiliares para búsquedas complejas

5. Para evitar errores comunes:
   - Verificar siempre la estructura antes de acceder a elementos anidados
   - Usar try/except para manejar casos como índices inexistentes
   - Hacer copias profundas (deepcopy) cuando se modifiquen estructuras anidadas

6. Para mejorar el rendimiento y mantenibilidad:
   - Considerar usar pandas para datos tabulares grandes
   - Migrar a clases personalizadas cuando la estructura sea muy compleja
   - Usar diccionarios cuando el acceso por posición se vuelve confuso
""")


# Conclusión
imprimir_seccion("CONCLUSIÓN")

print("""
Hemos completado un repaso completo de listas y listas de listas en Python:

- Las listas simples son colecciones ordenadas y mutables de elementos
- Las listas de listas permiten estructurar datos más complejos y jerárquicos
- Son ideales para representar tablas de información, registros y datos estructurados
- Con ellas puedes modelar colecciones con elementos heterogéneos y anidados

Para casos más complejos o grandes volúmenes de datos, considera usar:
- Diccionarios o clases personalizadas para mayor claridad
- Pandas para análisis de datos con funcionalidades avanzadas
- Collections como namedtuple para estructuras más eficientes

¡Practica estos conceptos para dominarlos completamente!
""")
