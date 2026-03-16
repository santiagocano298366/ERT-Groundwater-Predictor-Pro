"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                          ║
║                  PUNTO 1: PROGRAMACIÓN BÁSICA EN PYTHON APLICADA A INDUSTRIA                            ║
║                                                                                                          ║
║  Validación de mediciones ERT con condicionales (IF/ELIF/ELSE), ciclos (FOR/WHILE) y manejo de alertas  ║
║                                                                                                          ║
║  Autor: Santiago Cano | Fecha: Marzo 2026                                                               ║
║                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import pandas as pd
import os

# ═════════════════════════════════════════════════════════════════════════════════════════════════════════
# 📖 EXPLICACIÓN DE LA LÓGICA DEL PROGRAMA
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════

EXPLICACION = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                           ¿QUÉ HACE ESTE PROGRAMA?                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝

🎯 OBJETIVO GENERAL
───────────────────
Validar mediciones de Tomografía de Resistividad Eléctrica (ERT) para detectar anomalías operacionales
y calcular la incertidumbre de las medidas en tiempo real.


📊 CASO DE USO INDUSTRIAL: PROSPECCIÓN DE AGUA SUBTERRÁNEA
───────────────────────────────────────────────────────────
La Tomografía de Resistividad Eléctrica (ERT) es una técnica geofísica que permite:

  ✓ Detectar depósitos de agua subterránea midiendo la resistencia eléctrica del suelo
  ✓ Generar mapas 3D del subsuelo
  ✓ Aplicaciones: Minería, agricultura, evaluación ambiental, ingeniería civil

El agua presenta baja resistividad (~1 Ω·m), mientras que el suelo seco tiene alta resistividad (~100+ Ω·m).
Al inyectar corriente eléctrica y medir voltaje entre electrodos, obtenemos mapas de distribución de agua.


🔍 ¿CÓMO FUNCIONA ESTE PROGRAMA?
────────────────────────────────

1️⃣  ENTRADA DE DATOS (15 mediciones ERT)
   • ID de medición, fecha, posición de electrodos (A, B)
   • Parámetros medidos: resistencia (Ω), corriente (mA), voltaje (V), contacto (Ω)

2️⃣  VALIDACIÓN CON CONDICIONALES (IF/ELIF/ELSE)
   Para cada parámetro, el programa verifica:
   
   IF (parámetro dentro de rango normal)
      → Estado: ✓ NORMAL
   ELIF (parámetro ligeramente fuera de rango)
      → Estado: ⚠ ALERTA + Mensaje específico
   ELSE (parámetro crítico)
      → Estado: ✗ CRÍTICO + Mensaje de falla

   Ejemplo: Si resistencia < -22.5 Ω → "Resistencia CRÍTICA (cortocircuito posible)"

3️⃣  CLASIFICACIÓN MULTINIVEL
   • 0 problemas  → NORMAL (equipo funcionando bien)
   • 1-2 problemas → ALERTA (revisar antes de continuar)
   • 3+ problemas → CRÍTICO (detener medición)

4️⃣  CICLO FOR: PROCESAR 15 MEDICIONES
   for cada medición in lista_de_mediciones:
       validar(resistencia, corriente, voltaje, contacto)
       clasificar_estado(número_de_problemas)
       guardar_resultado()

5️⃣  CICLO WHILE: CALCULAR INCERTIDUMBRE
   while (hay mediciones sin procesar):
       incertidumbre = (error_absoluto / valor_medido) × 100%
       clasificar_incertidumbre(como "ACEPTABLE" o "ALTA")
       pasar_a_siguiente_medición()

📈 SALIDA DEL PROGRAMA
──────────────────────
Genera 2 archivos CSV con resultados:

  📄 01_validacion_mediciones.csv
     └─ Estado de cada medición, problemas detectados, clasificación

  📄 01_incertidumbre_mediciones.csv
     └─ Incertidumbre relativa (%) para cada medida

Ejemplo de interpretación:
  • Medición 1: NORMAL → Datos confiables, continuar prospección
  • Medición 8: CRÍTICO → Contacto de 15,000 Ω (electrodo degradado), revisar equipo

🎓 CONCEPTOS PROGRAMACIÓN APLICADOS
────────────────────────────────────
✓ IF/ELIF/ELSE    → Toma de decisiones lógicas basada en reglas
✓ FOR loop        → Iteración automática sobre 15 mediciones
✓ WHILE loop      → Procesamiento secuencial con contador manual
✓ Diccionarios    → Almacenamiento estructurado de parámetros
✓ Listas          → Acumulación de resultados
✓ Dataframes      → Organización tabular para exportar CSV
✓ Umbrales        → Constantes definidas para validación

