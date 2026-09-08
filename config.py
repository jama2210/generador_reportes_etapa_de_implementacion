from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"

LOGO_PATH = ASSETS_DIR / "logo_institucional.png"

NO_INFO_TEXT = "No informado en el formulario"

# =========================================
# COLUMNAS CRÍTICAS
# =========================================

COL_REGION = "Indique su región"
COL_DEPROV = "DEPROV"
COL_SUPERVISOR = "SUPERVISOR"
COL_MODALIDAD = "TIPO ASESORÍA"
COL_FECHA = "Indique la fecha de realización de la asesoría (2)"
COL_NOMBRE_ASESORIA = "NOMBRE ASESORÍA"

# Se utiliza supervisor como asesor por defecto
COL_ASESOR = COL_SUPERVISOR

REQUIRED_COLUMNS = [
    COL_REGION,
    COL_DEPROV,
    COL_SUPERVISOR,
    COL_MODALIDAD,
    COL_FECHA
]

# =========================================
# MODALIDADES CONOCIDAS
# =========================================

MODALITY_MAPPING = {
    "directa ee": "Directa EE",
    "red ee": "Red EE",
    "ee pade": "EE PADE",
}

# =========================================
# COLORES INSTITUCIONALES
# =========================================

INSTITUTIONAL_COLORS = {

    "primary": "006FB3",
    "secondary": "FE6565",
    "tertiary": "0A132D",
    "accent": "A8B7C7",
    "neutral": "EEEEEE",

    "gray_a": "4A4A4A",
    "gray_b": "8A8A8A",

    "black": "111111",
    "white": "FFFFFF"
}

# =========================================
# LONGITUDES
# =========================================

MAX_FILENAME_LENGTH = 120
MAX_FOLDERNAME_LENGTH = 100

SECTION_DISPLAY_NAMES = {

    "identificacion":
        "Identificación",

    "nivelacion":
        "Nivelación de Aprendizajes",

    "liderazgo":
        "Liderazgo Pedagógico",

    "asistencia":
        "Asistencia y Cultura Escolar",

    "nudos_criticos":
        "Nudos Críticos",

    "segundo_basico":
        "Segundo Básico",

    "cuarto_basico":
        "Cuarto Básico",

    "septimo_basico":
        "Séptimo Básico",

    "primero_medio":
        "Primero Medio",

    "visitas":
        "Visitas y Acompañamiento",

    "pade":
        "Monitoreo PADE",

    "informacion_adicional":
        "Información Adicional"
}


# ==========================================
# SECCIONES POR MODALIDAD
# ==========================================

MODALITY_SECTIONS = {

    "Directa EE": [
        "identificacion",
        "nivelacion",
        "liderazgo",
        "asistencia",
        "nudos_criticos",
        "segundo_basico",
        "cuarto_basico",
        "septimo_basico",
        "primero_medio",
        "visitas",
        "informacion_adicional"
    ],

    "Red EE": [
        "identificacion",
        "nivelacion",
        "asistencia",
        "nudos_criticos",
        "segundo_basico",
        "cuarto_basico",
        "septimo_basico",
        "primero_medio",
        "visitas",
        "informacion_adicional"
    ],

    "Monitoreo SLEP PADE": [
        "identificacion",
        "pade"
    ],

    "EE PADE": [
        "identificacion",
        "nivelacion",
        "liderazgo",
        "asistencia",
        "nudos_criticos",
        "segundo_basico",
        "cuarto_basico",
        "septimo_basico",
        "primero_medio",
        "visitas",
        "informacion_adicional"
    ]
}