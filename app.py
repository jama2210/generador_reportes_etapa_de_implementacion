import streamlit as st

from generator.excel_reader import ExcelReader
from generator.validators import ExcelValidator
from generator.data_cleaner import DataCleaner
from generator.data_grouper import DataGrouper
from generator.document_generator import DocumentGenerator
from generator.zip_generator import ZipGenerator

from generator.utils import (
    sanitize_foldername,
    sanitize_filename
)

from config import (
    COL_REGION,
    COL_DEPROV,
    COL_MODALIDAD,
    COL_SUPERVISOR
)

st.set_page_config(
    page_title="Generador de Informes",
    layout="wide"
)

st.title(
    "Generador de Informes\nEtapa de Implementación de la Asesoría"
)

uploaded_file = st.file_uploader(
    "Cargar archivo Excel",
    type=["xlsx"]
)

if uploaded_file:

    reader = ExcelReader()

    df = reader.read_excel(
        uploaded_file
    )

    missing = ExcelValidator.validate(
        df
    )

    if missing:

        st.error(
            "Faltan columnas obligatorias:"
        )

        for item in missing:
            st.write(f"- {item}")

        st.stop()

    df = DataCleaner.clean_dataframe(df)

    df = DataCleaner.remove_not_applicable(df)

    total_registros = len(df)

    total_supervisores = (
        df[COL_SUPERVISOR]
        .nunique()
    )

    total_regiones = (
        df[COL_REGION]
        .nunique()
    )

    total_deprov = (
        df[COL_DEPROV]
        .nunique()
    )

    total_modalidades = (
        df[COL_MODALIDAD]
        .nunique()
    )

    st.subheader("Resumen")

    col1,col2,col3,col4,col5 = st.columns(5)

    col1.metric(
        "Registros",
        total_registros
    )

    col2.metric(
        "Supervisores",
        total_supervisores
    )

    col3.metric(
        "Regiones",
        total_regiones
    )

    col4.metric(
        "DEPROV",
        total_deprov
    )

    col5.metric(
        "Modalidades",
        total_modalidades
    )

    grouped = DataGrouper.group_records(
        df,
        COL_REGION,
        COL_DEPROV,
        COL_MODALIDAD,
        COL_SUPERVISOR
    )

    report_count = len(grouped)

    st.info(
        f"Se generarán {report_count} informes."
    )

    if st.button(
        "Generar Informes"
    ):

        documents = []

        generator = DocumentGenerator()

        for group_key, group_df in grouped:

            (
                region,
                deprov,
                modalidad,
                supervisor
            ) = group_key

            group_df = DataCleaner.sort_records(
                group_df,
                "Indique la fecha de realización de la asesoría (2)"
            )

            doc = generator.generate_document(
                group_df,
                {
                    "region": region,
                    "deprov": deprov,
                    "modalidad": modalidad,
                    "supervisor": supervisor
                }
            )

            doc_path = (
                f"Informes_Etapa_Implementacion/"
                f"{sanitize_foldername(region)}/"
                f"{sanitize_foldername(deprov)}/"
                f"{sanitize_foldername(modalidad)}/"
                f"Informe_{sanitize_filename(supervisor)}.docx"
            )

            documents.append({
                "path": doc_path,
                "content": doc
            })

        zip_buffer = ZipGenerator.build_zip(
            documents
        )

        st.success(
            "Informes generados correctamente."
        )

        st.download_button(
            "📥 Descargar ZIP",
            data=zip_buffer,
            file_name="Informes_Etapa_Implementacion_Asesoria.zip",
            mime="application/zip"
        )