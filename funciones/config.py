"""Configuración centralizada de rutas y parámetros de negocio del proyecto (Bogotá)."""

from pathlib import Path
import sqlite3

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

DATOS_DIR = BASE_DIR / "datos"
DATOS_BRUTOS_DIR = DATOS_DIR / "brutos"
DATOS_INTERMEDIOS_DIR = DATOS_DIR / "intermedios"
DATOS_PROCESADOS_DIR = DATOS_DIR / "procesados"
DATOS_REFERENCIA_MADRID_DIR = DATOS_DIR / "referencia_madrid"

DOCS_DIR = BASE_DIR / "docs"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"

ENTREGABLES_DIR = BASE_DIR / "entregables"
ENTREGABLES_GRAFICOS_DIR = ENTREGABLES_DIR / "graficos"
ENTREGABLES_INFORMES_DIR = ENTREGABLES_DIR / "informes"
ENTREGABLES_DASHBOARDS_DIR = ENTREGABLES_DIR / "dashboards"

# Fuentes de datos — Inside Airbnb Bogotá (corte 2026-09-14)
FECHA_CORTE_AIRBNB = "2026-09-14"
URL_LISTINGS_SUMMARY_BOGOTA = (
    "https://data.insideairbnb.com/colombia/dc/bogot%C3%A1/2026-09-14/visualisations/listings.csv"
)
URL_LISTINGS_BOGOTA = (
    "https://data.insideairbnb.com/colombia/dc/bogot%C3%A1/2026-09-14/data/listings.csv.gz"
)
URL_REVIEWS_BOGOTA = (
    "https://data.insideairbnb.com/colombia/dc/bogot%C3%A1/2026-09-14/data/reviews.csv.gz"
)

# Archivos de datos principales (Bogotá)
LISTINGS_SUMMARY_RAW_PATH = DATOS_BRUTOS_DIR / "listings.csv"
LISTINGS_RAW_PATH = DATOS_BRUTOS_DIR / "listings.csv.gz"
REVIEWS_RAW_PATH = DATOS_BRUTOS_DIR / "reviews.csv.gz"
PRECIOS_M2_PATH = DATOS_BRUTOS_DIR / "precios_m2_bogota.csv"
POI_BOGOTA_CSV_PATH = DATOS_BRUTOS_DIR / "poi_bogota.csv"
DB_PATH = DATOS_INTERMEDIOS_DIR / "mercado_inmobiliario_bogota.db"

# Parámetros de negocio (Enfoque Analítico)
CIUDAD_OBJETIVO = "Bogotá"
PAIS_OBJETIVO = "Colombia"
MONEDA = "COP"
BOGOTA_COORDS = (4.6533, -74.0836)

# Ventaja competitiva: capacidad de negociación del 25% de descuento sobre precio de mercado
DESCUENTO_NEGOCIACION = 0.25
FACTOR_COMPRA_NETO = 1.0 - DESCUENTO_NEGOCIACION  # 0.75


def get_db_connection(db_path: Path = DB_PATH) -> sqlite3.Connection:
    """Devuelve una conexión SQLite a la base de datos del proyecto."""
    return sqlite3.connect(db_path)
