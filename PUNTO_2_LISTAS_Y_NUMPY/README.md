# Punto 2: Listas vs NumPy

## Descripción
Comparación de rendimiento entre listas nativas de Python y arrays de NumPy en dataset de 1.08M mediciones.

## Objetivo
Demostrar ventajas de NumPy: velocidad y eficiencia de memoria.

## Resultados
- ✅ **2.77x aceleración** con NumPy
- ✅ 71.4% reducción de memoria
- ✅ 1,081,693 mediciones procesadas
- ✅ 40.78x más rápido en filtrado

## Archivos
- `codigo/punto_2.py` - Código fuente
- `resultados/02_comparacion_listas_numpy.csv` - Comparativa
- `resultados/02_operaciones_numpy.csv` - Operaciones NumPy

## Operaciones NumPy implementadas
1. Estadísticas básicas (max, min, mean, std)
2. Filtrado con máscaras booleanas
3. Transformaciones matemáticas
4. Percentiles
5. Operaciones vectorizadas
