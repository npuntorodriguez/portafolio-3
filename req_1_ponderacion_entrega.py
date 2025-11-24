# req_1_ponderacion_entrega.py

## --- Requerimiento: Variables, Operadores, Estructuras Básicas (Ponderación de Entrega) ---

# 1. Variables de Entrada (Simulación de Datos CRÍTICOS)
nota_base_tarea = 9.5          # Nota que obtuvo el estudiante antes de la penalización.
tarea_entregada_a_tiempo = False # Si fue True (a tiempo, 100%), si fue False (atrasada, 90%).

# 2. Variables (Factores de Ponderación ABSOLUTOS)
ponderacion_a_tiempo = 1.00    # 100% de la nota base
ponderacion_atrasada = 0.90    # 90% de la nota base

# 3. Estructura y Operadores (Selección y Cálculo)

# La estructura if/else se usa aquí SÓLO para la selección categórica del factor:
if tarea_entregada_a_tiempo == True:
    factor_final = ponderacion_a_tiempo 
    mensaje_estado = "A TIEMPO (Ponderación 100%)"
else:
    factor_final = ponderacion_atrasada
    mensaje_estado = "ATRASADA (Ponderación 90%)"

# Aplicamos el Operador de Multiplicación CRÍTICO:
nota_final_ponderada = nota_base_tarea * factor_final

# Salida del Programa Categórico
print("--- PONDERACIÓN DE NOTA POR PUNTUALIDAD DE ENTREGA ---")
print(f"Nota base de la tarea: {nota_base_tarea:.2f}")
print(f"Estado de la Entrega: {mensaje_estado}")
print(f"Factor de Ponderación Usado: {factor_final:.2f}")
print(f"NOTA FINAL DEL ESTUDIANTE: {nota_final_ponderada:.2f}")

# La nota final en este ejemplo es 9.5 * 0.90 = 8.55.