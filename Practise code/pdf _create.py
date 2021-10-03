from fpdf import FPDF
#class PDF(FPDF):
#pdf= PDF()
#pdf= PDF(orientation='L')
#pdf= PDF(orientation='P', unit='mm', format='A4')
#pdf.add_page()
#pdf.add_page()
#pdf.output('test.pdf','F')

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Welcome to PythonGuides", ln=1, align="L")
pdf.output("python.pdf")