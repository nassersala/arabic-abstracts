#!/usr/bin/env python3
import PyPDF2

pdf_path = '/home/user/arabic-abstracts/full_papers/1711.09184/paper.pdf'
output_path = '/home/user/arabic-abstracts/full_papers/1711.09184/paper_text.txt'

with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    full_text = []
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        full_text.append(f"\n--- PAGE {page_num + 1} ---\n")
        full_text.append(text)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(''.join(full_text))

print(f"Extracted {num_pages} pages to {output_path}")
