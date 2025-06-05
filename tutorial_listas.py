#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tutorial de Listas en Python
Autor: Diego
Fecha: 4 de junio de 2025
"""

def imprimir_seccion(titulo):
    """Imprime un título de sección con formato para mejor visualización."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# PARTE 1: LISTAS BÁSICAS
# ============================================================================

def introduccion_listas():
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
    print(f"Lista por comprensión (cuadrados): {cuadrados}")
    
    pares = [x for x in range(1, 11) if x % 2 == 0]
    print(f"Lista por comprensión (números pares): {pares}")


def acceder_elementos_lista():
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


def modificar_listas():
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


def recorrer_listas():
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


def buscar_en_listas():
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


def ordenar_y_otras_operaciones():
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


def copiar_listas():
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
    import copy
    
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
# PARTE 2: LISTAS DE LISTAS (MATRICES)
# ============================================================================

def introduccion_listas_anidadas():
    imprimir_seccion("INTRODUCCIÓN A LISTAS ANIDADAS (MATRICES)")
    
    print("""
    Las listas anidadas son listas que contienen otras listas como elementos.
    Son útiles para representar estructuras multidimensionales como:
    - Matrices (tablas, cuadrículas)
    - Agrupaciones jerárquicas de datos
    - Grafos
    - Etc.
    """)
    
    # Crear listas anidadas (matrices)
    print("# Creación de una matriz 3x3:")
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Matriz:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Crear matriz por comprensión
    print("\n# Matriz 3x3 con valores por comprensión:")
    matriz_comp = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
    print(f"Matriz por comprensión:")
    for fila in matriz_comp:
        print(f"  {fila}")
    
    # Matriz irregular
    print("\n# Matriz irregular (filas de diferente longitud):")
    matriz_irregular = [
        [1, 2, 3, 4],
        [5, 6],
        [7, 8, 9]
    ]
    print(f"Matriz irregular:")
    for fila in matriz_irregular:
        print(f"  {fila}")


def acceder_elementos_matriz():
    imprimir_seccion("ACCEDER A ELEMENTOS EN MATRICES")
    
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Matriz:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Acceder por índices
    print("\n# Acceso por índices [fila][columna]:")
    print(f"Elemento en la posición [0][0]: {matriz[0][0]}")  # 1
    print(f"Elemento en la posición [1][2]: {matriz[1][2]}")  # 6
    print(f"Elemento en la posición [2][1]: {matriz[2][1]}")  # 8
    
    # Acceder a una fila completa
    print("\n# Acceso a una fila completa:")
    print(f"Primera fila [0]: {matriz[0]}")     # [1, 2, 3]
    print(f"Segunda fila [1]: {matriz[1]}")     # [4, 5, 6]
    
    # Acceder a una columna
    print("\n# Acceso a una columna (requiere iterar):")
    print("Primera columna [0]:")
    primera_columna = [fila[0] for fila in matriz]
    print(f"  {primera_columna}")  # [1, 4, 7]
    
    # Acceder a submatriz (slice)
    print("\n# Acceder a una submatriz:")
    print("Submatriz de las primeras 2 filas y 2 columnas:")
    submatriz = [fila[:2] for fila in matriz[:2]]
    for fila in submatriz:
        print(f"  {fila}")


