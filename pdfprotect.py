from PyPDF2 import PdfWriter, PdfReader

pdfwriter=PdfWriter()
pdf = PdfReader("test.pdf")

for page_num in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page_num])
pw = "123"
pdfwriter.encrypt(pw)
with open("test_pw.pdf", "wb") as f:
    pdfwriter.write(f)
