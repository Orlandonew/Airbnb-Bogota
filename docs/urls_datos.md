# Fuentes y URLs de Datos — Proyecto Bogotá

## Inside Airbnb — Bogotá, Colombia (Corte: 2026-09-14)
- **listings.csv** (resumen visualizaciones): https://data.insideairbnb.com/colombia/dc/bogot%C3%A1/2026-09-14/visualisations/listings.csv
- **listings.csv.gz** (detalle completo de alojamientos): https://data.insideairbnb.com/colombia/dc/bogot%C3%A1/2026-09-14/data/listings.csv.gz
- **reviews.csv.gz** (histórico detallado de reseñas): https://data.insideairbnb.com/colombia/dc/bogot%C3%A1/2026-09-14/data/reviews.csv.gz

### Archivos locales descargados (`datos/brutos/`)
- `datos/brutos/listings.csv` (~3,6 MB)
- `datos/brutos/listings.csv.gz` (~10,5 MB)
- `datos/brutos/reviews.csv.gz` (~49,9 MB)

### Fuentes complementarias planificadas para Bogotá (opcionales según fase)
- `datos/brutos/precios_m2_bogota.csv` *(pendiente de incorporar)*: Precio medio de venta por m² (COP/m²) por localidad/barrio de Bogotá (ej. Catastro Bogotá / portales inmobiliarios) para los cálculos de Fase 2 y Fase 3 con 25% de descuento.
- `datos/brutos/poi_bogota.csv` *(pendiente de incorporar)*: Puntos de interés turístico y empresarial de Bogotá (`name, lat, lon, weight, category`) para el índice de atractivo turístico.

---

## Referencia histórica (Caso original Madrid)
Conservada únicamente como documentación de referencia en `datos/referencia_madrid/` y `notebooks/referencia/`:
- Inside Airbnb Madrid `listings.csv`: https://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2025-06-12/visualisations/listings.csv
- Inside Airbnb Madrid `listings.csv.gz`: https://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2025-06-12/data/listings.csv.gz
- Idealista Madrid (venta €/m²): https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/madrid-comunidad/madrid-provincia/madrid/
