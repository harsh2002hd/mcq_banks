import docx

doc = docx.Document('Based on the provided document.docx')
with open('scratch/docx_content.txt', 'w', encoding='utf-8') as f:
    for para in doc.paragraphs:
        f.write(para.text + '\n')
