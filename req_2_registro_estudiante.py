# req_2_registro_estudiante.py

# --- Requerimiento: Tipos de Datos (str, int, float, bool) ---

print("--- REGISTRO CATEGÓRICO DE NUEVO ESTUDIANTE ONLINE ---")

# 1. Cadenas (str): Solicitud de información textual
nombre_estudiante = input("Nombre completo del estudiante: ") 
curso_matriculado = input("Nombre del curso a inscribir: ")

# 2. Enteros (int): Conversión de la edad
edad_str = input("Edad del estudiante (ej: 8): ")
edad_int = int(edad_str) # Conversión ABSOLUTA a entero

# 3. Flotantes (float): El precio del curso
precio_curso_str = input("Precio del curso sin descuento (ej: 499.99): ")
precio_curso_float = float(precio_curso_str) # Conversión ABSOLUTA a flotante

# 4. Booleano (bool): Estado de la etapa educativa
# El valor es True si el estudiante está en edad de Educación Básica (6 a 13 años).
es_educacion_basica = (edad_int >= 6) and (edad_int <= 13) # Asignación de valor booleano CRÍTICO

print("\n--- RESUMEN DE LA MATRÍCULA ---")
print(f"Nombre: {nombre_estudiante} (Tipo: {type(nombre_estudiante)})")
print(f"Curso: {curso_matriculado} (Tipo: {type(curso_matriculado)})")
print(f"Edad: {edad_int} años (Tipo: {type(edad_int)})")
print(f"Precio: ${precio_curso_float} (Tipo: {type(precio_curso_float)})")
print(f"¿Es Educación Básica?: {es_educacion_basica} (Tipo: {type(es_educacion_basica)})")

# El programa demuestra la gestión de diferentes tipos de datos, con una lógica booleana relevante.