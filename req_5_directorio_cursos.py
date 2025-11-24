# req_5_directorio_cursos.py

# --- Requerimiento: Estructuras de Datos (Listas y Diccionarios) ---

# 1. Lista ABSOLUTA para contener todos los cursos (El Catálogo General).
catalogo_cursos = []

# --- CURSOS CATEGÓRICOS PARA NIÑOS (KIDS) - Todos Online En Vivo ---

curso_esp = {
    "codigo": "KIDESP01",
    "nombre": "Programa en Español (Currículo Base)",
    "rango_edad": "6-10 años",
    "modalidad": "Online En Vivo", # <--- CRÍTICO
    "cupos_disponibles": 25,
    "inscripcion_abierta": True 
}

curso_ing = {
    "codigo": "KIDENG02",
    "nombre": "Programa en Inglés (Immersion)",
    "rango_edad": "8-12 años",
    "modalidad": "Online En Vivo", # <--- CRÍTICO
    "cupos_disponibles": 0,
    "inscripcion_abierta": False 
}

curso_creacion = {
    "codigo": "KIDCRE03",
    "nombre": "Taller 'La Creación' (Estudio Bíblico)",
    "rango_edad": "6-13 años",
    "modalidad": "Online En Vivo", # <--- CRÍTICO
    "cupos_disponibles": 18,
    "inscripcion_abierta": True 
}

curso_anatomia = {
    "codigo": "KIDANA04",
    "nombre": "Taller 'Tú Anatomía Creación de Dios'",
    "rango_edad": "9-13 años",
    "modalidad": "Online En Vivo", # <--- CRÍTICO
    "cupos_disponibles": 10,
    "inscripcion_abierta": True 
}

curso_musica = {
    "codigo": "KIDMUS05",
    "nombre": "Taller 'Música en Colores'",
    "rango_edad": "4-7 años",
    "modalidad": "Online En Vivo", # <--- CRÍTICO
    "cupos_disponibles": 5,
    "inscripcion_abierta": True 
}

# --- CURSOS CATEGÓRICOS PARA MAMÁS (MOMS) ---

curso_moms_english = {
    "codigo": "MOMEN201",
    "nombre": "Taller English for Moms",
    "rango_edad": "Adultos",
    "modalidad": "Online En Vivo", # <--- CRÍTICO
    "cupos_disponibles": 30,
    "inscripcion_abierta": True 
}

curso_teologia = {
    "codigo": "MOMTE202",
    "nombre": "Taller de Teología",
    "rango_edad": "Adultos",
    "modalidad": "Grabado", # <--- ÚNICO GRABADO (REQUERIMIENTO ABSOLUTO)
    "cupos_disponibles": 0,
    "inscripcion_abierta": False 
}


# 3. Almacenamiento Categórico de TODOS los diccionarios en la lista.
catalogo_cursos.append(curso_esp)
catalogo_cursos.append(curso_ing)
catalogo_cursos.append(curso_creacion)
catalogo_cursos.append(curso_anatomia)
catalogo_cursos.append(curso_musica)
catalogo_cursos.append(curso_moms_english)
catalogo_cursos.append(curso_teologia)


# 4. Función ABSOLUTA para mostrar solo la información de cursos con inscripción abierta
def mostrar_cursos_abiertos(catalogo):
    print("\n--- CATÁLOGO ABSOLUTO DE CURSOS CON INSCRIPCIÓN ABIERTA ---")
    
    for curso in catalogo:
        if curso["inscripcion_abierta"] == True:
            print("\n----------------------------------------")
            print(f"CÓDIGO: {curso['codigo']}")
            print(f"NOMBRE: {curso['nombre']}")
            print(f"PÚBLICO OBJETIVO: {curso['rango_edad']}")
            print(f"MODALIDAD: {curso['modalidad']}")
            print(f"CUPOS DISPONIBLES: {curso['cupos_disponibles']}")
        elif curso["inscripcion_abierta"] == False:
            print(f"\n[🚫 NO DISPONIBLE] {curso['nombre']} (Código: {curso['codigo']}) - Inscripción Cerrada.")

# Ejecución de la demo
mostrar_cursos_abiertos(catalogo_cursos)