#!/usr/bin/env python3
"""Extract text from Spanner PDF using multiple methods."""

import sys

# Try different PDF libraries
try:
    import PyPDF2
    method = "PyPDF2"
except ImportError:
    try:
        import pypdf
        method = "pypdf"
    except ImportError:
        print("No PDF library available. Install with: pip install pypdf", file=sys.stderr)
        sys.exit(1)

def extract_with_pypdf2(pdf_path):
    """Extract text using PyPDF2."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        for page_num, page in enumerate(reader.pages, 1):
            text.append(f"\n--- Page {page_num} ---\n")
            text.append(page.extract_text())
        return '\n'.join(text)

def extract_with_pypdf(pdf_path):
    """Extract text using pypdf."""
    import pypdf
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = []
        for page_num, page in enumerate(reader.pages, 1):
            text.append(f"\n--- Page {page_num} ---\n")
            text.append(page.extract_text())
        return '\n'.join(text)

if __name__ == "__main__":
    pdf_path = "/home/user/arabic-abstracts/full_papers/spanner-2012/spanner-osdi2012.pdf"

    try:
        if method == "PyPDF2":
            text = extract_with_pypdf2(pdf_path)
        else:
            text = extract_with_pypdf(pdf_path)

        # Write to file
        output_path = "/home/user/arabic-abstracts/full_papers/spanner-2012/paper_text.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"Text extracted successfully to {output_path}")
        print(f"Total characters: {len(text)}")

    except Exception as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        sys.exit(1)
