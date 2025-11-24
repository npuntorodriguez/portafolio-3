# req_4_seguimiento_modulos.py

# --- Requerimiento: Sentencias Iterativas (for y while) - Taller "English for Moms" ---

# --- Uso del bucle FOR: Listar los módulos y tareas semanales ---
print("--- SEGUIMIENTO CATEGÓRICO DEL TALLER 'ENGLISH FOR MOMS' ---")

# Lista absoluta de las TAREAS semanales que la mamá debe completar
tareas_semanales = [
    "Semana 1: Presentación Personal (Video)", 
    "Semana 2: Vocabulario de Hogar y Familia", 
    "Semana 3: Diálogo con el niño sobre su rutina",
    "Semana 4: Proyecto Final: Mi Rutina"
]

# Bucle FOR CRÍTICO: Itera sobre la lista de tareas.
print("\nTareas Semanales del Módulo 'English for Moms':")
for i, tarea in enumerate(tareas_semanales):
    # Usamos f-string para formatear la salida, indicando la numeración.
    print(f"✅ Tarea {i+1}: {tarea}")


print("\n----------------------------------------")

# --- Uso del bucle WHILE: Simular los intentos de la mamá en una Tarea CRÍTICA (Video) ---
print("--- Verificación de Intentos en la Tarea 'Video de Presentación' ---")

nombre_mama = "Naraly Ar" # <--- ¡NOMBRE CATEGÓRICO APLICADO!
intentos_maximos = 3 # El número MÁXIMO de veces que se permite subir el video.
intentos_actuales = 1 # Contador que empieza en el intento número 1.

# Bucle WHILE ABSOLUTO: Se repite MIENTRAS el número de intentos no supere el máximo.
while intentos_actuales <= intentos_maximos:
    
    if intentos_actuales == 1:
        print(f"La estudiante {nombre_mama} realiza el Primer Intento de grabación. (Intento {intentos_actuales})")
    else:
        print(f"La estudiante {nombre_mama} edita y re-sube el video. (Intento {intentos_actuales})")
    
    # Incremento Categórico para pasar al siguiente intento
    intentos_actuales += 1
    
    # Condición de éxito simulada después del segundo intento (salida controlada)
    if intentos_actuales > 2:
        print("🎉 ¡ÉXITO! El video ha sido APROBADO categóricamente después de este intento.")
        break # Se usa 'break' para SALIR del bucle 'while'.

print(f"\nProceso de Intentos de la estudiante {nombre_mama} FINALIZADO.")