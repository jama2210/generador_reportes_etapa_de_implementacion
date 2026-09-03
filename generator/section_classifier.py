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
        "fecha de realizacion"
    ],

    "nivelacion": [
        "nivelacion",
        "aprendizaje",
        "brechas de aprendizaje"
    ],

    "liderazgo": [
        "liderazgo",
        "acompanamiento"
    ],

    "asistencia": [
        "asistencia",
        "cultura escolar"
    ],

    "nudos_criticos": [
        "nudo",
        "apoyo requerido"
    ],

    "visitas": [
        "visita",
        "evidencia presentada",
        "medio de verificacion",
        "compromiso"
    ],

    "pade": [
        "pade",
        "slep",
        "nivel de avance",
        "obstaculo"
    ],

    "segundo_basico": [
        "2 basico"
    ],

    "cuarto_basico": [
        "4 basico"
    ],

    "septimo_basico": [
        "7 basico"
    ],

    "primero_medio": [
        "1 medio"
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