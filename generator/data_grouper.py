class DataGrouper:

    @staticmethod
    def group_records(
        df,
        region_col,
        deprov_col,
        modality_col,
        supervisor_col
    ):

        grouped = df.groupby(
            [
                region_col,
                deprov_col,
                modality_col,
                supervisor_col
            ],
            dropna=False
        )

        return grouped

    @staticmethod
    def count_reports(grouped):

        return len(grouped)

    @staticmethod
    def count_records(df):

        return len(df)