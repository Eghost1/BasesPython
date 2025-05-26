'''
Para trabajar con archivos en Python, se usa la función `open()`. Modos comunes:
- "r": leer
- "w": escribir (sobrescribe)
- "a": agregar al final
- "r+": leer y escribir
'''
#ejemplo de lecrtura en un archivo
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()

#ejemplo de escritura en un archivo
archivo = open("salida.txt", "w")
archivo.write("Hola mundo\n")
archivo.write("Segunda linea\n")
archivo.close()


#Como leer un archivo línea por línea
archivo = open("datos.txt", "r")
for linea in archivo:
    print(linea.strip())  # .strip() elimina espacios en blanco al inicio y al final
# Cerrar el archivo después de usarlo
archivo.close()



#Escribir varias líneas en un archivo
archivo = open("salida.txt", "w")
#1.
lineas = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n"]
for linea in lineas:
    archivo.write(linea)
archivo.close()

#2. otra forma de escribir varias líneas
# Usando una lista de nombres y escribiéndolos en un archivo
nombres = ["Ana", "Luis", "Carla"]
archivo = open("nombres.txt", "w")
for nombre in nombres:
    archivo.write(nombre + "\n")
archivo.close()



#Ejercicio: Leer archivo y filtrar datos
'''Archivo: notas.txt
Contenido:
Juan 5.5
Ana 6.0
Pedro 4.1

Enunciado:
Mostrar nombres con nota mayor a 5.0
'''


'''
archivo = open("notas.txt", "r")
for linea in archivo:
    partes = linea.strip().split()
    nombre = partes[0]
    nota = float(partes[1])
    if nota > 5.0:
        print(nombre)
archivo.close()
'''


'''
EJERCICIO PRACTICO:
- Leer un archivo (notas_alumnos.txt) y contar cuántas líneas no están vacías.
- Escribir un archivo nuevo (nombres_largos.txt) con los nombres que contienen más de 4 letras.
- Escribir un archivo los alumnos que aprobaron en un archivo alumnos_aprobados.txt (la nota de aprobación es 5.0).
'''
# Contar líneas no vacías en un archivo
archivo = open("notas_alumnos.txt", "r")
contador_lineas = 0
for linea in archivo:
    if linea.strip():  # Verifica si la línea no está vacía
        contador_lineas += 1
archivo.close()
print(f"Número de líneas no vacías: {contador_lineas}")

# Escribir nombres largos en un nuevo archivo   
nombres_largos = []
archivo = open("notas_alumnos.txt", "r")
for linea in archivo:
    if linea.strip():  # Verifica si la línea no está vacía antes de dividirla
        partes = linea.strip().split()  # Divide la línea en partes
        if partes:  # Verifica que la lista no esté vacía después de dividir
            nombre = partes[0]  # Ahora es seguro acceder al primer elemento
            if len(nombre) > 4: # Verifica si el nombre tiene más de 4 letras
                nombres_largos.append(nombre) # Agrega el nombre a la lista
archivo.close()
archivo_nombres_largos = open("nombres_largos.txt", "w")
for nombre in nombres_largos:
    archivo_nombres_largos.write(nombre + "\n")
archivo_nombres_largos.close()


# Escribir alumnos aprobados en un nuevo archivo sin try # y except
# Leer archivo y filtrar alumnos aprobados
alumnos_aprobados = []
archivo = open("notas_alumnos.txt", "r")
for linea in archivo:
    if linea.strip():  # Verifica si la línea no está vacía
        partes = linea.strip().split()
        if len(partes) >= 2:  # Asegura que haya al menos nombre y nota strip.split() separa de modo [nombre, nota]
            nombre = partes[0]
            nota = float(partes[1])
            if nota >= 5.0:
                alumnos_aprobados.append(nombre)
archivo.close()

# Escribir alumnos aprobados en un nuevo archivo
archivo_aprobados = open("alumnos_aprobados.txt", "w")
for alumno in alumnos_aprobados:
    archivo_aprobados.write(alumno + "\n")
archivo_aprobados.close()


