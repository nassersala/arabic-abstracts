#!/usr/bin/env python3
import PyPDF2
import sys

def extract_text_from_pdf(pdf_path, output_path):
    """Extract text from PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        text = []
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            text.append(f"--- Page {i+1}/{num_pages} ---\n")
            text.append(page_text)
            text.append("\n\n")

        full_text = ''.join(text)

        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(full_text)

        print(f"Extracted {num_pages} pages to {output_path}")
        print(f"Total characters: {len(full_text)}")

if __name__ == '__main__':
    extract_text_from_pdf('paper.pdf', 'paper.txt')
