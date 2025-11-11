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

# Terms used in translations (normalize to match glossary entries)
used_terms = {
    # Paper 1
    'formal verification': 1,
    'higher-order': 1,
    'type theory': 1,
    'proof assistant': 1,
    'concurrency': 1,
    'semantic': 1,
    'state': 1,
    'programming language': 2,  # used in papers 1 and 2
    'recursion': 2,  # used in papers 1 and 2
    'parallelism': 1,
    # Paper 2
    'monad': 1,
    'polymorphism': 2,  # used in papers 2 and 4
    'framework': 3,  # used in papers 2, 4, and 5
    'denotational': 4,  # used in papers 1, 2, 3, 4
    # Paper 3
    'distributed system': 1,
    'operational': 1,
    'functional programming': 1,
    'protocol': 1,
    # Paper 4
    'testing': 1,
    'quantum computing': 1,
    'architecture': 1,
    'hardware': 1,
    'matrix': 1,
    # Paper 5
    'implementation': 1,
    'regular expression': 1,
    'syntax': 1,
    'derivative': 1,
    'deterministic': 1,
    'equivalent': 1,
}

# Update usage counts
for term, count in used_terms.items():
    term_lower = term.lower()
    if term_lower in entries:
        entries[term_lower]['usage_count'] += count

# New terms to add
new_terms = [
    ('asynchronous', 'لامتزامن', '0.9', 1, 'Not synchronized in time'),
    ('automaton', 'آلية', '0.9', 1, 'Finite automaton'),
    ('call/cc', 'استدعاء الاستمرار', '0.8', 1, 'Call with current continuation'),
    ('Choi matrix', 'مصفوفة تشوي', '0.8', 1, 'Quantum process representation'),
    ('closed-term canonicity', 'الكنسية للحدود المغلقة', '0.7', 1, 'Canonical form for closed terms'),
    ('compositional semantics', 'الدلالات التركيبية', '0.9', 1, 'Compositional approach to semantics'),
    ('computation judgement', 'حكم حسابي', '0.8', 1, 'Judgement about computation'),
    ('consensus protocol', 'بروتوكول إجماع', '0.9', 1, 'Agreement protocol'),
    ('core calculus', 'حساب أساسي', '0.9', 1, 'Minimal formal system'),
    ('defunctionalization', 'إزالة الوظيفية', '0.8', 1, 'Transformation to eliminate higher-order functions'),
    ('density matrix', 'مصفوفة الكثافة', '0.9', 1, 'Quantum state representation'),
    ('effect', 'تأثير', '0.9', 1, 'Computational effect'),
    ('equivalence class', 'صنف تكافؤ', '0.9', 1, 'Set of equivalent elements'),
    ('fault-tolerant', 'متحمل للأخطاء', '0.9', 1, 'Resilient to failures'),
    ('handler', 'معالج', '0.9', 1, 'Effect handler'),
    ('higher-kinded', 'عالي النوع', '0.8', 1, 'Type constructor taking type constructors'),
    ('Hoare-style', 'بأسلوب هوير', '0.9', 1, 'Hoare logic style'),
    ('impredicative polymorphism', 'تعدد أشكال غير محصور', '0.7', 1, 'Polymorphism allowing quantification over all types'),
    ('inductive type', 'نوع استقرائي', '0.9', 1, 'Inductively defined type'),
    ('interaction tree', 'شجرة التفاعل', '0.8', 1, 'Denotational semantics using interaction trees'),
    ('judgementally', 'حكمياً', '0.8', 1, 'At the judgement level'),
    ('monadic computation', 'حوسبة موناديّة', '0.8', 1, 'Computation in monadic form'),
    ('non-guarded', 'غير محروس', '0.8', 1, 'Without guardedness restriction'),
    ('normalized', 'مُنَمَّط', '0.9', 1, 'In normalized/canonical form'),
    ('polymorphic assertion', 'تأكيد متعدد الأشكال', '0.8', 1, 'Type-polymorphic assertion'),
    ('quantum process tomography', 'التصوير المقطعي للعمليات الكمومية', '0.8', 1, 'Reconstruction of quantum process'),
    ('quantum state tomography', 'التصوير المقطعي للحالة الكمومية', '0.8', 1, 'Reconstruction of quantum state'),
    ('quantum subroutine', 'برنامج فرعي كمومي', '0.9', 1, 'Quantum program component'),
    ('realizability semantics', 'دلالات القابلية للتحقق', '0.8', 1, 'Semantics based on realizability'),
    ('regular language', 'لغة نظامية', '1.0', 1, 'Formal language recognized by finite automaton'),
    ('state transition system', 'نظام انتقال الحالة', '0.9', 1, 'System with states and transitions'),
    ('synthetic Tait computability', 'القابلية للحوسبة التركيبية لتايت', '0.7', 1, 'Tait method in synthetic setting'),
    ('syntactic derivative', 'مشتقة نحوية', '0.8', 1, 'Derivative of regular expression'),
    ('trace-based', 'قائم على الآثار', '0.8', 1, 'Based on execution traces'),
    ('unit testing', 'اختبار الوحدة', '1.0', 1, 'Testing individual components'),
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
print(f"New terms added: {len(new_terms)}")
print(f"Terms with updated usage counts: {len(used_terms)}")
