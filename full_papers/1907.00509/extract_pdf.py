#!/usr/bin/env python3
import PyPDF2
import sys

pdf_path = '/home/user/arabic-abstracts/full_papers/1907.00509/1907.00509.pdf'
output_path = '/home/user/arabic-abstracts/full_papers/1907.00509/paper_text.txt'

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num, page in enumerate(reader.pages):
            text += f'\n--- Page {page_num + 1} ---\n'
            text += page.extract_text()

        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(text)

        print(f"Extracted {len(reader.pages)} pages")
        print(f"Total characters: {len(text)}")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
