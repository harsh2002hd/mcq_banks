import docx

doc_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\Aviation Operations Practice Questions.docx'
output_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\scratch\ops_raw_text.txt'

doc = docx.Document(doc_path)
with open(output_path, 'w', encoding='utf-8') as f:
    for para in doc.paragraphs:
        if para.text.strip():
            f.write(para.text + '\n')

print(f"Extracted text to {output_path}")