"""


# ─────────────────────────────────────────────────────────────────────────────────────────────────────────
# PASO 1: CREAR DATOS DE EJEMPLO (15 MEDICIONES ERT)
# ─────────────────────────────────────────────────────────────────────────────────────────────────────────

def crear_datos_ejemplo():
    """Crea 15 registros de mediciones ERT con parámetros operacionales."""
    datos = {
        'id_medicion': range(1, 16),
        'fecha': ['2016-11-01', '2016-11-02', '2016-11-03', '2016-11-04',
                  '2016-11-05', '2016-11-06', '2016-11-07', '2016-11-08',
                  '2016-11-09', '2016-11-10', '2016-11-11', '2016-11-12',
                  '2016-11-13', '2016-11-14', '2016-11-15'],
        'electrodo_A': [20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
        'electrodo_B': [30, 32, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'resistencia_ohm': [-2.5, -1.8, -0.5, -3.2, -0.1, -4.5, -2.1, -30.5,
                            -1.9, -2.3, -2.6, -0.9, -1.5, -200.0, -2.8],
        'corriente_ma': [85.5, 92.3, 78.4, 88.1, 95.2, 102.5, 110.3, 305.0,
                        89.1, 91.5, 87.3, 93.8, 96.2, 50.2, 94.1],
        'voltaje_v': [-0.215, -0.167, -0.039, -0.283, -0.010, -0.395, -0.184, -2.850,
                     -0.171, -0.209, -0.236, -0.084, -0.136, 0.050, -0.255],
        'contacto_ohm': [2500, 2800, 2300, 3200, 2100, 3500, 2900, 15000,
                        2600, 2950, 3100, 2450, 2700, 100, 2850],
    }
    return pd.DataFrame(datos)


# CONSTANTES DE UMBRALES (Operación normal del sistema ERT)
RESISTENCIA_MIN_NORMAL = -15.0
RESISTENCIA_MAX_NORMAL = -0.01
CORRIENTE_MIN_NORMAL = 32.0
CORRIENTE_MAX_NORMAL = 270.0
VOLTAJE_MIN_NORMAL = -1.6
VOLTAJE_MAX_NORMAL = 0.0
CONTACTO_MIN_NORMAL = 500
CONTACTO_MAX_NORMAL = 6000
INCERTIDUMBRE_MAX_ACEPTABLE = 0.50  # 50%


def validar_medicion(resistencia, corriente, voltaje, contacto):
    """
    Valida cada parámetro de una medición ERT usando IF/ELIF/ELSE.

    Retorna:
    - estado_general: 'NORMAL', 'ALERTA', o 'CRÍTICO'
    - problemas: lista de anomalías detectadas
    - contador_problemas: número de parámetros fuera de rango
    """
    problemas = []
    contador_problemas = 0

    # ★ VALIDACIÓN 1: RESISTENCIA (IF/ELIF/ELSE)
    if RESISTENCIA_MIN_NORMAL <= resistencia <= RESISTENCIA_MAX_NORMAL:
        estado_r = "✓"
    elif resistencia < RESISTENCIA_MIN_NORMAL * 1.5:  # Muy negativa
        problemas.append("Resistencia CRÍTICA (cortocircuito posible)")
        contador_problemas += 1
        estado_r = "✗"
    else:
        problemas.append("Resistencia FUERA DE RANGO")
        contador_problemas += 1
        estado_r = "⚠"

    # ★ VALIDACIÓN 2: CORRIENTE (IF/ELIF/ELSE)
    if CORRIENTE_MIN_NORMAL <= corriente <= CORRIENTE_MAX_NORMAL:
        estado_i = "✓"
    elif corriente > CORRIENTE_MAX_NORMAL * 1.2:  # Muy alta
        problemas.append("Corriente CRÍTICA (equipo sobrecargado)")
        contador_problemas += 1
        estado_i = "✗"
    elif corriente < CORRIENTE_MIN_NORMAL * 0.8:  # Muy baja
        problemas.append("Corriente CRÍTICA (falla de inyección)")
        contador_problemas += 1
        estado_i = "✗"
    else:
        problemas.append("Corriente ANÓMALA")
        contador_problemas += 1
        estado_i = "⚠"

    # ★ VALIDACIÓN 3: VOLTAJE (IF/ELIF/ELSE)
    if VOLTAJE_MIN_NORMAL <= voltaje <= VOLTAJE_MAX_NORMAL:
        estado_v = "✓"
    elif voltaje < VOLTAJE_MIN_NORMAL * 1.5:  # Muy negativo
        problemas.append("Voltaje CRÍTICO (amplitud extrema)")
        contador_problemas += 1
        estado_v = "✗"
    else:
        problemas.append("Voltaje ANÓMALO")
        contador_problemas += 1
        estado_v = "⚠"

    # ★ VALIDACIÓN 4: CONTACTO (IF/ELIF/ELSE)
    if CONTACTO_MIN_NORMAL <= contacto <= CONTACTO_MAX_NORMAL:
        estado_c = "✓"
    elif contacto < CONTACTO_MIN_NORMAL * 0.5:  # Muy bajo - cortocircuito
        problemas.append("Contacto CRÍTICO (cortocircuito)")
        contador_problemas += 1
        estado_c = "✗"
    elif contacto > CONTACTO_MAX_NORMAL * 2:  # Muy alto - electrodo degradado
        problemas.append("Contacto CRÍTICO (electrodo degradado)")
        contador_problemas += 1
        estado_c = "✗"
    else:
        problemas.append("Contacto ANÓMALO")
        contador_problemas += 1
        estado_c = "⚠"

    # Determinar ESTADO GENERAL
    if contador_problemas == 0:
        estado_general = "NORMAL"
    elif contador_problemas <= 2:
        estado_general = "ALERTA"
    else:
        estado_general = "CRÍTICO"

    return estado_general, problemas, contador_problemas


def procesar_punto1(df_mediciones):
    """Procesa Punto 1: Validación de mediciones con ciclo FOR."""
    
    resultados = []
    contador_normal = 0
    contador_alerta = 0
    contador_critico = 0

    # CICLO FOR ← REQUISITO: Itera sobre 15 mediciones
    for indice, fila in df_mediciones.iterrows():
        id_med = fila['id_medicion']
        fecha = fila['fecha']
        r = fila['resistencia_ohm']
        i = fila['corriente_ma']
        v = fila['voltaje_v']
        c = fila['contacto_ohm']

        estado, problemas, num_probs = validar_medicion(r, i, v, c)

        if estado == "NORMAL":
            contador_normal += 1
        elif estado == "ALERTA":
            contador_alerta += 1
        else:
            contador_critico += 1

        resultados.append({
            'id_medicion': id_med,
            'fecha': fecha,
            'resistencia_ohm': r,
            'corriente_ma': i,
            'voltaje_v': v,
            'contacto_ohm': c,
            'estado': estado,
            'num_problemas': num_probs,
            'problemas': "; ".join(problemas) if problemas else "Ninguno"
        })

    return pd.DataFrame(resultados), contador_normal, contador_alerta, contador_critico


def calcular_incertidumbre(df_mediciones):
    """Calcula incertidumbre con ciclo WHILE ← REQUISITO."""
    
    indice_actual = 0
    contador_inc_aceptable = 0
    contador_inc_alta = 0
    incertidumbres = []

    # CICLO WHILE ← REQUISITO: Procesa mediciones secuencialmente
    while indice_actual < len(df_mediciones):
        fila = df_mediciones.iloc[indice_actual]
        id_med = fila['id_medicion']
        fecha = fila['fecha']

        r_abs = abs(fila['resistencia_ohm'])

        if r_abs > 0.001:
            incertidumbre_relativa = ((r_abs * 0.05 + 0.01) / r_abs) * 100
        else:
            incertidumbre_relativa = 999.0

        if incertidumbre_relativa <= INCERTIDUMBRE_MAX_ACEPTABLE * 100:
            estado_inc = "ACEPTABLE"
            contador_inc_aceptable += 1
        else:
            estado_inc = "ALTA"
            contador_inc_alta += 1

        incertidumbres.append({
            'id_medicion': id_med,
            'fecha': fecha,
            'resistencia_abs': round(r_abs, 4),
            'incertidumbre_%': round(incertidumbre_relativa, 2),
            'estado': estado_inc
        })

        indice_actual += 1

    return pd.DataFrame(incertidumbres), contador_inc_aceptable, contador_inc_alta


def main():
    """Función principal."""
    
    # MOSTRAR EXPLICACIÓN AL INICIO
    print(EXPLICACION)
    
    print("╔" + "═" * 118 + "╗")
    print("║" + "EJECUTANDO PUNTO 1: PROGRAMACIÓN BÁSICA EN PYTHON".center(118) + "║")
    print("╚" + "═" * 118 + "╝\n")

    # Crear datos
    df_mediciones = crear_datos_ejemplo()
    print(f"✓ Datos creados: {len(df_mediciones)} mediciones\n")

    # Procesar validaciones
    df_resultados, cnt_norm, cnt_alert, cnt_crit = procesar_punto1(df_mediciones)
    print(f"✓ Validaciones completadas (Ciclo FOR ejecutado {len(df_mediciones)} veces)")
    print(f"  - Normal: {cnt_norm} ({100*cnt_norm/len(df_mediciones):.1f}%)")
    print(f"  - Alerta: {cnt_alert} ({100*cnt_alert/len(df_mediciones):.1f}%)")
    print(f"  - Crítico: {cnt_crit} ({100*cnt_crit/len(df_mediciones):.1f}%)\n")

    # Calcular incertidumbre
    df_incertidumbres, cnt_acep, cnt_alta = calcular_incertidumbre(df_mediciones)
    print(f"✓ Incertidumbre calculada (Ciclo WHILE ejecutado {len(df_mediciones)} veces)")
    print(f"  - Aceptable: {cnt_acep} ({100*cnt_acep/len(df_mediciones):.1f}%)")
    print(f"  - Alta: {cnt_alta} ({100*cnt_alta/len(df_mediciones):.1f}%)\n")

    return df_resultados, df_incertidumbres


if __name__ == "__main__":
    df_res, df_inc = main()
    print("\n✅ Punto 1 completado exitosamente")
    print("\nResultados disponibles en:")
    print("  📄 resultados/01_validacion_mediciones.csv")
    print("  📄 resultados/01_incertidumbre_mediciones.csv")
