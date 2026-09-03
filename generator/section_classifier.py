from generator.utils import normalize_for_matching


SECTION_PATTERNS = {

    "identificacion": [
        "id",
        "correo",
        "supervisor",
        "region",
        "deprov",
        "tipo asesoria",
        "nombre asesoria",
        "fecha"
    ],

    "nivelacion": [
        "nivelacion de aprendizajes"
    ],

    "liderazgo": [
        "liderazgo pedagogico",
        "acompanamiento"
    ],

    "asistencia": [
        "asistencia y cultura escolar"
    ],

    "nudos_criticos": [
        "nudo"
    ],

    "segundo_basico": [
        "2 basico",
        "2o basico",
        "2 básico"
    ],

    "cuarto_basico": [
        "4 basico",
        "4o basico",
        "4 básico"
    ],

    "septimo_basico": [
        "7 basico",
        "7o basico",
        "7 básico"
    ],

    "primero_medio": [
        "1 medio",
        "1o medio",
        "1º año medio"
    ],

    "visitas": [
        "visitas de acompanamiento",
        "evidencias presentadas",
        "medio de verificacion",
        "compromiso"
    ],

    "pade": [
        "slep",
        "nivel de avance",
        "obstaculo",
        "implementacion del pade"
    ]
}


class SectionClassifier:

    @staticmethod
    def classify_column(column_name):

        normalized = normalize_for_matching(
            column_name
        )

        for section, patterns in SECTION_PATTERNS.items():

            for pattern in patterns:

                if pattern in normalized:

                    return section

        return "informacion_adicional"

    @staticmethod
    def build_section_map(columns):

        result = {}

        for col in columns:

            section = SectionClassifier.classify_column(col)

            result.setdefault(
                section,
                []
            ).append(col)

        return result