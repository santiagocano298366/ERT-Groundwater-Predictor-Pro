# Punto 1: Programacion Basica en Python Aplicada a Industria

## Objetivo General

Implementar un programa en Python que valide datos de operacion de un proceso industrial, utilizando condicionales (IF/ELIF/ELSE), ciclos (FOR/WHILE) y reglas de alerta para detectar anomalias operacionales.

---

## EXPLICACION DE LA LOGICA DEL PROGRAMA

### Que hace este programa?

Este programa valida mediciones de Tomografia de Resistividad Electrica (ERT) para detectar anomalias operacionales en sistemas de prospeccion de agua subterranea.

### Caso de Uso Industrial: Prospeccion de Agua Subterranea

La Tomografia de Resistividad Electrica (ERT) es una tecnica geofisica que permite:

- Detectar depositos de agua subterranea midiendo la resistencia electrica del suelo
- Generar mapas 3D del subsuelo
- Aplicaciones: Mineria, agricultura, evaluacion ambiental, ingenieria civil

Principio fisico:
- El agua presenta baja resistividad (~1 Ohm·m)
- El suelo seco tiene alta resistividad (~100+ Ohm·m)
- Al inyectar corriente electrica y medir voltaje entre electrodos, obtenemos mapas de distribucion de agua

### Como Funciona el Programa (Paso a Paso)

#### 1. ENTRADA DE DATOS (15 mediciones ERT)

Cada medicion contiene:
- ID de medicion
- Fecha
- Posicion de electrodo A
- Posicion de electrodo B
- Resistencia (Ohm)
- Corriente (mA)
- Voltaje (V)
- Contacto / Impedancia (Ohm)

#### 2. VALIDACION CON CONDICIONALES (IF/ELIF/ELSE)

Para cada parametro, el programa verifica:

IF (parametro dentro de rango normal)
    => Estado: NORMAL (OK)
ELIF (parametro ligeramente fuera de rango)
    => Estado: ALERTA + Mensaje especifico
ELSE (parametro critico)
    => Estado: CRITICO + Mensaje de falla

Ejemplos de alertas:
- Si resistencia < -22.5 Ohm => "Resistencia CRITICA (cortocircuito posible)"
- Si corriente > 324 mA => "Corriente CRITICA (equipo sobrecargado)"
- Si contacto < 250 Ohm => "Contacto CRITICO (cortocircuito)"

#### 3. CLASIFICACION MULTINIVEL

El programa evalua 4 parametros (Resistencia, Corriente, Voltaje, Contacto):

0 problemas   => NORMAL         => Continuar prospeccion
1-2 problemas => ALERTA         => Revisar antes de continuar
3+ problemas  => CRITICO        => Detener medicion

#### 4. CICLO FOR: PROCESAR 15 MEDICIONES

for indice, medicion in mediciones:
    validar(resistencia, corriente, voltaje, contacto)
    clasificar_estado(numero_de_problemas)
    guardar_resultado()

Resultado: Itera exactamente 15 veces (una por cada medicion)

#### 5. CICLO WHILE: CALCULAR INCERTIDUMBRE

indice_actual = 0
while indice_actual < len(mediciones):
    incertidumbre = (error_absoluto / valor_medido) * 100%
    clasificar_incertidumbre(como "ACEPTABLE" o "ALTA")
    indice_actual += 1  (incremento manual)

Formula de Incertidumbre:
Incertidumbre (%) = (|R| * 0.05 + 0.01) / |R| * 100

Donde R es la resistencia absoluta medida.

### Salida del Programa

Genera 2 archivos CSV con resultados:

01_validacion_mediciones.csv
- Estado de cada medicion (NORMAL, ALERTA, CRITICO)
- Numero de problemas detectados
- Descripcion especifica de cada anomalia

01_incertidumbre_mediciones.csv
- Incertidumbre relativa (%) para cada medida
- Clasificacion como "ACEPTABLE" o "ALTA"
- Permite evaluar confiabilidad de los datos