def modificar_matrices():
    imprimir_seccion("MODIFICAR MATRICES")
    
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Matriz original:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Modificar un elemento
    print("\n# Modificar un elemento:")
    matriz[0][0] = 99
    matriz[1][1] = 55
    print("Después de modificar [0][0] y [1][1]:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Modificar una fila completa
    print("\n# Modificar una fila completa:")
    matriz[0] = [10, 20, 30]
    print("Después de cambiar la primera fila:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Añadir una nueva fila
    print("\n# Añadir una nueva fila:")
    matriz.append([11, 12, 13])
    print("Después de añadir una fila:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Eliminar una fila
    print("\n# Eliminar una fila:")
    matriz.pop(1)  # Elimina la segunda fila
    print("Después de eliminar la segunda fila:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Insertar una fila en una posición específica
    print("\n# Insertar una fila en una posición específica:")
    matriz.insert(1, [40, 50, 60])
    print("Después de insertar una fila en la posición 1:")
    for fila in matriz:
        print(f"  {fila}")


def recorrer_matrices():
    imprimir_seccion("RECORRER MATRICES")
    
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Matriz:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Recorrer por filas (método más común)
    print("\n# Recorrer por filas:")
    print("for fila in matriz:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Recorrer elemento por elemento con for anidados
    print("\n# Recorrer elemento por elemento:")
    print("for fila in matriz:")
    print("    for elemento in fila:")
    for fila in matriz:
        for elemento in fila:
            print(f"  {elemento}", end=" ")
        print()  # Salto de línea al final de cada fila
    
    # Recorrer con índices
    print("\n# Recorrer con índices:")
    print("for i in range(len(matriz)):")
    print("    for j in range(len(matriz[i])):")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"  matriz[{i}][{j}] = {matriz[i][j]}", end="  ")
        print()
    
    # Recorrer con enumerate
    print("\n# Recorrer con enumerate:")
    print("for i, fila in enumerate(matriz):")
    print("    for j, elemento in enumerate(fila):")
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            print(f"  [{i},{j}]={elemento}", end="  ")
        print()


def operaciones_matrices():
    imprimir_seccion("OPERACIONES CON MATRICES")
    
    matriz_A = [
        [1, 2],
        [3, 4]
    ]
    matriz_B = [
        [5, 6],
        [7, 8]
    ]
    print("Matriz A:")
    for fila in matriz_A:
        print(f"  {fila}")
    print("\nMatriz B:")
    for fila in matriz_B:
        print(f"  {fila}")
    
    # Suma de matrices
    print("\n# Suma de matrices (A + B):")
    suma = []
    for i in range(len(matriz_A)):
        fila_suma = []
        for j in range(len(matriz_A[i])):
            fila_suma.append(matriz_A[i][j] + matriz_B[i][j])
        suma.append(fila_suma)
    
    for fila in suma:
        print(f"  {fila}")
    
    # Multiplicación por escalar
    print("\n# Multiplicación por escalar (2 * A):")
    escalar = 2
    resultado = []
    for fila in matriz_A:
        fila_resultado = [escalar * elemento for elemento in fila]
        resultado.append(fila_resultado)
    
    for fila in resultado:
        print(f"  {fila}")
    
    # Multiplicación de matrices
    print("\n# Multiplicación de matrices (A * B):")
    filas_A = len(matriz_A)
    columnas_A = len(matriz_A[0])
    columnas_B = len(matriz_B[0])
    
    # Inicializar matriz resultado con ceros
    resultado = []
    for i in range(filas_A):
        resultado.append([0] * columnas_B)
    
    # Realizar multiplicación
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += matriz_A[i][k] * matriz_B[k][j]
    
    for fila in resultado:
        print(f"  {fila}")
    
    # Transpuesta de una matriz
    print("\n# Matriz transpuesta de A:")
    transpuesta = []
    for j in range(len(matriz_A[0])):
        fila_transpuesta = []
        for i in range(len(matriz_A)):
            fila_transpuesta.append(matriz_A[i][j])
        transpuesta.append(fila_transpuesta)
    
    for fila in transpuesta:
        print(f"  {fila}")


def ejemplos_practicos():
    imprimir_seccion("EJEMPLOS PRÁCTICOS")
    
    # Ejemplo 1: Suma de todos los elementos de una matriz
    print("# Ejemplo 1: Suma de todos los elementos de una matriz")
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    suma = 0
    for fila in matriz:
        suma += sum(fila)
    print(f"Matriz: {matriz}")
    print(f"Suma de todos los elementos: {suma}")
    
    # Forma alternativa con comprensión de listas
    suma_alt = sum(sum(fila) for fila in matriz)
    print(f"Suma (alternativa): {suma_alt}")
    
    # Ejemplo 2: Encontrar el valor máximo y su posición
    print("\n# Ejemplo 2: Encontrar el valor máximo y su posición")
    max_valor = matriz[0][0]
    max_pos = (0, 0)
    
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor > max_valor:
                max_valor = valor
                max_pos = (i, j)
    
    print(f"Matriz: {matriz}")
    print(f"Valor máximo: {max_valor}")
    print(f"Posición (fila, columna): {max_pos}")
    
    # Ejemplo 3: Filtrar valores pares e impares
    print("\n# Ejemplo 3: Filtrar valores pares e impares")
    pares = []
    impares = []
    
    for fila in matriz:
        for valor in fila:
            if valor % 2 == 0:
                pares.append(valor)
            else:
                impares.append(valor)
    
    print(f"Matriz: {matriz}")
    print(f"Valores pares: {pares}")
    print(f"Valores impares: {impares}")
    
    # Ejemplo 4: Tabla de multiplicar como matriz
    print("\n# Ejemplo 4: Tabla de multiplicar como matriz")
    n = 5
    tabla_multiplicar = []
    for i in range(1, n+1):
        fila = []
        for j in range(1, n+1):
            fila.append(i * j)
        tabla_multiplicar.append(fila)
    
    print(f"Tabla de multiplicar {n}x{n}:")
    for fila in tabla_multiplicar:
        print(f"  {fila}")


def casos_uso_avanzados():
    imprimir_seccion("CASOS DE USO AVANZADOS")
    
    # Representación de un tablero de juego (tic-tac-toe)
    print("# Ejemplo 1: Tablero de juego (tic-tac-toe)")
    tablero = [
        ["X", "O", " "],
        [" ", "X", " "],
        ["O", " ", "X"]
    ]
    print("Tablero de juego:")
    for fila in tablero:
        print(f"  | {fila[0]} | {fila[1]} | {fila[2]} |")
    
    # Representación de datos tabulares
    print("\n# Ejemplo 2: Datos tabulares (estudiantes y calificaciones)")
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
    
    # Matriz dispersa (la mayoría de elementos son cero)
    print("\n# Ejemplo 3: Representación eficiente de matriz dispersa")
    # Representación densa (poco eficiente para matrices dispersas)
    matriz_densa = [
        [0, 0, 0, 5, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    
    print("Matriz densa:")
    for fila in matriz_densa:
        print(f"  {fila}")
    
    # Representación eficiente (solo elementos no cero)
    matriz_dispersa = {
        (0, 3): 5,
        (1, 2): 3,
        (3, 1): 2,
        (4, 0): 1
    }
    
    print("\nRepresentación eficiente (solo elementos no cero):")
    print(f"  {matriz_dispersa}")
    
    # Reconstruir la matriz desde la representación dispersa
    filas = 5
    columnas = 5
    matriz_reconstruida = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz_dispersa.get((i, j), 0))
        matriz_reconstruida.append(fila)
    
    print("\nReconstrucción de la matriz dispersa:")
    for fila in matriz_reconstruida:
        print(f"  {fila}")


def mejores_practicas():
    imprimir_seccion("MEJORES PRÁCTICAS AL TRABAJAR CON LISTAS Y MATRICES")
    
    print("""
    1. Usar nombres descriptivos
       - lista_estudiantes en lugar de l
       - matriz_calificaciones en lugar de m
    
    2. Al recorrer listas:
       - Preferir 'for elemento in lista' cuando solo necesitas los valores
       - Usar enumerate cuando necesitas índices: 'for i, valor in enumerate(lista)'
       - Evitar 'for i in range(len(lista))' a menos que sea necesario
    
    3. Para matrices:
       - Mantener todas las filas con la misma longitud (matrices regulares)
       - Documentar la estructura cuando se usan matrices irregulares
       - Considerar usar NumPy para operaciones matemáticas avanzadas con matrices
    
    4. Al buscar elementos:
       - Usar 'if elemento in lista' para verificar existencia
       - Usar lista.index() para encontrar posiciones
       - Crear funciones auxiliares para búsquedas complejas
    
    5. Para evitar errores comunes:
       - Verificar índices antes de acceder a elementos
       - Usar try/except para manejar casos como listas vacías
       - Hacer copias profundas (deepcopy) cuando sea necesario
    
    6. Para mejorar el rendimiento:
       - Considerar estructuras de datos alternativas para operaciones específicas
         (conjuntos para búsquedas rápidas, diccionarios para acceso por clave)
       - Para matrices grandes, utilizar NumPy que es mucho más eficiente
    """)


def numpy_intro():
    imprimir_seccion("INTRODUCCIÓN A NUMPY PARA MATRICES (OPCIONAL)")
    
    try:
        import numpy as np
        print("""
    NumPy ofrece una alternativa más eficiente y poderosa para trabajar con matrices.
    Si trabajas frecuentemente con matrices, considera usar NumPy.
        """)
        
        print("# Ejemplos básicos de NumPy:")
        # Crear matriz
        matriz_np = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        print(f"Matriz NumPy:\n{matriz_np}")
        
        # Operaciones
        print(f"\nSuma de todos los elementos: {np.sum(matriz_np)}")
        print(f"Valor máximo: {np.max(matriz_np)}")
        print(f"Valor mínimo: {np.min(matriz_np)}")
        print(f"Media: {np.mean(matriz_np)}")
        
        # Acceso a filas y columnas
        print(f"\nPrimera fila: {matriz_np[0]}")
        print(f"Primera columna: {matriz_np[:, 0]}")
        
        # Operaciones matriciales
        print(f"\nTranspuesta:\n{matriz_np.transpose()}")
        print(f"Matriz * 2:\n{matriz_np * 2}")
        
    except ImportError:
        print("""
    NumPy no está instalado en tu sistema. Si quieres experimentar con matrices
    de manera más eficiente, puedes instalarlo con:
    
    pip install numpy
    
    NumPy proporciona un objeto array multidimensional y funciones sofisticadas
    para trabajar con estos arrays, lo que lo hace ideal para computación científica.
        """)


def main():
    print("\n🐍 TUTORIAL COMPLETO DE LISTAS Y MATRICES EN PYTHON 🐍\n")
    
    print("""
    Este tutorial está dividido en dos partes principales:
    1. Listas básicas: creación, acceso, modificación, recorrido, etc.
    2. Listas de listas (matrices): operaciones específicas y patrones de uso.
    
    Puedes avanzar sección por sección presionando Enter.
    """)
    input("\nPresiona Enter para comenzar con listas básicas...")
    
    # Parte 1: Listas básicas
    introduccion_listas()
    input("\nPresiona Enter para continuar...")
    
    acceder_elementos_lista()
    input("\nPresiona Enter para continuar...")
    
    modificar_listas()
    input("\nPresiona Enter para continuar...")
    
    recorrer_listas()
    input("\nPresiona Enter para continuar...")
    
    buscar_en_listas()
    input("\nPresiona Enter para continuar...")
    
    ordenar_y_otras_operaciones()
    input("\nPresiona Enter para continuar...")
    
    copiar_listas()
    input("\nPresiona Enter para continuar con matrices (listas de listas)...")
    
    # Parte 2: Matrices
    introduccion_listas_anidadas()
    input("\nPresiona Enter para continuar...")
    
    acceder_elementos_matriz()
    input("\nPresiona Enter para continuar...")
    
    modificar_matrices()
    input("\nPresiona Enter para continuar...")
    
    recorrer_matrices()
    input("\nPresiona Enter para continuar...")
    
    operaciones_matrices()
    input("\nPresiona Enter para continuar...")
    
    ejemplos_practicos()
    input("\nPresiona Enter para continuar...")
    
    casos_uso_avanzados()
    input("\nPresiona Enter para continuar...")
    
    mejores_practicas()
    input("\nPresiona Enter para finalizar con información sobre NumPy...")
    
    numpy_intro()
    
    print("\n🎉 ¡Felicidades! Has completado el tutorial completo sobre listas y matrices.")
    print("   Ahora tienes un conocimiento sólido de cómo trabajar con estas estructuras de datos.")
    print("   Practica estos conceptos para dominarlos completamente.")


if __name__ == "__main__":
    main()
