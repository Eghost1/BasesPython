# =============================================================================
# PARTE 1: ESTRUCTURAS DE DATOS
# =============================================================================

# 1.1. Lista simple de géneros
generos = [
    "Acción", "Aventura", "Comedia", "Drama", "Ciencia Ficción", 
    "Terror", "Fantasía", "Animación", "Crimen", "Thriller", 
    "Romance", "Documental"
]

# 1.2. Lista de listas para películas: [título, año, duración, calificación, [géneros]]
peliculas = [
    ["El Padrino", 1972, 175, 9.2, ["Drama", "Crimen"]],
    ["Interestelar", 2014, 169, 8.6, ["Ciencia Ficción", "Aventura", "Drama"]],
    ["El Caballero Oscuro", 2008, 152, 9.0, ["Acción", "Crimen", "Drama"]],
    ["Pulp Fiction", 1994, 154, 8.9, ["Crimen", "Drama"]],
    ["El Rey León", 1994, 88, 8.5, ["Animación", "Aventura", "Drama"]],
    ["Matrix", 1999, 136, 8.7, ["Acción", "Ciencia Ficción"]],
    ["Parásitos", 2019, 132, 8.5, ["Drama", "Thriller", "Comedia"]],
    ["Todo en Todas Partes al Mismo Tiempo", 2022, 139, 8.0, ["Ciencia Ficción", "Comedia", "Acción"]],
    ["El Señor de los Anillos: La Comunidad del Anillo", 2001, 178, 8.8, ["Aventura", "Fantasía"]],
    ["Coco", 2017, 105, 8.4, ["Animación", "Aventura", "Comedia"]]
]

# 1.3. Lista de diccionarios para series
series = [
    {
        "titulo": "Breaking Bad",
        "año_inicio": 2008,
        "año_fin": 2013,
        "temporadas": 5,
        "episodios_total": 62,
        "calificacion": 9.5,
        "generos": ["Drama", "Crimen", "Thriller"],
        "estado": "Finalizada"
    },
    {
        "titulo": "Stranger Things",
        "año_inicio": 2016,
        "año_fin": 2025,  # Suponiendo que continúa hasta 2025
        "temporadas": 5,
        "episodios_total": 42,
        "calificacion": 8.7,
        "generos": ["Drama", "Fantasía", "Terror"],
        "estado": "En emisión"
    },
    {
        "titulo": "The Office",
        "año_inicio": 2005,
        "año_fin": 2013,
        "temporadas": 9,
        "episodios_total": 201,
        "calificacion": 8.9,
        "generos": ["Comedia"],
        "estado": "Finalizada"
    },
    {
        "titulo": "Game of Thrones",
        "año_inicio": 2011,
        "año_fin": 2019,
        "temporadas": 8,
        "episodios_total": 73,
        "calificacion": 9.2,
        "generos": ["Drama", "Fantasía", "Aventura"],
        "estado": "Finalizada"
    },
    {
        "titulo": "The Mandalorian",
        "año_inicio": 2019,
        "año_fin": 2025,  # Suponiendo que continúa
        "temporadas": 4,
        "episodios_total": 32,
        "calificacion": 8.7,
        "generos": ["Acción", "Aventura", "Ciencia Ficción"],
        "estado": "En emisión"
    },
    {
        "titulo": "Friends",
        "año_inicio": 1994,
        "año_fin": 2004,
        "temporadas": 10,
        "episodios_total": 236,
        "calificacion": 8.9,
        "generos": ["Comedia", "Romance"],
        "estado": "Finalizada"
    },
    {
        "titulo": "Black Mirror",
        "año_inicio": 2011,
        "año_fin": 2023,
        "temporadas": 6,
        "episodios_total": 27,
        "calificacion": 8.8,
        "generos": ["Drama", "Ciencia Ficción", "Thriller"],
        "estado": "Finalizada"
    },
    {
        "titulo": "The Crown",
        "año_inicio": 2016,
        "año_fin": 2023,
        "temporadas": 6,
        "episodios_total": 60,
        "calificacion": 8.7,
        "generos": ["Drama", "Historia"],
        "estado": "Finalizada"
    }
]

# 1.4. Diccionario para plataformas de streaming
plataformas = {
    "Netflix": ["Breaking Bad", "Stranger Things", "The Crown", "Black Mirror"],
    "Disney+": ["The Mandalorian", "Coco", "El Rey León"],
    "Prime Video": ["The Office", "Todo en Todas Partes al Mismo Tiempo", "El Señor de los Anillos: La Comunidad del Anillo"],
    "HBO Max": ["Game of Thrones", "El Caballero Oscuro", "Matrix"],
    "Paramount+": ["El Padrino", "Pulp Fiction"]
}

