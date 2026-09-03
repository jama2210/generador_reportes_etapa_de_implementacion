import pandas as pd

from config import (
    NO_INFO_TEXT,
    MODALITY_MAPPING
)

from generator.utils import (
    clean_empty_value,
    normalize_text
)


class DataCleaner:

    @staticmethod
    def remove_not_applicable(df):

        replacements = [
            "No aplica",
            "NO APLICA",
            "No Aplica",
            "N/A",
            "NA"
        ]

        return df.replace(
            replacements,
            "",
            regex=False
        )

    @staticmethod
    def clean_dataframe(df):

        df = df.copy()

        for column in df.columns:

            df[column] = df[column].apply(
                clean_empty_value
            )

        return df

    @staticmethod
    def normalize_modality(value):

        normalized = normalize_text(value)

        return MODALITY_MAPPING.get(
            normalized,
            str(value).strip()
        )

    @staticmethod
    def normalize_modalities(df, column_name):

        if column_name not in df.columns:
            return df

        df[column_name] = df[column_name].apply(
            DataCleaner.normalize_modality
        )

        return df

    @staticmethod
    def replace_empty_supervisor(df, supervisor_column):

        if supervisor_column not in df.columns:
            return df

        df[supervisor_column] = df[
            supervisor_column
        ].replace(
            "",
            NO_INFO_TEXT
        )

        return df

    def normalize_date(value):

        try:

            date = pd.to_datetime(
                value,
                errors="coerce",
                dayfirst=True
            )

            if pd.isna(date):

                return None

            return date

        except Exception:

            return None

    @staticmethod
    def sort_records(
        df,
        date_column,
        id_column="ID"
    ):

        temp = df.copy()

        temp["_sort_date"] = temp[
            date_column
        ].apply(
            DataCleaner.normalize_date
        )

        if id_column in temp.columns:

            temp = temp.sort_values(
                by=[
                    "_sort_date",
                    id_column
                ],
                ascending=True
            )

        else:

            temp = temp.sort_values(
                by="_sort_date"
            )

        return temp.drop(
            columns="_sort_date"
        )

