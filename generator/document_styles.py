from docx.shared import Pt
from docx.shared import RGBColor

from config import INSTITUTIONAL_COLORS


def apply_document_styles(document):

    styles = document.styles

    normal = styles["Normal"]

    normal.font.name = "Aptos"
    normal.font.size = Pt(10)

    return document


def format_title(paragraph):

    run = paragraph.runs[0]

    run.font.name = "Aptos"
    run.font.size = Pt(22)

    run.font.bold = True

    run.font.color.rgb = RGBColor(
        0,
        61,
        165
    )


def format_heading(paragraph):

    run = paragraph.runs[0]

    run.font.name = "Aptos"

    run.font.bold = True

    run.font.size = Pt(15)
