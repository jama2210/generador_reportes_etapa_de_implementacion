import re
import unicodedata
import pandas as pd

from config import (
    NO_INFO_TEXT,
    MAX_FILENAME_LENGTH,
    MAX_FOLDERNAME_LENGTH
)

def has_real_content(value):

    if value is None:
        return False

    value = str(value).strip()

    if not value:
        return False

    invalid_values = {
        "",
        "nan",
        "none",
        "nat",
        "no informado en el formulario",
        "<br>",
        "<br><br>"
    }

    return value.lower() not in invalid_values


def is_not_applicable(value):

    if value is None:
        return True

    value = str(value).strip().lower()

    patterns = [
        "no aplica",
        "n/a",
        "na"
    ]

    return value in patterns

def normalize_text(text):
    """
    Normaliza texto para comparación.
    """

    if pd.isna(text):
        return ""

    text = str(text)

    text = text.strip()

    text = unicodedata.normalize("NFKD", text)

    text = "".join(
        c for c in text
        if not unicodedata.combining(c)
    )

    text = re.sub(r"\s+", " ", text)

    return text.lower()


def normalize_column_name(column_name):
    """
    Normaliza nombres de columnas.
    """

    if column_name is None:
        return ""

    column_name = str(column_name)

    column_name = column_name.replace("\n", " ")

    column_name = re.sub(r"\s+", " ", column_name)

    return column_name.strip()


def clean_empty_value(value):
    """
    Convierte vacíos a texto institucional.
    """

    if pd.isna(value):
        return NO_INFO_TEXT

    value = str(value).strip()

    if not value:
        return NO_INFO_TEXT

    return value


def sanitize_path_name(name, max_length=100):
    """
    Limpia nombres de carpetas y archivos.
    """

    name = clean_empty_value(name)

    invalid_chars = r'[\\/:*?"<>|]'

    name = re.sub(invalid_chars, "_", name)

    name = unicodedata.normalize("NFKD", name)

    name = "".join(
        c for c in name
        if not unicodedata.combining(c)
    )

    name = re.sub(r"\s+", " ", name)

    name = name.strip()

    return name[:max_length]


def sanitize_filename(name):
    return sanitize_path_name(
        name,
        MAX_FILENAME_LENGTH
    )


def sanitize_foldername(name):
    return sanitize_path_name(
        name,
        MAX_FOLDERNAME_LENGTH
    )


def format_chilean_date(value):
    """
    Formato DD-MM-YYYY
    """

    if pd.isna(value):
        return NO_INFO_TEXT

    try:
        date_obj = pd.to_datetime(
            value,
            dayfirst=True,
            errors="coerce"
        )

        if pd.isna(date_obj):
            return str(value)

        return date_obj.strftime("%d-%m-%Y")

    except Exception:
        return str(value)


def split_multiselect(value):
    """
    Convierte selecciones múltiples a lista.
    """

    value = clean_empty_value(value)

    if value == NO_INFO_TEXT:
        return [value]

    separators = [
        ";",
        ",",
        "|",
        "\n"
    ]

    values = [value]

    for sep in separators:

        new_values = []

        for item in values:
            new_values.extend(item.split(sep))

        values = new_values

    values = [
        item.strip()
        for item in values
        if item.strip()
    ]

    return values

import re


def make_friendly_label(text):

    if not text:
        return "Campo sin nombre"

    text = str(text)

    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text.capitalize()

def normalize_for_matching(text):

    text = normalize_text(text)

    text = text.replace("º", "")

    text = text.replace("°", "")

    return text
