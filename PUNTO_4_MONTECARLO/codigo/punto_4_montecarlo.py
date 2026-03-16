"""
PUNTO 4: SIMULACIÓN DE MONTECARLO
5000 simulaciones para estimar probabilidad de agua

Autor: Santiago Cano
Fecha: Marzo 2026
"""

import numpy as np
import pandas as pd


def simular_conductividad(conductividad_media=0.2326, conductividad_std=0.25, num_simulaciones=5000):
    """Genera 5000 simulaciones de conductividad."""
    
    np.random.seed(42)
    conductividades = np.random.normal(loc=conductividad_media,
                                       scale=conductividad_std,
                                       size=num_simulaciones)
    return conductividades


def calcular_estadisticas(conductividades):
    """Calcula estadísticas de las simulaciones."""
    
    stats = {
        'media': np.mean(conductividades),
        'mediana': np.median(conductividades),
        'std': np.std(conductividades),
        'min': np.min(conductividades),
        'max': np.max(conductividades),
        'p5': np.percentile(conductividades, 5),
        'p95': np.percentile(conductividades, 95),
    }
    return stats


def calcular_probabilidad_agua(conductividades, umbral=0.01):
    """Calcula probabilidad de presencia de agua."""
    
    muestras_agua = np.sum(conductividades > umbral)
    probabilidad = (muestras_agua / len(conductividades)) * 100
    
    return probabilidad, muestras_agua


def main():
    """Función principal."""
    print("╔" + "═" * 100 + "╗")
    print("║" + "PUNTO 4: SIMULACIÓN DE MONTECARLO".center(100) + "║")
    print("╚" + "═" * 100 + "╝\n")

    # Simular
    print("Generando 5000 simulaciones de conductividad...")
    conductividades = simular_conductividad()
    print(f"✓ {len(conductividades):,} muestras generadas\n")

    # Estadísticas
    stats = calcular_estadisticas(conductividades)
    print("Estadísticas:")
    for clave, valor in stats.items():
        print(f"  {clave}: {valor:.4f}")
    print()

    # Probabilidad de agua
    prob_agua, muestras = calcular_probabilidad_agua(conductividades)
    print(f"Probabilidad de agua:")
    print(f"  Umbral: 0.01 S/m")
    print(f"  Muestras que cumplen: {muestras:,} / {len(conductividades):,}")
    print(f"  Probabilidad: {prob_agua:.1f}%\n")

    # Decisión
    if prob_agua >= 70:
        decision = "✅ FAVORABLE - Explorar agua"
    else:
        decision = "❌ DESFAVORABLE - Riesgo alto"
    
    print(f"DECISIÓN: {decision}")

    return conductividades, stats, prob_agua


if __name__ == "__main__":
    conductividades, stats, prob = main()
    print("\nPunto 4 completado exitosamente")
