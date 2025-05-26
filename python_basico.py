#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tutorial Básico de Python: La importancia de nombrar correctamente las variables
Autor: Diego
Fecha: 14 de mayo de 2025
"""

def imprimir_seccion(titulo):
    """Imprime un título de sección con formato para mejor visualización."""
    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)


def ejemplo_variables():
    imprimir_seccion("1. VARIABLES Y NOMBRES DESCRIPTIVOS")
    
    # Ejemplo de nombres de variables poco descriptivos
    print("⚠️  Nombres poco descriptivos:")
    x = 10
    y = 20
    z = x + y
    print(f"x = {x}, y = {y}, z = x + y = {z}")
    
    # Ejemplo de nombres de variables descriptivos
    print("\n✅ Nombres descriptivos:")
    edad_estudiante = 10
    anos_experiencia = 20
    edad_total = edad_estudiante + anos_experiencia
    print(f"edad_estudiante = {edad_estudiante}")
    print(f"anos_experiencia = {anos_experiencia}")
    print(f"edad_total = edad_estudiante + anos_experiencia = {edad_total}")
    
    print("\n💡 CONSEJO: Usar nombres descriptivos hace que el código sea:")
    print("  - Más fácil de entender")
    print("  - Más fácil de mantener")
    print("  - Menos propenso a errores")


def ejemplo_bucle_for_malo():
    imprimir_seccion("2. BUCLES FOR: NOMBRES POCO DESCRIPTIVOS")
    
    print("⚠️  Ejemplo con nombres poco descriptivos:")
    
    # Lista de temperaturas diarias
    l = [22, 24, 19, 21, 25, 23, 20]
    
    # Mal ejemplo: variables poco descriptivas
    print("Temperaturas por encima de 22°C:")
    for i in l:
        if i > 22:
            print(f"  {i}°C")
    
    # ¿Qué significa i? ¿Qué representa l?
    # Difícil de entender sin contexto


def ejemplo_bucle_for_bueno():
    imprimir_seccion("3. BUCLES FOR: NOMBRES DESCRIPTIVOS")
    
    print("✅ Ejemplo con nombres descriptivos:")
    
    # Lista de temperaturas diarias
    temperaturas_semana = [22, 24, 19, 21, 25, 23, 20]
    
    # Buen ejemplo: variables descriptivas
    print("Temperaturas por encima de 22°C:")
    for temperatura in temperaturas_semana:
        if temperatura > 22:
            print(f"  {temperatura}°C")
    
    # Utilizando índices cuando es necesario
    print("\nDía a día:")
    for indice, temperatura in enumerate(temperaturas_semana, start=1):
        print(f"  Día {indice}: {temperatura}°C")


def ejemplo_bucle_while_malo():
    imprimir_seccion("4. BUCLES WHILE: NOMBRES POCO DESCRIPTIVOS")
    
    print("⚠️  Ejemplo con nombres poco descriptivos:")
    
    # Simulación de intentos de conexión
    x = 0
    m = 5
    
    while x < m:
        x += 1
        print(f"  Intento {x}: {'Exitoso' if x == 3 else 'Fallido'}")
        if x == 3:
            break
    
    # ¿Qué es x? ¿Qué representa m?
    # Código difícil de mantener


def ejemplo_bucle_while_bueno():
    imprimir_seccion("5. BUCLES WHILE: NOMBRES DESCRIPTIVOS")
    
    print("✅ Ejemplo con nombres descriptivos:")
    
    # Simulación de intentos de conexión
    intentos_realizados = 0
    max_intentos = 5
    
    while intentos_realizados < max_intentos:
        intentos_realizados += 1
        exito = intentos_realizados == 3  # Simulamos éxito en el tercer intento
        
        print(f"  Intento {intentos_realizados}: {'Exitoso' if exito else 'Fallido'}")
        
        if exito:
            print("  ¡Conexión establecida! Saliendo del bucle.")
            break
    else:
        print("  Se alcanzó el número máximo de intentos sin éxito.")


def ejemplo_bucle_anidado_malo():
    imprimir_seccion("6. BUCLES ANIDADOS: NOMBRES POCO DESCRIPTIVOS")
    
    print("⚠️  Ejemplo con nombres poco descriptivos:")
    
    # Matriz de datos
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Mal ejemplo: variables i, j son poco descriptivas
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"  m[{i}][{j}] = {m[i][j]}", end=' ')
        print()


def ejemplo_bucle_anidado_bueno():
    imprimir_seccion("7. BUCLES ANIDADOS: NOMBRES DESCRIPTIVOS")
    
    print("✅ Ejemplo con nombres descriptivos:")
    
    # Matriz de calificaciones por estudiante y asignatura
    calificaciones = [
        [85, 90, 78],  # Estudiante 1: Matemáticas, Ciencias, Historia
        [92, 88, 95],  # Estudiante 2: Matemáticas, Ciencias, Historia
        [76, 82, 89]   # Estudiante 3: Matemáticas, Ciencias, Historia
    ]
    
    materias = ["Matemáticas", "Ciencias", "Historia"]
    
    # Buen ejemplo: variables descriptivas
    for num_estudiante, notas_estudiante in enumerate(calificaciones, start=1):
        print(f"\n  Estudiante {num_estudiante}:")
        for indice_materia, calificacion in enumerate(notas_estudiante):
            nombre_materia = materias[indice_materia]
            print(f"    {nombre_materia}: {calificacion}")


def ejercicio_practico():
    imprimir_seccion("8. EJERCICIO PRÁCTICO")
    
    print("Revisemos lo aprendido con un ejercicio:")
    print("""