Ejemplo de interpretacion:
- Medicion 1: NORMAL => Datos confiables, continuar prospeccion
- Medicion 8: CRITICO => Contacto de 15,000 Ohm (electrodo degradado), revisar equipo

---

## CONCEPTOS DE PROGRAMACION APLICADOS

IF/ELIF/ELSE
- Uso: Validacion de 4 parametros con logica multinivel
- Ubicacion: Funcion validar_medicion()

FOR loop
- Uso: Itera sobre 15 mediciones procesa cada una
- Ubicacion: Funcion procesar_punto1()

WHILE loop
- Uso: Calcula incertidumbre de forma secuencial
- Ubicacion: Funcion calcular_incertidumbre()

Diccionarios
- Uso: Almacena parametros de cada medicion

Listas
- Uso: Acumula problemas detectados

DataFrames (Pandas)
- Uso: Organiza resultados en tabla para exportar

Constantes
- Uso: Define umbrales de operacion normal

---

## REQUISITOS CUMPLIDOS

Requisito                      Estado
≥10 registros                 CUMPLIDO - 15 mediciones generadas
IF/ELIF/ELSE                  CUMPLIDO - 4 validaciones con condicionales
FOR loop                      CUMPLIDO - Itera 15 mediciones en procesar_punto1()
WHILE loop                    CUMPLIDO - Calcula incertidumbre en calcular_incertidumbre()
Alertas con reglas            CUMPLIDO - 6+ tipos de alertas, 8 umbrales definidos
Explicacion clara             CUMPLIDO - Este README documenta cada aspecto

---

## ARCHIVOS EN ESTE DIRECTORIO

PUNTO_1_PROGRAMACION_BASICA/
- README.md                          (Este archivo)
- codigo/
  - punto_1.py                       Codigo fuente principal
- resultados/
  - 01_validacion_mediciones.csv     Resultados de validacion
  - 01_incertidumbre_mediciones.csv  Analisis de incertidumbre

---

## COMO EJECUTAR

Opcion 1: Desde Google Colab

from google.colab import drive
drive.mount('/content/drive')

exec(open('/path/to/punto_1.py').read())

Opcion 2: Localmente

python codigo/punto_1.py

---

## RESULTADOS ESPERADOS

Al ejecutar el programa, obtendras:

Datos creados: 15 mediciones
Validaciones completadas (Ciclo FOR ejecutado 15 veces)
  - Normal: 13 (86.7%)
  - Alerta: 1 (6.7%)
  - Critico: 1 (6.7%)

Incertidumbre calculada (Ciclo WHILE ejecutado 15 veces)
  - Aceptable: 15 (100%)
  - Alta: 0 (0%)

Punto 1 completado exitosamente

---

## METRICAS PRINCIPALES

Metrica                          Valor   Interpretacion
Mediciones Procesadas            15      Supera minimo de 10
Operacion Normal                 86.7%   Mayoria de datos validos
Incertidumbre Aceptable          100%    Precision garantizada
Estados Detectados               3 tipos NORMAL, ALERTA, CRITICO
Alertas Distintas                6+ tipos Cobertura completa
Ciclos Ejecutados                30      15 FOR + 15 WHILE

---

## APLICACION PRACTICA

Este programa es aplicable a:

- Mineria: Deteccion de vetas minerales
- Agricultura: Evaluacion de humedad del suelo
- Hidrogeologia: Prospeccion de acuiferos
- Ingenieria Civil: Evaluacion del subsuelo
- Monitoreo Ambiental: Deteccion de contaminacion

---

## REFERENCIAS

- Tomografia de Resistividad Electrica (ERT) - Wikipedia
- Ohm's Law Applications in Geophysics
- Python Control Flow: IF/ELIF/ELSE, FOR, WHILE

---

## AUTOR

Santiago Cano
- Master en Automatizacion
- Curso: Fundamentos de Programacion Cientifica
- Marzo 2026

---

Ultima actualizacion: Marzo 2026
