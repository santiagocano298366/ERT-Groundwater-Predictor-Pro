"""
PUNTO 5: PROYECTO FINAL - AVANCE CON LITERATURA
Análisis de 10 referencias + cronograma

Autor: Santiago Cano
Fecha: Marzo 2026
"""

import pandas as pd


def crear_matriz_literatura():
    """Crea matriz de revisión de literatura."""
    
    referencias = pd.DataFrame({
        'ID': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10'],
        'Autor/Año': [
            'Abdelrahman et al. (2024)',
            'USGS (2024)',
            'Frontiers Water (2025)',
            'Samouëlian et al. (2023)',
            'Hermans et al. (2020)',
            'Loke (2023)',
            'Koesuma et al. (2024)',
            'Guerin et al. (2021)',
            'Kaya & Yoshida (2021)',
            'Xu et al. (2022)'
        ],
        'Año': [2024, 2024, 2025, 2023, 2020, 2023, 2024, 2021, 2021, 2022],
        'Hallazgos Clave': [
            'σ > 0.01 S/m indica agua probable',
            'Monitoreo en tiempo real es viable',
            'ERT es más efectiva en < 100m',
            'Correlación σ-humedad es robusta',
            'Inversión 3D mejora interpretación',
            'Algoritmos RES3DINV son estándar',
            'Precisión ~85% en predicción',
            'Frecuencia afecta interpretación',
            'IA alcanza ~90% de precisión',
            'Cambios detectables cada 2 semanas'
        ]
    })
    
    return referencias


def crear_cronograma():
    """Crea cronograma del proyecto."""
    
    cronograma = pd.DataFrame({
        'Fase': [
            'Análisis de datos',
            'Desarrollo modelo',
            'Diseño hardware',
            'Desarrollo software',
            'Validación campo',
            'Prototipado',
            'Documentación'
        ],
        'Mes Inicio': [1, 3, 5, 5, 8, 11, 11],
        'Mes Fin': [2, 4, 7, 7, 10, 12, 12],
        'Duración (meses)': [2, 2, 3, 3, 3, 2, 2]
    })
    
    return cronograma


def crear_indicadores():
    """Crea indicadores de éxito."""
    
    indicadores = pd.DataFrame({
        'Indicador': [
            'Precisión del modelo',
            'Costo del dispositivo',
            'Tiempo de medición',
            'Accesibilidad',
            'Autonomía de batería',
            'Exactitud de resistividad',
            'Validación en campo'
        ],
        'Meta': [
            '≥80%',
            '<$5,000',
            '<2 horas',
            'Score ≥8/10',
            '≥8 horas',
            '±10%',
            '≥90%'
        ]
    })
    
    return indicadores


def main():
    """Función principal."""
    print("╔" + "═" * 100 + "╗")
    print("║" + "PUNTO 5: PROYECTO FINAL".center(100) + "║")
    print("╚" + "═" * 100 + "╝\n")

    # Literatura
    referencias = crear_matriz_literatura()
    print(f"Matriz de Literatura: {len(referencias)} referencias")
    print(f"  Antigüedad promedio: {(2025 - referencias['Año'].mean()):.1f} años")
    print(f"  Recientes (≥2022): {sum(referencias['Año'] >= 2022)} referencias\n")

    # Cronograma
    cronograma = crear_cronograma()
    print(f"Cronograma: {len(cronograma)} fases")
    print(f"  Duración total: {cronograma['Mes Fin'].max()} meses\n")

    # Indicadores
    indicadores = crear_indicadores()
    print(f"Indicadores de éxito: {len(indicadores)} métricas\n")

    return referencias, cronograma, indicadores


if __name__ == "__main__":
    refs, crono, indic = main()
    print("Punto 5 completado exitosamente")
