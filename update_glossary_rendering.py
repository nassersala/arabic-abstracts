#!/usr/bin/env python3
import re
from collections import defaultdict

# Read the current glossary
with open('/home/user/arabic-abstracts/translations/glossary.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse existing entries
entries = {}
lines = content.split('\n')
header_lines = []
in_header = True

for line in lines:
    if in_header:
        header_lines.append(line)
        if line.startswith('|---'):
            in_header = False
        continue

    if line.strip() and line.startswith('|'):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 6 and parts[1]:
            english = parts[1]
            arabic = parts[2]
            confidence = parts[3]
            usage_count = int(parts[4])
            notes = parts[5]
            entries[english.lower()] = {
                'english': english,
                'arabic': arabic,
                'confidence': confidence,
                'usage_count': usage_count,
                'notes': notes
            }

# Terms used in rendering papers - update usage counts
used_terms = {
    'algorithm': 6,  # used in all 6 papers
    'rendering': 4,  # used in Phong, Whitted, Kajiya, Jensen
    'simulation': 2,  # used in Whitted, Bouaziz
    'dynamics': 1,  # used in Bouaziz
}

# Update usage counts
for term, count in used_terms.items():
    term_lower = term.lower()
    if term_lower in entries:
        entries[term_lower]['usage_count'] += count

# New rendering-specific terms to add
new_terms = [
    ('alternating optimization', 'تحسين متناوب', '0.9', 1, 'Optimization method alternating between steps'),
    ('caustics', 'ظواهر كاوية', '0.8', 1, 'Light patterns from reflection/refraction'),
    ('coherence', 'تماسك', '0.9', 1, 'Property exploited to reduce computation'),
    ('constraint', 'قيد', '0.9', 1, 'Physical or mathematical constraint'),
    ('continuum mechanics', 'ميكانيكا الاستمرارية', '0.9', 1, 'Physics of continuous materials'),
    ('finite element', 'عناصر محدودة', '0.9', 1, 'Numerical method for PDEs'),
    ('global illumination', 'إضاءة شاملة', '0.9', 2, 'Comprehensive lighting simulation'),
    ('hierarchical sampling', 'عينات هرمية', '0.8', 1, 'Hierarchical variance reduction technique'),
    ('hidden surface', 'سطح مخفي', '0.9', 2, 'Surface occluded from view'),
    ('illumination', 'إضاءة', '0.9', 3, 'Lighting model or calculation'),
    ('monte carlo', 'مونت كارلو', '0.9', 1, 'Stochastic simulation method'),
    ('optical phenomena', 'ظواهر بصرية', '0.9', 1, 'Visual effects from light interaction'),
    ('photon', 'فوتون', '1.0', 2, 'Quantum of light energy'),
    ('photon mapping', 'خرائط الفوتون', '0.9', 2, 'Global illumination technique'),
    ('position based dynamics', 'ديناميكيات قائمة على الموضع', '0.9', 1, 'Physics simulation method'),
    ('potential energy', 'طاقة كامنة', '0.9', 1, 'Stored energy in a system'),
    ('ray tracing', 'تتبع الأشعة', '0.9', 3, 'Rendering technique following light rays'),
    ('reflection', 'انعكاس', '0.9', 2, 'Light bouncing off surfaces'),
    ('refraction', 'انكسار', '0.9', 1, 'Light bending through media'),
    ('shader', 'مظلل', '0.9', 2, 'Program calculating surface appearance'),
    ('shading', 'تظليل', '0.9', 4, 'Surface appearance calculation'),
    ('shadow', 'ظل', '0.9', 1, 'Darkened area from blocked light'),
    ('solver', 'حلّال', '0.9', 2, 'Algorithm solving equations'),
    ('sorting', 'ترتيب', '0.9', 2, 'Ordering data elements'),
    ('variance reduction', 'تقليل التباين', '0.8', 1, 'Monte Carlo optimization technique'),
]

# Add new terms
for english, arabic, confidence, usage, notes in new_terms:
    english_lower = english.lower()
    if english_lower not in entries:
        entries[english_lower] = {
            'english': english,
            'arabic': arabic,
            'confidence': confidence,
            'usage_count': usage,
            'notes': notes
        }

# Sort entries alphabetically by English term
sorted_entries = sorted(entries.values(), key=lambda x: x['english'].lower())

# Write updated glossary
output_lines = header_lines + ['']
for entry in sorted_entries:
    line = f"| {entry['english']} | {entry['arabic']} | {entry['confidence']} | {entry['usage_count']} | {entry['notes']} |"
    output_lines.append(line)

with open('/home/user/arabic-abstracts/translations/glossary.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f"Glossary updated successfully!")
print(f"Total terms: {len(entries)}")
print(f"New terms added: {len([t for t in new_terms if t[0].lower() not in entries])}")
print(f"Terms with updated usage counts: {len(used_terms)}")
