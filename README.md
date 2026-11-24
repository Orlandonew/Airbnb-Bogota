# Proyecto de Inversión Inmobiliaria — Alquiler Turístico (Airbnb Bogotá)

Proyecto estructurado de **Business Analytics e inversión inmobiliaria** orientado a identificar las tipologías de inmuebles y zonas geográficas con mayor potencial comercial para el alquiler turístico en **Bogotá (Colombia)**, partiendo de los datos públicos de **Inside Airbnb** (`listings.csv.gz` y `reviews.csv.gz`, corte `2026-09-14`).

---

## Enfoque Analítico

1. **Análisis de datos Airbnb:** Evaluación de ocupación, precios (COP), demanda y estacionalidad por zonas geográficas (localidades y barrios de Bogotá) utilizando `listings.csv.gz` y `reviews.csv.gz`.
2. **Business Analytics:** Aplicación de metodologías analíticas (minicubos, segmentación, análisis temporal de reseñas y análisis geoespacial) para identificar tipologías de inmuebles con mayor potencial comercial.
3. **Optimización de KPIs:** Monitorización de días de ocupación anual, precio por noche y costes de adquisición para maximizar rentabilidad.
4. **Ventaja competitiva:** Capacidad de negociación del **25% de descuento** sobre precios de mercado en la adquisición de activos.

---

## Fases del Proyecto

| Fase | Notebook de trabajo | Objetivo principal |
| :--- | :--- | :--- |
| **1. Discovery & Análisis** | `notebooks/01_discovery_analisis.ipynb` | Identificación de oportunidades mediante análisis de datos de mercado turístico de Bogotá (`listings` + `reviews`). |
| **2. Due Diligence** | `notebooks/02_due_diligence.ipynb` | Evaluación detallada del potencial de rentabilidad por ubicación y tipología. |
| **3. Adquisición Estratégica** | `notebooks/03_adquisicion_estrategica.ipynb` | Compra con descuentos del 25% y optimización del precio/m² por zona en Bogotá. |
| **4. Gestión & Optimización** | `notebooks/04_gestion_optimizacion.ipynb` | Maximización de ocupación y pricing dinámico (apoyado en estacionalidad de reseñas) para optimizar ingresos. |

> **Estado actual:** Proyecto estructurado y configurado para **Bogotá**, con los datasets de Inside Airbnb descargados en `datos/brutos/` y sin análisis ejecutados todavía.

---

## Estructura del Proyecto

```text
Inmobiliaria/
├── README.md                              # Visión general y guía del proyecto (Bogotá)
├── requirements.txt                       # Dependencias Python del proyecto
├── .gitignore                             # Reglas de exclusión para Git
├── datos/
│   ├── brutos/                            # Fuentes originales de Bogotá sin modificar
│   │   ├── listings.csv                   # Inside Airbnb Bogotá (2026-09-14) — resumen alojamientos
│   │   ├── listings.csv.gz                # Inside Airbnb Bogotá (2026-09-14) — detalle alojamientos
│   │   └── reviews.csv.gz                 # Inside Airbnb Bogotá (2026-09-14) — reseñas detalladas
│   ├── intermedios/                       # Base SQLite limpia de Bogotá (por generar en Fase 1)
│   ├── procesados/                        # Tablones analíticos finales de Bogotá
│   └── referencia_madrid/                 # Datos del caso original de Madrid (aislados como respaldo)
├── docs/
│   ├── arquitectura_proyecto.md           # Mapeo del enfoque analítico y las 4 fases a Bogotá
│   ├── urls_datos.md                      # Enlaces oficiales de Inside Airbnb Bogotá y notas de datos
│   ├── proyecto-objetivos.md              # Marco de objetivos, palancas, KPIs y preguntas semilla
│   ├── metodologia_minicubos.md           # Referencia metodológica de minicubos BA
│   └── guia_inicio_proyecto.md            # Guía original de inicialización del proyecto
├── funciones/
│   ├── __init__.py                        # Exportaciones del paquete
│   ├── config.py                          # Rutas, URLs de Bogotá y parámetros de negocio (25% dto.)
│   └── funciones.py                       # Utilidades geoespaciales (Haversine, atractivo turístico, mapas)
├── notebooks/
│   ├── 01_discovery_analisis.ipynb        # Plantilla Fase 1: Discovery & Análisis (Bogotá)
│   ├── 02_due_diligence.ipynb             # Plantilla Fase 2: Due Diligence (Bogotá)
│   ├── 03_adquisicion_estrategica.ipynb   # Plantilla Fase 3: Adquisición Estratégica (Bogotá)
│   ├── 04_gestion_optimizacion.ipynb      # Plantilla Fase 4: Gestión & Optimización (Bogotá)
│   └── referencia/                        # Notebooks de respaldo originales (caso Madrid)
└── entregables/
    ├── graficos/                          # Gráficos y mapas generados para Bogotá
    ├── informes/                          # Informes ejecutivos generados para Bogotá
    ├── dashboards/                        # Dashboards interactivos
    └── referencia/                        # Entregables de respaldo originales (caso Madrid)
```

---

## Inventario de Datos Activos (Bogotá)

- **`datos/brutos/listings.csv`** (~3,6 MB): Tabla resumen de anuncios de Airbnb en Bogotá (corte `2026-09-14`).
- **`datos/brutos/listings.csv.gz`** (~10,5 MB): Detalle completo de anuncios de Airbnb en Bogotá (corte `2026-09-14`).
- **`datos/brutos/reviews.csv.gz`** (~49,9 MB): Histórico completo de reseñas por alojamiento en Bogotá (corte `2026-09-14`), útil para análisis de demanda, actividad real y estacionalidad.
- **Datos complementarios previstos** (cuando avancemos a Fase 2 / Fase 3):
  - `datos/brutos/precios_m2_bogota.csv`: Precio de venta por m² (COP/m²) por localidad/barrio de Bogotá.
  - `datos/brutos/poi_bogota.csv`: Puntos de interés turístico y corporativo de Bogotá para scoring geoespacial.

---

## Puesta en Marcha del Entorno

```bash
pip install -r requirements.txt
```

Todos los parámetros de negocio y rutas para Bogotá se centralizan en `funciones/config.py`.
