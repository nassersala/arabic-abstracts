#!/usr/bin/env python3
"""Update glossary with new terms and usage counts for GloVe translation"""

# Terms to update (existing terms with usage count increments)
updates = {
    "corpus": 1,
    "efficient": 1,
    "factorization": 1,
    "matrix": 3,
    "outperform": 1,
    "performance": 1,
    "regression": 1,
    "representation": 2,
    "semantic": 1,
    "sparse": 1,
    "training": 2,
    "vector": 6,
}

# New terms to add (term, arabic, confidence, notes)
new_terms = [
    ("co-occurrence", "التواجد المشترك", 0.9, "Word co-occurrence in NLP"),
    ("context window", "نافذة السياق", 0.9, "Sliding context window in NLP"),
    ("fine-grained", "دقيق التفاصيل", 0.9, "Fine-grained or detailed"),
    ("log-bilinear", "لوغاريتمي ثنائي الخطية", 0.8, "Log-bilinear regression model"),
    ("named entity recognition", "التعرف على الكيانات المسماة", 0.9, "NER task in NLP"),
    ("nonzero", "غير صفري", 0.9, "Nonzero elements"),
    ("opaque", "غامض", 0.9, "Not transparent or clear"),
    ("regularities", "انتظامات", 0.9, "Patterns or regularities"),
    ("similarity task", "مهمة التشابه", 0.9, "Similarity evaluation task"),
    ("substructure", "بنية فرعية", 0.9, "Substructure or sub-pattern"),
    ("syntactic", "نحوي", 0.9, "Related to syntax"),
    ("vector arithmetic", "حساب المتجهات", 0.9, "Vector arithmetic operations"),
    ("vector space", "فضاء المتجهات", 0.9, "Vector space in mathematics"),
    ("word analogy", "قياس الكلمات", 0.85, "Word analogy task"),
    ("word vector", "متجه الكلمة", 0.9, "Word vector representation"),
]

# Read the glossary
with open('/home/user/arabic-abstracts/translations/glossary.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find header lines (first 5 lines)
header = lines[:5]
entries = []

# Parse existing entries
for line in lines[5:]:
    if line.strip() and line.startswith('|'):
        parts = [p.strip() for p in line.split('|')[1:-1]]  # Remove empty first and last
        if len(parts) == 5:
            english, arabic, confidence, usage, notes = parts
            entries.append({
                'english': english,
                'arabic': arabic,
                'confidence': confidence,
                'usage': int(usage),
                'notes': notes
            })

# Update existing entries
for entry in entries:
    if entry['english'] in updates:
        entry['usage'] += updates[entry['english']]

# Add new entries
for term, arabic, confidence, notes in new_terms:
    entries.append({
        'english': term,
        'arabic': arabic,
        'confidence': str(confidence),
        'usage': 1,
        'notes': notes
    })

# Sort entries alphabetically by English term (case-insensitive)
entries.sort(key=lambda x: x['english'].lower())

# Write back to file
with open('/home/user/arabic-abstracts/translations/glossary.md', 'w', encoding='utf-8') as f:
    # Write header
    for line in header:
        f.write(line)

    # Write entries
    for entry in entries:
        f.write(f"| {entry['english']} | {entry['arabic']} | {entry['confidence']} | {entry['usage']} | {entry['notes']} |\n")

print(f"Updated {len(updates)} existing terms")
print(f"Added {len(new_terms)} new terms")
print(f"Total terms in glossary: {len(entries)}")
