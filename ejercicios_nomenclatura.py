#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicios de Práctica: La importancia de nombrar correctamente las variables
Autor: Diego
Fecha: 15 de mayo de 2025
"""

def imprimir_encabezado(titulo, numero):
    """Imprime un encabezado para cada ejercicio."""
    print(f"\n{'=' * 60}")
    print(f"EJERCICIO {numero}: {titulo}")
    print(f"{'=' * 60}")


def ejercicio_1():
    imprimir_encabezado("REFACTORIZAR CÓDIGO CON NOMBRES POCO DESCRIPTIVOS", 1)
    
    print("""
Instrucciones:
--------------
1. Observa el siguiente código que calcula el área y perímetro de un rectángulo
2. Identifica los problemas con los nombres de variables
3. Reescribe el código usando nombres descriptivos
4. Ejecuta ambas versiones y compara su legibilidad

Código original:
""")
    
    # Ejemplo con nombres poco descriptivos
    print("# Versión con nombres poco descriptivos:")
    print("a = 10")
    print("b = 20")
    print("c = a * b")
    print("d = 2 * (a + b)")
    print("print(f'c = {c}')")
    print("print(f'd = {d}')")
    
    # Ejecución del código poco descriptivo
    print("\n# Resultado:")
    a = 10
    b = 20
    c = a * b
    d = 2 * (a + b)
    print(f'c = {c}')
    print(f'd = {d}')
    
    print("\nTu solución (ejemplo):")
    print("# Versión con nombres descriptivos:")
    print("longitud_rectangulo = 10")
    print("ancho_rectangulo = 20")
    print("area_rectangulo = longitud_rectangulo * ancho_rectangulo")
    print("perimetro_rectangulo = 2 * (longitud_rectangulo + ancho_rectangulo)")
    print("print(f'Área del rectángulo = {area_rectangulo} unidades cuadradas')")
    print("print(f'Perímetro del rectángulo = {perimetro_rectangulo} unidades')")
    
    # Ejecución del código descriptivo
    print("\n# Resultado:")
    longitud_rectangulo = 10
    ancho_rectangulo = 20
    area_rectangulo = longitud_rectangulo * ancho_rectangulo
    perimetro_rectangulo = 2 * (longitud_rectangulo + ancho_rectangulo)
    print(f'Área del rectángulo = {area_rectangulo} unidades cuadradas')
    print(f'Perímetro del rectángulo = {perimetro_rectangulo} unidades')


def ejercicio_2():
    imprimir_encabezado("BUCLE FOR CON LISTA DE DICCIONARIOS", 2)
    
    print("""
Instrucciones:
--------------
1. Observa el siguiente código que procesa una lista de estudiantes
2. Identifica los problemas con los nombres de variables
3. Reescribe el código usando nombres descriptivos
4. Piensa en cómo afecta a la claridad cuando hay estructuras anidadas

