# req_6_calculadora_matricula.py

# --- Requerimiento: Funciones para Reutilización (def) - Descuento Fijo por Paquete ---

# 1. Definición de la Función ABSOLUTA (Calculadora de Paquete de Cursos)

def calcular_paquete_biprograma(precio_esp, precio_ing, descuento_paquete):
    """
    Calcula el costo final aplicando un descuento fijo si el niño toma ambos programas.
    
    Args:
        precio_esp (int): Costo base del Programa en Español.
        precio_ing (int): Costo base del Programa en Inglés.
        descuento_paquete (int): El monto fijo de descuento al tomar el paquete.
        
    Returns:
        tuple: (precio_individual_total, precio_paquete_final)
    """
    # 1. Suma Categórica de los precios individuales
    precio_individual_total = precio_esp + precio_ing
    
    # 2. Aplicación del descuento fijo
    precio_paquete_final = precio_individual_total - descuento_paquete
    
    # Devuelve ambos valores para comparación
    return precio_individual_total, precio_paquete_final


# 2. Variables de Entrada (Valores en Pesos Chilenos - CLP)
precio_base_espanol = 35000 
precio_base_ingles = 25000
descuento_fijo_paquete = 10000 # Descuento ABSOLUTO por tomar ambos programas

# 3. Escenario 1: Uso de la Función para calcular el Paquete Biprograma
# La función devuelve dos valores, que asignamos a dos variables.
costo_individual_total, costo_final_paquete = calcular_paquete_biprograma(
    precio_base_espanol, 
    precio_base_ingles, 
    descuento_fijo_paquete
)

print("--- CÁLCULO DE MATRÍCULA CATEGÓRICO (PAQUETE) ---")
print(f"Programa en Español (Individual): ${precio_base_espanol} CLP")
print(f"Programa en Inglés (Individual): ${precio_base_ingles} CLP")

print("\n-----------------------------------------------------")
print("Cálculo del Paquete Biprograma (Español + Inglés):")
print(f"Suma Individual ABSOLUTA (Sin Descuento): ${costo_individual_total} CLP")
print(f"Descuento Fijo Aplicado: ${descuento_fijo_paquete} CLP")
print(f"COSTO FINAL del Paquete (Requisito CRÍTICO): ${costo_final_paquete} CLP")


# 4. Escenario 2: Reutilización de la Función para otros Cursos (Taller de Mamás)
# Asumiendo que dos talleres de Mamás también tienen un paquete similar (ej: $5.000 de descuento)
precio_taller_teologia = 15000
precio_taller_english = 12000
descuento_moms_paquete = 5000

total_moms_individual, total_moms_paquete = calcular_paquete_biprograma(
    precio_taller_teologia,
    precio_taller_english,
    descuento_moms_paquete
)

print("\n-----------------------------------------------------")
print("Cálculo del Paquete de Talleres para Mamás (Teología + English):")
print(f"Suma Individual ABSOLUTA: ${total_moms_individual} CLP")
print(f"COSTO FINAL del Paquete de Mamás: ${total_moms_paquete} CLP")

# La función se reutilizó ABSOLUTAMENTE para dos escenarios, demostrando su utilidad.