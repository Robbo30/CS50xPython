from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(False)
pdf.add_page()
pdf.set_font("helvetica", "B", 25)
pdf.cell(w=0, h=30, txt="CS50 shirtificate")
pdf.image("D:\VS Studio\Python on VS Studio\Learning Python\CS50P\Week 8 (OOP)\CS50Shirtificate\shirtificate.png", 20, 50, 175, 200)
pdf.set_font("helvetica", "B", 1)
pdf.set_text_color(255)
pdf.cell(w=0, h=110, txt=name+" took CS50", align="C")

pdf.output("D:\VS Studio\Python on VS Studio\Learning Python\CS50P\Week 8 (OOP)\CS50Shirtificate\shirtificate.png")

