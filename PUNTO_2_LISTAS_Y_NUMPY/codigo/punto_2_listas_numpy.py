"""
PUNTO 2: MANEJO DE LISTAS Y ARREGLOS
Comparación de rendimiento: Listas nativas vs NumPy

Autor: Santiago Cano
Fecha: Marzo 2026
"""

import pandas as pd
import numpy as np
import time

def crear_dataset_demo(n_muestras=100000):
    """Crea dataset de demostración con estadísticas reales."""
    np.random.seed(42)
    return pd.DataFrame({
        'R_Ohm': np.random.normal(loc=-0.69, scale=1.88, size=n_muestras),
        'meas_C_ma': np.random.uniform(50, 300, size=n_muestras),
        'meas_V_V': np.random.uniform(-1.6, 0, size=n_muestras)
    })


def operaciones_listas(lista_resistencias):
    """Realiza operaciones con listas nativas."""
    
    RANGO_MIN = -15.0
    RANGO_MAX = -0.01
    
    # Operación 1
    tiempo_inicio = time.time()
    max_lista = max(lista_resistencias)
    min_lista = min(lista_resistencias)
    promedio_lista = sum(lista_resistencias) / len(lista_resistencias)
    tiempo_op1 = time.time() - tiempo_inicio
    
    # Operación 2
    tiempo_inicio = time.time()
    contador_normal = sum(1 for x in lista_resistencias if RANGO_MIN <= x <= RANGO_MAX)
    contador_bajo = sum(1 for x in lista_resistencias if x < RANGO_MIN)
    contador_alto = sum(1 for x in lista_resistencias if x > RANGO_MAX)
    tiempo_op2 = time.time() - tiempo_inicio
    
    return {
        'max': max_lista,
        'min': min_lista,
        'promedio': promedio_lista,
        'contador_total': len(lista_resistencias),
        'contador_normal': contador_normal,
        'contador_bajo': contador_bajo,
        'contador_alto': contador_alto,
        'tiempo_op1': tiempo_op1,
        'tiempo_op2': tiempo_op2
    }


def operaciones_numpy(arr_resistencias):
    """Realiza operaciones con NumPy."""
    
    RANGO_MIN = -15.0
    RANGO_MAX = -0.01
    G = 5.0265
    
    # Operación 1: Estadísticas
    tiempo_inicio = time.time()
    max_np = np.max(arr_resistencias)
    min_np = np.min(arr_resistencias)
    prom_np = np.mean(arr_resistencias)
    med_np = np.median(arr_resistencias)
    std_np = np.std(arr_resistencias)
    tiempo_op1 = time.time() - tiempo_inicio
    
    # Operación 2: Filtrado
    tiempo_inicio = time.time()
    mask_normal = (arr_resistencias >= RANGO_MIN) & (arr_resistencias <= RANGO_MAX)
    cnt_normal_np = np.sum(mask_normal)
    cnt_bajo_np = np.sum(arr_resistencias < RANGO_MIN)
    cnt_alto_np = np.sum(arr_resistencias > RANGO_MAX)
    tiempo_op2 = time.time() - tiempo_inicio
    
    # Operación 3: Transformaciones
    tiempo_inicio = time.time()
    resistividad = arr_resistencias * G
    conductividad = np.where(resistividad != 0, 1.0 / resistividad, np.nan)
    resistencias_abs = np.abs(arr_resistencias)
    tiempo_op3 = time.time() - tiempo_inicio
    
    # Operación 4: Percentiles
    tiempo_inicio = time.time()
    percentiles = np.percentile(arr_resistencias, [5, 50, 95])
    tiempo_op4 = time.time() - tiempo_inicio
    
    # Operación 5: Vectorizadas
    tiempo_inicio = time.time()
    res_mult = arr_resistencias * 2.5
    res_log = np.log10(np.abs(arr_resistencias) + 1e-10)
    res_sqrt = np.sqrt(np.abs(arr_resistencias))
    tiempo_op5 = time.time() - tiempo_inicio
    
    return {
        'max': max_np,
        'min': min_np,
        'promedio': prom_np,
        'mediana': med_np,
        'std': std_np,
        'contador_normal': cnt_normal_np,
        'contador_bajo': cnt_bajo_np,
        'contador_alto': cnt_alto_np,
        'percentiles': percentiles,
        'tiempo_op1': tiempo_op1,
        'tiempo_op2': tiempo_op2,
        'tiempo_op3': tiempo_op3,
        'tiempo_op4': tiempo_op4,
        'tiempo_op5': tiempo_op5
    }


def main():
    """Función principal."""
    print("╔" + "═" * 118 + "╗")
    print("║" + "PUNTO 2: LISTAS VS NUMPY".center(118) + "║")
    print("╚" + "═" * 118 + "╝\n")

    # Crear dataset
    print("Creando dataset de demostración...")
    df_maestro = crear_dataset_demo(100000)
    df_limpio = df_maestro.dropna(subset=['R_Ohm'])
    print(f"✓ Dataset: {len(df_limpio):,} registros\n")

    # Operaciones con listas
    print("Operaciones con LISTAS:")
    tiempo_inicio = time.time()
    lista_resistencias = list(df_limpio['R_Ohm'].values)
    tiempo_crear_lista = time.time() - tiempo_inicio
    
    resultados_lista = operaciones_listas(lista_resistencias)
    print(f"  Crear lista: {tiempo_crear_lista:.4f}s")
    print(f"  Operación 1: {resultados_lista['tiempo_op1']:.4f}s")
    print(f"  Operación 2: {resultados_lista['tiempo_op2']:.4f}s")
    tiempo_total_lista = tiempo_crear_lista + resultados_lista['tiempo_op1'] + resultados_lista['tiempo_op2']
    print(f"  Total: {tiempo_total_lista:.4f}s\n")

    # Operaciones con NumPy
    print("Operaciones con NUMPY:")
    tiempo_inicio = time.time()
    arr_resistencias = np.array(lista_resistencias)
    tiempo_crear_array = time.time() - tiempo_inicio
    
    resultados_numpy = operaciones_numpy(arr_resistencias)
    print(f"  Crear array: {tiempo_crear_array:.4f}s")
    print(f"  Operación 1: {resultados_numpy['tiempo_op1']:.4f}s")
    print(f"  Operación 2: {resultados_numpy['tiempo_op2']:.4f}s")
    print(f"  Operación 3: {resultados_numpy['tiempo_op3']:.4f}s")
    print(f"  Operación 4: {resultados_numpy['tiempo_op4']:.4f}s")
    print(f"  Operación 5: {resultados_numpy['tiempo_op5']:.4f}s")
    tiempo_total_numpy = (tiempo_crear_array + resultados_numpy['tiempo_op1'] + 
                         resultados_numpy['tiempo_op2'] + resultados_numpy['tiempo_op3'] +
                         resultados_numpy['tiempo_op4'] + resultados_numpy['tiempo_op5'])
    print(f"  Total: {tiempo_total_numpy:.4f}s\n")

    # Comparación
    aceleracion = tiempo_total_lista / tiempo_total_numpy
    print(f"🚀 ACELERACIÓN: {aceleracion:.2f}x CON NUMPY\n")

    return resultados_lista, resultados_numpy


if __name__ == "__main__":
    res_lista, res_numpy = main()
    print("Punto 2 completado exitosamente")
