"""Build the Deel PDF from its single-source, ATS-friendly Markdown draft."""

from io import BytesIO
from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "jobs" / "deel" / "targeted-resume.md"
OUTPUT_PATH = (
    ROOT / "output" / "deel" / "Muhammad_Adeel_Senior_Frontend_Engineer_Deel.pdf"
)

BODY = ParagraphStyle(
    "body", fontName="Helvetica", fontSize=9, leading=11.4, spaceAfter=3
)
STYLES = {
    "body": BODY,
    "name": ParagraphStyle(
        "name", parent=BODY, fontName="Helvetica-Bold", fontSize=19,
        leading=22, alignment=TA_CENTER, spaceAfter=4,
    ),
    "contact": ParagraphStyle(
        "contact", parent=BODY, fontSize=8.7, leading=11,
        alignment=TA_CENTER, spaceAfter=2,
    ),
    "tagline": ParagraphStyle(
        "tagline", parent=BODY, alignment=TA_CENTER, fontSize=10,
        leading=13, spaceAfter=4,
    ),
    "section": ParagraphStyle(
        "section", parent=BODY, fontName="Helvetica-Bold", fontSize=10.5,
        leading=13, spaceBefore=7, spaceAfter=2, keepWithNext=True,
    ),
    "role": ParagraphStyle(
        "role", parent=BODY, fontName="Helvetica-Bold", fontSize=9.5,
        leading=12, spaceBefore=5, keepWithNext=True,
    ),
    "project": ParagraphStyle(
        "project", parent=BODY, fontName="Helvetica-Bold", spaceBefore=4,
        keepWithNext=True,
    ),
    "date": ParagraphStyle(
        "date", parent=BODY, fontName="Helvetica-Oblique", keepWithNext=True,
    ),
    "bullet": ParagraphStyle(
        "bullet", parent=BODY, leftIndent=10, firstLineIndent=0,
        bulletIndent=0,
    ),
}


def inline(text):
    """Escape source text before translating the supported emphasis markers."""
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)


def make_story(source):
    story = []
    in_header = True
    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), STYLES["name"]))
        elif line.startswith("## "):
            in_header = False
            story.append(Paragraph(inline(line[3:]), STYLES["section"]))
            rule = HRFlowable(
                width="100%", thickness=0.6, color=colors.HexColor("#333333"),
                spaceAfter=4,
            )
            rule.keepWithNext = True
            story.append(rule)
        elif line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), STYLES["role"]))
        elif line.startswith("#### "):
            story.append(Paragraph(inline(line[5:]), STYLES["project"]))
        elif line.startswith("- "):
            story.append(Paragraph(
                inline(line[2:]), STYLES["bullet"], bulletText="\u2022"
            ))
        elif in_header:
            style = "tagline" if line.startswith("**") else "contact"
            story.append(Paragraph(inline(line), STYLES[style]))
        else:
            style = "date" if line.startswith("*") and not line.startswith("**") else "body"
            story.append(Paragraph(inline(line), STYLES[style]))
    story.append(Spacer(1, 2))
    return story


def build(
    source_path=SOURCE_PATH,
    output_path=OUTPUT_PATH,
    title="Muhammad Adeel - Senior Frontend Engineer - Deel",
):
    source = source_path.read_text(encoding="utf-8")
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=LETTER, leftMargin=38, rightMargin=38,
        topMargin=30, bottomMargin=30,
        title=title,
        author="Muhammad Adeel",
    )
    doc.build(make_story(source))
    if not 1 <= doc.page <= 2:
        raise ValueError(f"Resume must be 1-2 pages; generated {doc.page}.")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(buffer.getvalue())
    print(f"Wrote {output_path} ({doc.page} pages)")


if __name__ == "__main__":
    build()
