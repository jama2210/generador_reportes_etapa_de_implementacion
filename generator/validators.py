from generator.utils import normalize_for_matching


REQUIRED_COLUMNS = {
    "region":
        "Indique su región",

    "deprov":
        "DEPROV",

    "supervisor":
        "SUPERVISOR",

    "modalidad":
        "TIPO ASESORÍA",

    "fecha":
        "Indique la fecha de realización de la asesoría (2)"
}


class ExcelValidator:

    @staticmethod
    def validate(df):

        normalized_columns = {
            normalize_for_matching(col): col
            for col in df.columns
        }

        missing = []

        for expected in REQUIRED_COLUMNS.values():

            normalized_expected = normalize_for_matching(
                expected
            )

            exists = False

            for current in normalized_columns:

                if normalized_expected in current:
                    exists = True
                    break

            if not exists:

                missing.append(expected)

        return missing