import zipfile
from io import BytesIO


class ZipGenerator:

    @staticmethod
    def build_zip(documents):

        zip_buffer = BytesIO()

        with zipfile.ZipFile(
            zip_buffer,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zip_file:

            for item in documents:

                zip_file.writestr(
                    item["path"],
                    item["content"].getvalue()
                )

        zip_buffer.seek(0)

        return zip_buffer