1. Modifica el siguiente código para usar nombres de variables descriptivos:

```python
d = {"a": 10, "b": 20, "c": 30}
s = 0
for k in d:
    s += d[k]
    print(f"k = {k}, v = {d[k]}, s = {s}")
```

2. Mejora este bucle while:

```python
i = 0
m = 100
while i < m:
    i += 10
    print(f"i = {i}")
```
    """)


def resumen():
    imprimir_seccion("RESUMEN: BUENAS PRÁCTICAS DE NOMENCLATURA")
    
    print("""
✅ RECOMENDACIONES:

1. Usa nombres descriptivos que expliquen QUÉ hace la variable.
   - temperatura_actual vs. t
   - contador_estudiantes vs. c
   - precio_total vs. pt

2. En bucles for:
   - Para colecciones: usar plurales para la colección y singular para el elemento
     • for estudiante in estudiantes:
     • for producto in lista_productos:

3. En bucles while:
   - Usar variables que expliquen la condición de salida
     • while intentos_realizados < max_intentos:
     • while tiempo_actual < tiempo_limite:

4. En índices cuando sean necesarios:
   - indice_estudiante, posicion_actual, num_fila son mejores que i, j, k

5. Convenciones en Python:
   - snake_case para variables y funciones (palabras_separadas_por_guiones_bajos)
   - MAYUSCULAS para constantes (MAX_INTENTOS = 5)
   - CamelCase para clases (class EstudianteUniversitario:)

💡 RECUERDA: El código se lee muchas más veces de las que se escribe.
    Un buen nombre de variable es una forma de documentación.
""")


def main():
    print("\n🐍 TUTORIAL DE PYTHON: IMPORTANCIA DE NOMBRAR VARIABLES 🐍\n")
    input("Presiona Enter para comenzar...\n")
    
    ejemplo_variables()
    input("\nPresiona Enter para continuar...")
    
    ejemplo_bucle_for_malo()
    input("\nPresiona Enter para continuar...")
    
    ejemplo_bucle_for_bueno()
    input("\nPresiona Enter para continuar...")
    
    ejemplo_bucle_while_malo()
    input("\nPresiona Enter para continuar...")
    
    ejemplo_bucle_while_bueno()
    input("\nPresiona Enter para continuar...")
    
    ejemplo_bucle_anidado_malo()
    input("\nPresiona Enter para continuar...")
    
    ejemplo_bucle_anidado_bueno()
    input("\nPresiona Enter para continuar...")
    
    ejercicio_practico()
    input("\nPresiona Enter para ver las soluciones...")
    
    print("\n💡 SOLUCIONES AL EJERCICIO:")
    print("""
# Ejercicio 1 - Solución:
diccionario_valores = {"a": 10, "b": 20, "c": 30}
suma_total = 0
for clave in diccionario_valores:
    valor = diccionario_valores[clave]
    suma_total += valor
    print(f"clave = {clave}, valor = {valor}, suma_total = {suma_total}")

# Ejercicio 2 - Solución:
contador = 0
valor_maximo = 100
while contador < valor_maximo:
    contador += 10
    print(f"contador = {contador}")
""")
    
    input("\nPresiona Enter para ver el resumen...")
    resumen()
    
    print("\n🎉 ¡Felicidades! Has completado el tutorial básico de Python.")
    print("   Ahora entiendes por qué nombrar bien las variables es crucial,")
    print("   especialmente en bucles for y while.")


if __name__ == "__main__":
    main()
