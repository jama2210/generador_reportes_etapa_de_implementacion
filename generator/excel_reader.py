import pandas as pd

from generator.utils import (
    normalize_column_name
)


class ExcelReader:

    def __init__(self):

        self.column_mapping = {}

    def read_excel(self, uploaded_file):

        df = pd.read_excel(
            uploaded_file,
            engine="openpyxl"
        )

        self.column_mapping = {
            col: normalize_column_name(col)
            for col in df.columns
        }

        return df

    def get_normalized_columns(self):

        return self.column_mapping