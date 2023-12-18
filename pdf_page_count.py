import PyPDF2

with open('blank_wm.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