Código original:
""")
      # Ejemplo con nombres poco descriptivos    print("# Versión con nombres poco descriptivos:")
    print("l = [")
    print("    {\"n\": \"Ana\", \"e\": 22, \"c\": [\"Mat\", \"Fis\", \"Qui\"]},")
    print("    {\"n\": \"Juan\", \"e\": 19, \"c\": [\"His\", \"Geo\", \"Ing\"]},")
    print("    {\"n\": \"Maria\", \"e\": 20, \"c\": [\"Bio\", \"Mat\", \"Ing\"]}")
    print("]")
    print("")
    print("for i in l:")
    print("    print(f\"Nombre: {i['n']}, Edad: {i['e']}\")")
    print("    print(\"Cursos:\")")
    print("    for j in i['c']:")
    print("        print(f\"  - {j}\")")
    print("    print()")
    
    # Ejecución del código poco descriptivo
    print("\n# Resultado:")
    l = [
        {"n": "Ana", "e": 22, "c": ["Mat", "Fis", "Qui"]},
        {"n": "Juan", "e": 19, "c": ["His", "Geo", "Ing"]},
        {"n": "Maria", "e": 20, "c": ["Bio", "Mat", "Ing"]}
    ]
    
    for i in l:
        print(f"Nombre: {i['n']}, Edad: {i['e']}")
        print("Cursos:")
        for j in i['c']:
            print(f"  - {j}")
        print()
    print("\nTu solución (ejemplo):")
    print("# Versión con nombres descriptivos:")
    print("estudiantes = [")
    print("    {\"nombre\": \"Ana\", \"edad\": 22, \"cursos\": [\"Matemáticas\", \"Física\", \"Química\"]},")
    print("    {\"nombre\": \"Juan\", \"edad\": 19, \"cursos\": [\"Historia\", \"Geografía\", \"Inglés\"]},")
    print("    {\"nombre\": \"Maria\", \"edad\": 20, \"cursos\": [\"Biología\", \"Matemáticas\", \"Inglés\"]}")
    print("]")
    print("")
    print("for estudiante in estudiantes:")
    print("    print(f\"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}\")")
    print("    print(\"Cursos:\")")
    print("    for nombre_curso in estudiante['cursos']:")
    print("        print(f\"  - {nombre_curso}\")")
    print("    print()")
    
    # Ejecución del código descriptivo
    print("\n# Resultado:")
    estudiantes = [
        {"nombre": "Ana", "edad": 22, "cursos": ["Matemáticas", "Física", "Química"]},
        {"nombre": "Juan", "edad": 19, "cursos": ["Historia", "Geografía", "Inglés"]},
        {"nombre": "Maria", "edad": 20, "cursos": ["Biología", "Matemáticas", "Inglés"]}
    ]
    
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
        print("Cursos:")
        for nombre_curso in estudiante['cursos']:
            print(f"  - {nombre_curso}")
        print()


def ejercicio_3():
    imprimir_encabezado("BUCLE WHILE PARA SIMULAR UN PROCESO", 3)
    
    print("""
Instrucciones:
--------------
1. Observa el siguiente código que simula un proceso de carga
2. Identifica los problemas con los nombres de variables
3. Reescribe el código usando nombres descriptivos
4. ¿Cómo mejora la comprensión del algoritmo con buenos nombres?

Código original:
""")
    
    # Ejemplo con nombres poco descriptivos    print("# Versión con nombres poco descriptivos:")
    print("import time")
    print("")
    print("x = 0")
    print("y = 10")
    print("z = False")
    print("")
    print("while x < y:")
    print("    x += 1")
    print("    p = x * 10")
    print("    print(f\"Progreso: {p}%\")")
    print("    if x == y:")
    print("        z = True")
    print("    time.sleep(0.1)  # Simular tiempo de procesamiento")
    print("")
    print("if z:")
    print("    print(\"¡Proceso completado!\")")
    print("else:")
    print("    print(\"Proceso interrumpido\")")
    
    print("\nTu solución (ejemplo):")    
    print("# Versión con nombres descriptivos:")
    print("import time")
    print("")
    print("progreso_actual = 0")
    print("total_pasos = 10")
    print("proceso_completado = False")
    print("")
    print("while progreso_actual < total_pasos:")
    print("    progreso_actual += 1")
    print("    porcentaje_completado = progreso_actual * 10")
    print("    print(f\"Progreso: {porcentaje_completado}%\")")
    print("    if progreso_actual == total_pasos:")
    print("        proceso_completado = True")
    print("    time.sleep(0.1)  # Simular tiempo de procesamiento")
    print("")
    print("if proceso_completado:")
    print("    print(\"¡Proceso completado!\")")
    print("else:")
    print("    print(\"Proceso interrumpido\")")


def ejercicio_4():
    imprimir_encabezado("BUCLES ANIDADOS CON MATRICES", 4)
    
    print("""
Instrucciones:
--------------
1. Observa el siguiente código que procesa una matriz de datos
2. Identifica los problemas con los nombres de variables
3. Reescribe el código usando nombres descriptivos
4. Ejecuta ambas versiones y compara su legibilidad

Código original:
""")
    
    # Ejemplo con nombres poco descriptivos
    print("""# Versión con nombres poco descriptivos:
