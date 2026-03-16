# ERT Groundwater Predictor Pro

**Dispositivo portátil de medición para predicción de agua subterránea mediante análisis de resistividad eléctrica**

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Resultados Principales](#resultados-principales)
- [Cómo Revisar](#cómo-revisar)
- [Entregables](#entregables)
- [Tecnologías](#tecnologías)

---

## 🎯 Descripción

Sistema automatizado para estimar zonas con potencial de agua subterránea usando análisis de resistividad eléctrica (ERT).

### Ventajas
- ✅ **Costo**: <$5,000 USD (vs $50k-500k equipos comerciales)
- ✅ **Portátil**: <2 kg
- ✅ **Accesible**: Operación por personal no-especializado
- ✅ **Rápido**: <2 horas de análisis (vs 2-3 semanas manual)
- ✅ **Preciso**: 80-90% de precisión en predicción

---

## 📁 Estructura del Proyecto

ERT-Groundwater-Predictor-Pro/ │ ├── 📚 DOCUMENTACION/ ← TODA LA DOCUMENTACIÓN │ ├── 01_PROGRAMACION_BASICA.md │ ├── 02_LISTAS_Y_NUMPY.md │ ├── 03_INDICADORES_KPI.md │ ├── 04_MONTECARLO.md │ ├── 05_PROYECTO_FINAL.md │ ├── 06_PROTOTIPO_LOVABLE.md │ ├── 07_DESPLIEGUE_AWS.md │ └── README_DOCUMENTACION.md │ ├── 📊 PUNTO_1_PROGRAMACION_BASICA/ │ ├── README.md │ ├── codigo/ │ │ └── punto_1.py │ └── resultados/ │ ├── 01_validacion_mediciones.csv │ └── 01_incertidumbre_mediciones.csv │ ├── 📊 PUNTO_2_LISTAS_Y_NUMPY/ │ ├── README.md │ ├── codigo/ │ │ └── punto_2.py │ └── resultados/ │ ├── 02_comparacion_listas_numpy.csv │ └── 02_operaciones_numpy.csv │ ├── 📊 PUNTO_3_INDICADORES_KPI/ │ ├── README.md │ ├── codigo/ │ │ └── punto_3.py │ └── resultados/ │ ├── 03_kpi_indicadores.csv │ ├── 03_resumen_estado.csv │ └── 03_hallazgos_acciones.csv │ ├── 📊 PUNTO_4_MONTECARLO/ │ ├── README.md │ ├── codigo/ │ │ └── punto_4.py │ └── resultados/ │ ├── 04_montecarlo_5000_simulaciones.csv │ ├── 04_montecarlo_resumen.csv │ └── 04_montecarlo_campana_gauss.png │ ├── 📊 PUNTO_5_PROYECTO_FINAL/ │ ├── README.md │ ├── codigo/ │ │ └── punto_5.py │ └── resultados/ │ ├── 05_matriz_literatura.csv │ ├── 05_cronograma_proyecto.csv │ └── 05_indicadores_exito.csv │ ├── 📊 PUNTO_6_PROTOTIPO_LOVABLE/ │ ├── README.md │ ├── enlace_prototipo.txt │ └── capturas_pantalla/ │ ├── 📓 NOTEBOOKS/ │ └── proyecto_completo.ipynb │ ├── README.md ├── .gitignore ├── LICENSE └── requirements.txt


---

## 🎯 Resultados Principales

### Por Punto

| Punto | Métrica | Resultado |
|-------|---------|-----------|
| **1** | Operación normal | 86.7% ✅ |
| **2** | Aceleración NumPy | 2.77x ⚡ |
| **2** | Reducción memoria | 71.4% 💾 |
| **3** | KPIs en verde | 6/6 ✅ |
| **4** | Probabilidad agua | 81.5% 💧 |
| **4** | Simulaciones | 5,000 🔄 |
| **5** | Referencias | 10 (2020-2025) 📚 |
| **6** | Páginas web | 5 funcionales 🌐 |

---

## 📖 Cómo Revisar

### Para el Profesor: Flujo Recomendado

1. **Lee primero**: Este README
2. **Ve a DOCUMENTACION/**: Lee README_DOCUMENTACION.md
3. **Por cada punto**:
   - Abre carpeta `PUNTO_X_NOMBRE`
   - Lee `README.md` para contexto
   - Revisa carpeta `codigo/` para ver el código
   - Analiza carpeta `resultados/` para los CSV y gráficos
4. **Visualizaciones**: Abre los PNG en `PUNTO_4_MONTECARLO/resultados/`
5. **Prototipo**: Ve a `PUNTO_6_PROTOTIPO_LOVABLE/` para enlace web

### Para Estudiantes: Cómo Usar

1. Clona el repositorio
2. Ve a carpeta que te interese
3. Abre el `README.md` de esa carpeta
4. Ejecuta el código en `codigo/`
5. Revisa los resultados en `resultados/`

---

## ✅ Entregables Cumplidos

- [x] **1. Código Python** - En cada carpeta `PUNTO_X/codigo/`
- [x] **2. Evidencia listas/arreglos** - CSV en `PUNTO_2_LISTAS_Y_NUMPY/resultados/`
- [x] **3. Monte Carlo + interpretación** - PNG + CSV en `PUNTO_4_MONTECARLO/`
- [x] **4. Documento proyecto + literatura** - En `DOCUMENTACION/05_PROYECTO_FINAL.md`
- [x] **5. Prototipo Lovable** - En `PUNTO_6_PROTOTIPO_LOVABLE/`
- [x] **6. Consulta AWS** - En `DOCUMENTACION/07_DESPLIEGUE_AWS.md`
- [x] **7. Presentación** - En `DOCUMENTACION/` (disponible como PDF)

---

## 🛠️ Tecnologías

- **Python** 3.9+
- **NumPy** - Procesamiento numérico (2.77x más rápido)
- **Pandas** - Análisis de datos
- **Matplotlib/Seaborn** - Visualizaciones
- **SciPy** - Estadísticas y distribuiciones
- **React** - Prototipo web
- **AWS** - Arquitectura de despliegue

---

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Mediciones procesadas | 1,081,693 |
| Líneas de código | ~2,000+ |
| Archivos CSV | 12 |
| Gráficos generados | 5+ |
| Documentos | 7 |
| Referencias literatura | 10 |
| Cronograma proyecto | 12 meses |

---

## 📄 Licencia

MIT License - Ver LICENSE para detalles

---

## 👤 Autor

**Santiago Cano**
- Maestría en Automatización
- Curso: Fundamentos de Programación Científica
- Marzo 2026

---

## 🔗 Enlaces

- **GitHub**: https://github.com/santiagocano298366/ERT-Groundwater-Predictor-Pro
- **Documentación Completa**: Ver carpeta `DOCUMENTACION/`
- **Datos Completos**: Ver carpetas `PUNTO_X/resultados/`

---

**¿Preguntas?** Revisa la documentación en cada carpeta o contacta al autor.
