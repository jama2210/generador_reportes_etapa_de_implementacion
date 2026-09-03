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
    "red ee": "Red EE"
}

# =========================================
# COLORES INSTITUCIONALES
# =========================================

INSTITUTIONAL_COLORS = {
    "primary": "003DA5",
    "secondary": "D52B1E",
    "text": "333333",
    "light": "F2F2F2"
}

# =========================================
# LONGITUDES
# =========================================

MAX_FILENAME_LENGTH = 120
MAX_FOLDERNAME_LENGTH = 100