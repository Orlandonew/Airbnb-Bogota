# Arquitectura del Proyecto y Mapeo Metodológico — Bogotá (Colombia)

Este documento conecta los pilares del **Enfoque Analítico** y las **4 fases operativas** con los recursos técnicos, fuentes de datos de **Bogotá** y KPIs del repositorio.

---

## 1. Pilares del Enfoque Analítico

| Pilar | Traducción técnica en el proyecto (Bogotá) | Recursos principales |
| :--- | :--- | :--- |
| **Análisis de datos Airbnb** | Evaluación de oferta, precios por noche (COP), ocupación estimada (`estimated_occupancy_l365d`), disponibilidad (`availability_365`) y demanda histórica/estacionalidad a partir de reseñas por localidad y barrio de Bogotá. | `datos/brutos/listings.csv`, `datos/brutos/listings.csv.gz`, `datos/brutos/reviews.csv.gz`, `docs/urls_datos.md` |
| **Business Analytics** | Segmentación por tipología (`room_type`, `bedrooms`, `accommodates`, `beds`), minicubos unidimensionales, análisis temporal de demanda con `reviews.csv.gz` y scoring de ubicación (POIs de Bogotá). | `docs/metodologia_minicubos.md`, `funciones/funciones.py` |
| **Optimización de KPIs** | Medición y optimización de días de ocupación anual, precio por noche (ADR), volumen/tendencia de reseñas, ingreso anual estimado, coste de adquisición y margen bruto. | `docs/proyecto-objetivos.md`, `funciones/config.py` |
| **Ventaja competitiva (25% dto.)** | Aplicación sistemática del factor neto de compra (`FACTOR_COMPRA_NETO = 0.75`) sobre el precio de mercado por m² (COP/m²) en Bogotá. | `funciones/config.py` (`DESCUENTO_NEGOCIACION = 0.25`), `datos/brutos/precios_m2_bogota.csv` *(por incorporar)* |

---

## 2. Roadmap por Fases

### Fase 1 — Discovery & Análisis (`notebooks/01_discovery_analisis.ipynb`)
- **Propósito:** Identificar oportunidades iniciales mediante el análisis de datos del mercado turístico de Bogotá.
- **Entradas:** `datos/brutos/listings.csv`, `datos/brutos/listings.csv.gz` y `datos/brutos/reviews.csv.gz` (corte Inside Airbnb `2026-09-14`).
- **Alcance:** Auditoría de calidad de datos, limpieza, exploración de precios (COP/noche), ocupación, competencia por localidad/barrio y evolución temporal de la demanda vía `reviews.csv.gz`.
- **Salidas esperadas:** Base limpia consolidada en `datos/intermedios/mercado_inmobiliario_bogota.db` y gráficos exploratorios en `entregables/graficos/`.

### Fase 2 — Due Diligence (`notebooks/02_due_diligence.ipynb`)
- **Propósito:** Evaluar en detalle el potencial de rentabilidad por ubicación y tipología de inmueble en Bogotá.
- **Entradas:** Tablas procesadas en `datos/intermedios/mercado_inmobiliario_bogota.db`, reseñas agregadas por anuncio y (opcionalmente) `datos/brutos/poi_bogota.csv`.
- **Metodología:** Ingeniería de variables, construcción de KPIs, minicubos BA por localidad/barrio/tipología y análisis geoespacial.
- **Salidas esperadas:** Tablón analítico final en `datos/procesados/` y rankings/mapas de rentabilidad y ocupación en `entregables/graficos/`.

### Fase 3 — Adquisición Estratégica (`notebooks/03_adquisicion_estrategica.ipynb`)
- **Propósito:** Compra con **25% de descuento** sobre precio de mercado y optimización del **precio/m²** por zona en Bogotá.
- **Entradas:** Resultados de Due Diligence + precios de compra por m² en Bogotá (`datos/brutos/precios_m2_bogota.csv`) + `FACTOR_COMPRA_NETO = 0.75`.
- **Metodología:** Modelización de coste de adquisición con 25% de descuento, relación coste vs. ingreso/margen y matriz de priorización de localidades/barrios y tipologías.
- **Salidas esperadas:** Informe de recomendaciones de adquisición en `entregables/informes/`.

### Fase 4 — Gestión & Optimización (`notebooks/04_gestion_optimizacion.ipynb`)
- **Propósito:** Maximización de ocupación y **pricing dinámico** para optimizar ingresos de la cartera en Bogotá.
- **Entradas:** Tablón analítico de Bogotá + estacionalidad extraída de `reviews.csv.gz`.
- **Metodología:** Elasticidad precio–ocupación, detección de temporadas altas/bajas por localidad/tipología, bandas de pricing dinámico y seguimiento de KPIs.
- **Salidas esperadas:** Reglas de pricing dinámico y panel/informe de seguimiento en `entregables/dashboards/` y `entregables/informes/`.
