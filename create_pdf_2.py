import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def create_pdf():
    df = pd.read_csv("topics.csv")
    pdf_file = 'output_2.pdf'
    can = canvas.Canvas(pdf_file, pagesize=A4)

    for index, item in df.iterrows():
        topic = item["Topic"]

        can.setFont('Helvetica-Bold', 20)

        can.drawString(20, 800, topic)
        can.line(0.25 * inch, 10.9 * inch, 8 * inch, 10.9 * inch)

        can.setFont('Times-BoldItalic', 10)
        can.setFillColor("gray")
        can.drawRightString(7.80 * inch, 0.25 * inch, topic)

        can.showPage()
        for page in range(item["Pages"] - 1):

            can.setFont('Times-BoldItalic', 10)
            can.setFillColor("gray")
            can.drawRightString(7.80 * inch, 0.25 * inch, topic)

            can.showPage()

    can.save()


create_pdf()