m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

r = []
for i in range(len(m)):
    s = 0
    for j in range(len(m[i])):
        if m[i][j] % 2 == 0:  # Si es par
            s += m[i][j]
    r.append(s)

print(f"r = {r}")
""")
    
    # Ejecución del código poco descriptivo
    print("\n# Resultado:")
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    r = []
    for i in range(len(m)):
        s = 0
        for j in range(len(m[i])):
            if m[i][j] % 2 == 0:  # Si es par
                s += m[i][j]
        r.append(s)
    
    print(f"r = {r}")
    
    print("\nTu solución (ejemplo):")
    print("""# Versión con nombres descriptivos:
matriz_numeros = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

suma_pares_por_fila = []
for indice_fila in range(len(matriz_numeros)):
    suma_numeros_pares = 0
    for indice_columna in range(len(matriz_numeros[indice_fila])):
        numero_actual = matriz_numeros[indice_fila][indice_columna]
        if numero_actual % 2 == 0:  # Si es par
            suma_numeros_pares += numero_actual
    suma_pares_por_fila.append(suma_numeros_pares)

print(f"Suma de números pares por fila: {suma_pares_por_fila}")
""")
    
    # Ejecución del código descriptivo
    print("\n# Resultado:")
    matriz_numeros = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    suma_pares_por_fila = []
    for indice_fila in range(len(matriz_numeros)):
        suma_numeros_pares = 0
        for indice_columna in range(len(matriz_numeros[indice_fila])):
            numero_actual = matriz_numeros[indice_fila][indice_columna]
            if numero_actual % 2 == 0:  # Si es par
                suma_numeros_pares += numero_actual
        suma_pares_por_fila.append(suma_numeros_pares)
    
    print(f"Suma de números pares por fila: {suma_pares_por_fila}")


def ejercicio_5():
    imprimir_encabezado("FUNCIONES CON NOMBRES DE PARÁMETROS", 5)
    
    print("""
Instrucciones:
--------------
1. Observa las siguientes funciones que calculan el precio final de un producto
2. Identifica los problemas con los nombres de variables y parámetros
3. Reescribe las funciones usando nombres descriptivos
4. ¿Por qué es especialmente importante tener buenos nombres en funciones?

Código original:
""")
    
    # Ejemplo con nombres poco descriptivos
    print("""# Versión con nombres poco descriptivos:
def calc(p, d, t):
    Calcula algo relacionado con precios
    a = p - (p * d / 100)
    b = a * (t / 100)
    c = a + b
    return c

# Uso de la función
res = calc(1000, 20, 16)
print(f"Resultado: {res}")
""")
    
    # Ejecución del código poco descriptivo
    def calc(p, d, t):
        """Calcula algo relacionado con precios."""
        a = p - (p * d / 100)
        b = a * (t / 100)
        c = a + b
        return c
    
    # Uso de la función con nombres poco descriptivos
    print("\n# Resultado:")
    res = calc(1000, 20, 16)
    print(f"Resultado: {res}")
    
    print("\nTu solución (ejemplo):")
    print("""# Versión con nombres descriptivos:
def calcular_precio_final(precio_base, porcentaje_descuento, porcentaje_impuesto):

    Calcula el precio final de un producto aplicando descuento e impuestos.
    
    Args:
        precio_base: El precio original del producto
        porcentaje_descuento: El porcentaje de descuento a aplicar
        porcentaje_impuesto: El porcentaje de impuesto a aplicar
    
    Returns:
        El precio final después de aplicar descuento e impuestos

    precio_con_descuento = precio_base - (precio_base * porcentaje_descuento / 100)
    valor_impuesto = precio_con_descuento * (porcentaje_impuesto / 100)
    precio_final = precio_con_descuento + valor_impuesto
    return precio_final

