from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")

    # Add the multiple lines
    for i in range(20, 298, 10):
        pdf.line(x1=10, y1=i, x2=200, y2=i)

    # Set the footer
    pdf.ln(268)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=8, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Add the multiple lines
        for j in range(20, 298, 10):
            pdf.line(x1=10, y1=j, x2=200, y2=j)

        # Set the footer
        pdf.ln(280)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=8, txt=row["Topic"], align="R")

pdf.output('output.pdf')