# =============================================================================
# PARTE 2: FUNCIONES
# =============================================================================

def agregar_pelicula(peliculas, titulo, año, duracion, calificacion, generos_pelicula):
    """
    Añade una nueva película a la lista de películas.
    
    Args:
        peliculas: Lista de películas existente
        titulo: Título de la película
        año: Año de lanzamiento
        duracion: Duración en minutos
        calificacion: Calificación entre 0 y 10
        generos_pelicula: Lista de géneros de la película
    
    Returns:
        bool: True si la película fue añadida, False en caso contrario
    """
    # Validar calificación
    if calificacion < 0 or calificacion > 10:
        print(f"Error: La calificación debe estar entre 0 y 10. Valor proporcionado: {calificacion}")
        return False
    
    # Validar géneros
    for genero in generos_pelicula:
        if genero not in generos:
            print(f"Error: El género '{genero}' no es válido. Géneros disponibles: {generos}")
            return False
    
    # Crear y añadir la película
    nueva_pelicula = [titulo, año, duracion, calificacion, generos_pelicula]
    peliculas.append(nueva_pelicula)
    print(f"Película '{titulo}' añadida correctamente.")
    return True


def agregar_serie(series, titulo, año_inicio, año_fin, temporadas, episodios, calificacion, generos_serie, estado):
    """
    Añade una nueva serie a la lista de series.
    
    Args:
        series: Lista de series existente
        titulo: Título de la serie
        año_inicio: Año de inicio
        año_fin: Año de finalización (puede ser None si está en emisión)
        temporadas: Número de temporadas
        episodios: Número total de episodios
        calificacion: Calificación entre 0 y 10
        generos_serie: Lista de géneros de la serie
        estado: Estado de la serie ('Finalizada', 'En emisión', 'Cancelada')
    
    Returns:
        bool: True si la serie fue añadida, False en caso contrario
    """
    # Validar calificación
    if calificacion < 0 or calificacion > 10:
        print(f"Error: La calificación debe estar entre 0 y 10. Valor proporcionado: {calificacion}")
        return False
    
    # Validar géneros
    for genero in generos_serie:
        if genero not in generos:
            print(f"Error: El género '{genero}' no es válido. Géneros disponibles: {generos}")
            return False
    
    # Crear y añadir la serie
    nueva_serie = {
        "titulo": titulo,
        "año_inicio": año_inicio,
        "año_fin": año_fin,
        "temporadas": temporadas,
        "episodios_total": episodios,
        "calificacion": calificacion,
        "generos": generos_serie,
        "estado": estado
    }
    
    series.append(nueva_serie)
    print(f"Serie '{titulo}' añadida correctamente.")
    return True


def registrar_en_plataforma(plataformas, plataforma, titulo):
    """
    Registra un título en una plataforma de streaming.
    
    Args:
        plataformas: Diccionario de plataformas
        plataforma: Nombre de la plataforma
        titulo: Título a registrar
    
    Returns:
        bool: True si se registró correctamente, False en caso contrario
    """
    # Crear la plataforma si no existe
    if plataforma not in plataformas:
        plataformas[plataforma] = []
        print(f"Nueva plataforma '{plataforma}' creada.")
    
    # Evitar duplicados
    if titulo in plataformas[plataforma]:
        print(f"El título '{titulo}' ya está registrado en {plataforma}.")
        return False
    
    # Registrar el título
    plataformas[plataforma].append(titulo)
    print(f"Título '{titulo}' registrado en {plataforma}.")
    return True


def buscar_por_genero(contenido, genero):
    """
    Busca títulos que pertenezcan a un género específico.
    Funciona tanto para la lista de películas como para la de series.
    
    Args:
        contenido: Lista de películas o series
        genero: Género a buscar
    
    Returns:
        list: Lista de títulos que pertenecen al género
    """
    resultados = []
    
    # Determinar si estamos procesando películas o series
    es_pelicula = isinstance(contenido[0], list) if contenido else False
    
    for item in contenido:
        if es_pelicula:  # Si es una película (lista)
            titulo = item[0]
            generos_item = item[4]
        else:  # Si es una serie (diccionario)
            titulo = item["titulo"]
            generos_item = item["generos"]
        
        # Añadir a resultados si el género coincide
        if genero in generos_item:
            resultados.append(titulo)
    
    return resultados