# Uso de la función
precio_final = calcular_precio_final(1000, 20, 16)
print(f"Precio final: ${precio_final}")
""")
    
    # Ejecución del código descriptivo
    def calcular_precio_final(precio_base, porcentaje_descuento, porcentaje_impuesto):
        """
        Calcula el precio final de un producto aplicando descuento e impuestos.
        
        Args:
            precio_base: El precio original del producto
            porcentaje_descuento: El porcentaje de descuento a aplicar
            porcentaje_impuesto: El porcentaje de impuesto a aplicar
        
        Returns:
            El precio final después de aplicar descuento e impuestos
        """
        precio_con_descuento = precio_base - (precio_base * porcentaje_descuento / 100)
        valor_impuesto = precio_con_descuento * (porcentaje_impuesto / 100)
        precio_final = precio_con_descuento + valor_impuesto
        return precio_final
    
    # Uso de la función con nombres descriptivos
    print("\n# Resultado:")
    precio_final = calcular_precio_final(1000, 20, 16)
    print(f"Precio final: ${precio_final}")


def ejercicio_6():
    imprimir_encabezado("DESAFÍO: CÓDIGO REAL CON PROBLEMAS DE NOMENCLATURA", 6)
    
    print("""
Instrucciones:
--------------
1. A continuación se presenta un algoritmo de filtrado y procesamiento de datos
2. El código funciona pero tiene serios problemas de nomenclatura
3. Tu tarea es reescribir el código completo con nombres significativos
4. Incluye comentarios que expliquen la lógica del algoritmo

Código original:
""")
    
    # Ejemplo con nombres poco descriptivos
    print("""# Versión con nombres poco descriptivos:
def f(d, m, t):
    r = []
    for i in d:
        if i["c"] >= m and i["s"] == t:
            r.append(i)
    
    s = 0
    for i in r:
        s += i["v"]
    
    if len(r) > 0:
        p = s / len(r)
    else:
        p = 0
    
    return {
        "f": r,
        "t": s,
        "p": p,
        "n": len(r)
    }

# Datos de ejemplo
x = [
    {"i": 1, "c": 25, "s": "A", "v": 100},
    {"i": 2, "c": 30, "s": "B", "v": 200},
    {"i": 3, "c": 18, "s": "A", "v": 150},
    {"i": 4, "c": 40, "s": "A", "v": 300},
    {"i": 5, "c": 35, "s": "B", "v": 250}
]

# Uso de la función
z = f(x, 20, "A")
print(z)
""")
    
    # Ejecución del código poco descriptivo
    def f(d, m, t):
        r = []
        for i in d:
            if i["c"] >= m and i["s"] == t:
                r.append(i)
        
        s = 0
        for i in r:
            s += i["v"]
        
        if len(r) > 0:
            p = s / len(r)
        else:
            p = 0
        
        return {
            "f": r,
            "t": s,
            "p": p,
            "n": len(r)
        }
    
    # Datos de ejemplo con nombres poco descriptivos
    print("\n# Resultado:")
    x = [
        {"i": 1, "c": 25, "s": "A", "v": 100},
        {"i": 2, "c": 30, "s": "B", "v": 200},
        {"i": 3, "c": 18, "s": "A", "v": 150},
        {"i": 4, "c": 40, "s": "A", "v": 300},
        {"i": 5, "c": 35, "s": "B", "v": 250}
    ]
    
    # Uso de la función con nombres poco descriptivos
    z = f(x, 20, "A")
    print(z)
    
    print("\nTu solución (completa por tu cuenta):")
    print("""# Versión con nombres descriptivos:
def filtrar_y_analizar_productos(lista_productos, calificacion_minima, tipo_producto):
    \"\"\"
    Filtra productos por calificación mínima y tipo, y calcula estadísticas.
    
    Args:
        lista_productos: Lista de diccionarios con datos de productos
        calificacion_minima: Calificación mínima para filtrar productos
        tipo_producto: Tipo de producto a filtrar
        
    Returns:
        Diccionario con productos filtrados y estadísticas
    \"\"\"
    # Paso 1: Filtrar productos que cumplen los criterios
    productos_filtrados = []
    for producto in lista_productos:
        if producto["calificacion"] >= calificacion_minima and producto["tipo"] == tipo_producto:
            productos_filtrados.append(producto)
    
    # Paso 2: Calcular la suma total de ventas
    suma_ventas = 0
    for producto in productos_filtrados:
        suma_ventas += producto["ventas"]
    
    # Paso 3: Calcular el promedio de ventas
    if len(productos_filtrados) > 0:
        promedio_ventas = suma_ventas / len(productos_filtrados)
    else:
        promedio_ventas = 0
    
    # Paso 4: Retornar resultados y estadísticas
    return {
        "productos_filtrados": productos_filtrados,
        "total_ventas": suma_ventas,
        "promedio_ventas": promedio_ventas,
        "numero_productos": len(productos_filtrados)
    }

