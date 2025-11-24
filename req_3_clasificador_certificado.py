# req_3_clasificador_certificado.py

# --- Requerimiento: Sentencias Condicionales (if, elif, else) ---

print("--- CLASIFICADOR CATEGÓRICO DE CERTIFICADO DE LOGRO ---")

# Variables de entrada (Simulación de nota final)
nota_final_porcentaje = 85.0 # Nota del estudiante, expresada en porcentaje (0 a 100)
nota_corte_certificado = 80.0 # Mínimo necesario para el Certificado de Logro
nota_corte_mencion = 95.0     # Mínimo para obtener una Mención de Honor

print(f"Nota final del curso: {nota_final_porcentaje:.1f}%")
print(f"Mínimo para Certificado: {nota_corte_certificado:.1f}%")

# Control de Flujo ABSOLUTO:
if nota_final_porcentaje >= nota_corte_mencion:
    # 1. Condición: LOGRO ABSOLUTO MÁXIMO
    estado_final = "¡CERTIFICADO CON MENCIÓN DE HONOR! Desempeño CRÍTICO sobresaliente."
elif nota_final_porcentaje >= nota_corte_certificado:
    # 2. Condición: CERTIFICADO REGULAR (se ejecuta si NO tiene mención, pero sí la nota de corte)
    estado_final = "CERTIFICADO DE LOGRO OBTENIDO. ¡Felicidades!"
else:
    # 3. Condición: SIN CERTIFICADO (la conclusión ineludible)
    estado_final = "SIN CERTIFICADO. Requiere repasar los módulos clave."

print(f"RESULTADO FINAL: {estado_final}")

# El script demuestra el uso ABSOLUTO de if, elif y else para la toma de decisiones.