def calcular_estadisticas(peliculas, series):
    """
    Calcula estadísticas de la colección completa.
    
    Args:
        peliculas: Lista de películas
        series: Lista de series
    
    Returns:
        dict: Diccionario con las estadísticas calculadas
    """
    # Total de títulos
    total_titulos = len(peliculas) + len(series)
    
    # Calificaciones promedio
    suma_calificaciones_peliculas = sum(pelicula[3] for pelicula in peliculas)
    suma_calificaciones_series = sum(serie["calificacion"] for serie in series)
    promedio_calificaciones = (suma_calificaciones_peliculas + suma_calificaciones_series) / total_titulos
    
    # Géneros más comunes
    conteo_generos = {}
    for pelicula in peliculas:
        for genero in pelicula[4]:
            conteo_generos[genero] = conteo_generos.get(genero, 0) + 1
            
    for serie in series:
        for genero in serie["generos"]:
            conteo_generos[genero] = conteo_generos.get(genero, 0) + 1
    
    # Ordenar géneros por frecuencia
    generos_ordenados = sorted(conteo_generos.items(), key=lambda x: x[1], reverse=True)
    
    # Década con más títulos
    decadas = {}
    for pelicula in peliculas:
        decada = (pelicula[1] // 10) * 10
        decadas[decada] = decadas.get(decada, 0) + 1
    
    for serie in series:
        decada = (serie["año_inicio"] // 10) * 10
        decadas[decada] = decadas.get(decada, 0) + 1
    
    decada_mas_titulos = max(decadas.items(), key=lambda x: x[1])
    
    # Duración promedio de películas
    duracion_promedio = sum(pelicula[2] for pelicula in peliculas) / len(peliculas)
    
    # Promedio de temporadas en series
    promedio_temporadas = sum(serie["temporadas"] for serie in series) / len(series)
    
    # Armar y retornar el diccionario de estadísticas
    estadisticas = {
        "total_titulos": total_titulos,
        "promedio_calificaciones": round(promedio_calificaciones, 1),
        "generos_mas_comunes": generos_ordenados[:3],  # Top 3 de géneros
        "decada_mas_titulos": decada_mas_titulos,
        "duracion_promedio_peliculas": round(duracion_promedio, 1),
        "promedio_temporadas_series": round(promedio_temporadas, 1)
    }
    
    return estadisticas


def recomendar_contenido(peliculas, series, generos_preferidos, calificacion_minima):
    """
    Recomienda películas y series basadas en géneros preferidos y calificación mínima.
    
    Args:
        peliculas: Lista de películas
        series: Lista de series
        generos_preferidos: Lista de géneros preferidos
        calificacion_minima: Calificación mínima requerida
    
    Returns:
        dict: Diccionario con las recomendaciones de películas y series
    """
    recomendaciones_peliculas = []
    recomendaciones_series = []
    
    # Recomendar películas
    for pelicula in peliculas:
        if pelicula[3] >= calificacion_minima:
            # Verificar si la película tiene al menos uno de los géneros preferidos
            if any(genero in pelicula[4] for genero in generos_preferidos):
                recomendaciones_peliculas.append({
                    "titulo": pelicula[0],
                    "año": pelicula[1],
                    "calificacion": pelicula[3],
                    "generos": pelicula[4]
                })
    
    # Recomendar series
    for serie in series:
        if serie["calificacion"] >= calificacion_minima:
            # Verificar si la serie tiene al menos uno de los géneros preferidos
            if any(genero in serie["generos"] for genero in generos_preferidos):
                recomendaciones_series.append({
                    "titulo": serie["titulo"],
                    "año_inicio": serie["año_inicio"],
                    "calificacion": serie["calificacion"],
                    "generos": serie["generos"],
                    "estado": serie["estado"]
                })
    
    # Ordenar recomendaciones por calificación (de mayor a menor)
    recomendaciones_peliculas.sort(key=lambda x: x["calificacion"], reverse=True)
    recomendaciones_series.sort(key=lambda x: x["calificacion"], reverse=True)
    
    return {
        "peliculas": recomendaciones_peliculas,
        "series": recomendaciones_series
    }





# Mostrar la estructura de datos actual
print("=" * 60)
print("ESTRUCTURA DE DATOS INICIAL")
print("=" * 60)

# Mostrar lista de géneros
print("\n1. Lista de géneros:")
for i, gen in enumerate(generos, 1):
    print(f"   {i}. {gen}", end="   ")
    if i % 4 == 0:
        print()  # Nueva línea cada 4 géneros
print("\n")

# Mostrar algunas películas
print("2. Ejemplo de películas (formato lista de listas):")
for i, pelicula in enumerate(peliculas[:3], 1):  # Mostrar solo las 3 primeras
    print(f"   {i}. {pelicula[0]} ({pelicula[1]}) - Calificación: {pelicula[3]}/10")
    print(f"      Duración: {pelicula[2]} minutos - Géneros: {', '.join(pelicula[4])}")
print("   ... y otras películas más.\n")

# Mostrar algunas series
print("3. Ejemplo de series (formato lista de diccionarios):")
for i, serie in enumerate(series[:3], 1):  # Mostrar solo las 3 primeras
    print(f"   {i}. {serie['titulo']} ({serie['año_inicio']}-{serie['año_fin']})")
    print(f"      {serie['temporadas']} temporadas, {serie['episodios_total']} episodios - Calificación: {serie['calificacion']}/10")
    print(f"      Géneros: {', '.join(serie['generos'])} - Estado: {serie['estado']}")
print("   ... y otras series más.\n")

# Mostrar algunas plataformas
print("4. Ejemplo de plataformas (formato diccionario):")
for i, (plataforma, titulos) in enumerate(list(plataformas.items())[:3], 1):  # Mostrar solo las 3 primeras
    print(f"   {i}. {plataforma}: {', '.join(titulos[:3])}" + ("..." if len(titulos) > 3 else ""))
print("   ... y otras plataformas más.\n")

# Ejemplos de uso de las funciones
print("=" * 60)
print("EJEMPLOS DE USO DE FUNCIONES")
print("=" * 60)

# Ejemplo 1: Agregar una película
print("\n1. Agregar una película:")
nueva_pelicula = agregar_pelicula(peliculas, "Avatar", 2009, 162, 7.8, ["Ciencia Ficción", "Aventura", "Acción"])
print(f"   ¿Se agregó correctamente? {nueva_pelicula}")
print(f"   Total de películas ahora: {len(peliculas)}")

# Ejemplo 2: Agregar una serie
print("\n2. Agregar una serie:")
nueva_serie = agregar_serie(series, "The Boys", 2019, 2025, 4, 32, 8.7, ["Acción", "Comedia", "Crimen"], "En emisión")
print(f"   ¿Se agregó correctamente? {nueva_serie}")
print(f"   Total de series ahora: {len(series)}")

# Ejemplo 3: Registrar en plataforma
print("\n3. Registrar título en plataforma:")
registro = registrar_en_plataforma(plataformas, "Netflix", "Avatar")
print(f"   ¿Se registró correctamente? {registro}")
print(f"   Títulos en Netflix ahora: {plataformas['Netflix']}")

# Ejemplo 4: Buscar por género
print("\n4. Buscar por género:")
peliculas_accion = buscar_por_genero(peliculas, "Acción")
print(f"   Películas de Acción: {peliculas_accion}")
series_drama = buscar_por_genero(series, "Drama")
print(f"   Series de Drama: {series_drama}")

# Ejemplo 5: Calcular estadísticas
print("\n5. Estadísticas de la colección:")
stats = calcular_estadisticas(peliculas, series)
print(f"   Total de títulos: {stats['total_titulos']}")
print(f"   Calificación promedio: {stats['promedio_calificaciones']}/10")
print(f"   Géneros más comunes: {stats['generos_mas_comunes'][:3]}")  # Top 3
print(f"   Década con más títulos: {stats['decada_mas_titulos'][0]}s ({stats['decada_mas_titulos'][1]} títulos)")
print(f"   Duración promedio de películas: {stats['duracion_promedio_peliculas']} minutos")
print(f"   Promedio de temporadas por serie: {stats['promedio_temporadas_series']}")

# Ejemplo 6: Obtener recomendaciones
print("\n6. Recomendaciones personalizadas:")
recomendaciones = recomendar_contenido(peliculas, series, ["Acción", "Aventura"], 8.5)

if recomendaciones["peliculas"]:
    print("   Películas recomendadas:")
    for i, p in enumerate(recomendaciones["peliculas"][:2], 1):  # Mostrar solo las 2 primeras
        print(f"   {i}. {p['titulo']} - {p['calificacion']}/10 - Géneros: {', '.join(p['generos'])}")
else:
    print("   No hay películas que cumplan los criterios")
    
if recomendaciones["series"]:
    print("   Series recomendadas:")
    for i, s in enumerate(recomendaciones["series"][:2], 1):  # Mostrar solo las 2 primeras
        print(f"   {i}. {s['titulo']} - {s['calificacion']}/10 - Géneros: {', '.join(s['generos'])}")
else:
    print("   No hay series que cumplan los criterios")