# Datos de ejemplo
productos = [
    {"id": 1, "calificacion": 25, "tipo": "A", "ventas": 100},
    {"id": 2, "calificacion": 30, "tipo": "B", "ventas": 200},
    {"id": 3, "calificacion": 18, "tipo": "A", "ventas": 150},
    {"id": 4, "calificacion": 40, "tipo": "A", "ventas": 300},
    {"id": 5, "calificacion": 35, "tipo": "B", "ventas": 250}
]

# Uso de la función
resultados = filtrar_y_analizar_productos(productos, 20, "A")
print(resultados)
""")


def instrucciones_entrega():
    print(f"\n{'=' * 60}")
    print("INSTRUCCIONES PARA COMPLETAR Y ENTREGAR LOS EJERCICIOS")
    print(f"{'=' * 60}")
    
    print("""
Para sacar el máximo provecho de estos ejercicios:

1. Completa cada ejercicio en una hoja aparte o en un editor de código

2. Para cada ejercicio:
   - Analiza primero el código con nombres poco descriptivos
   - Identifica los problemas específicos
   - Reescribe el código con nombres descriptivos
   - Ejecuta ambas versiones y compara resultados

3. Reflexiona sobre estas preguntas:
   - ¿Cómo cambió tu comprensión del código con mejores nombres?
   - ¿Cuánto tiempo te tomó entender el propósito del código original?
   - ¿Qué convenciones de nomenclatura decidiste seguir?
   - ¿Cómo elegiste los nombres para las variables más complejas?

4. Comparte tu código mejorado con compañeros para obtener feedback
   - ¿Tus compañeros pueden entender el propósito del código sin explicaciones?
   - ¿Hay mejores nombres que podrían haber elegido?

5. Para el ejercicio 6 (desafío):
   - Intenta primero entender qué hace el código sin cambiar los nombres
   - Luego renombra todas las variables con nombres descriptivos
   - Añade comentarios explicando el propósito de cada sección

¡RECUERDA!
Un buen nombre de variable es aquel que hace obvio su propósito
sin necesidad de comentarios adicionales.
""")


def main():
    print("\n🔤 EJERCICIOS PRÁCTICOS: IMPORTANCIA DE NOMBRAR VARIABLES 🔤\n")
    print("En este archivo encontrarás ejercicios para practicar y")
    print("reforzar la importancia de nombrar correctamente las variables.")
    print("\nCada ejercicio incluye:")
    print("  - Código con nombres de variables poco descriptivos")
    print("  - Espacio para tu solución")
    print("  - Un ejemplo de solución para comparar")
    
    while True:
        print("\nMenú de ejercicios:")
        print("1. Refactorizar código con nombres poco descriptivos")
        print("2. Bucle for con lista de diccionarios")
        print("3. Bucle while para simular un proceso")
        print("4. Bucles anidados con matrices")
        print("5. Funciones con nombres de parámetros")
        print("6. Desafío: código real con problemas de nomenclatura")
        print("7. Ver instrucciones de entrega")
        print("8. Salir")
        
        opcion = input("\nSelecciona un ejercicio (1-8): ")
        
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            instrucciones_entrega()
        elif opcion == "8":
            print("\n¡Gracias por practicar! Recuerda que un buen nombre de variable")
            print("es una forma de documentación que hace tu código más mantenible.")
            break
        else:
            print("\n⚠️ Opción inválida. Por favor, selecciona un número del 1 al 8.")


if __name__ == "__main__":
    main()
