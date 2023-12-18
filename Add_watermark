import PyPDF2

template = PyPDF2.PdfReader(open('combine.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('blank_wm.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('AWM_combine.pdf', 'wb') as file:
        output.write(file)
