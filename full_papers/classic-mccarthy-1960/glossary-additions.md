# Glossary Additions for classic-mccarthy-1960

This document lists new technical terms introduced in the McCarthy LISP paper translation that should be added to the main glossary.

## New Terms to Add

| English | Arabic | Confidence | Usage Count | Notes |
|---------|--------|------------|-------------|-------|
| S-expression | تعبير-S | 0.95 | 15 | Symbolic expression - fundamental LISP data structure |
| S-function | دالة-S | 0.95 | 8 | Function operating on S-expressions |
| apply | apply | 1.0 | 12 | Universal function - kept in English as function name |
| eval | eval | 1.0 | 10 | Evaluation function - kept in English as function name |
| cons cell | خلية cons | 0.95 | 6 | Memory cell with CAR and CDR fields |
| atomic symbol | رمز ذري | 0.95 | 7 | Indivisible symbol in LISP |
| dotted pair | زوج منقط | 0.95 | 8 | Pair notation (A · B) |
| meta-circular evaluator | مُقيِّم دائري وصفي | 0.90 | 4 | Interpreter defined in terms of itself |
| homoiconicity | التماثل الأيقوني | 0.85 | 3 | Code and data have same representation |
| association list | قائمة اقتران | 0.95 | 5 | List of variable-value pairs (environment) |
| environment | بيئة | 0.95 | 6 | Variable bindings for evaluation |
| fixed point | نقطة ثابتة | 0.95 | 2 | Self-referential definition point |
| short-circuit evaluation | التقييم القصير الدائرة | 0.90 | 2 | Stop evaluation when condition is met |
| property list | قائمة خصائص | 0.95 | 3 | Symbol attributes in LISP |
| free storage | التخزين الحر | 0.90 | 2 | Available memory pool |
| mark-and-sweep | المَرْك والمسح | 0.90 | 2 | Garbage collection algorithm |
| Church-Turing thesis | أطروحة تشرش-تورينغ | 0.95 | 1 | Equivalence of computation models |
| predicate | عبارة شرطية | 0.95 | 5 | Boolean-valued function |
| consequent | نتيجة | 0.90 | 4 | Result expression in conditional |
| CAR | CAR | 1.0 | 10 | Contents of Address Register (LISP primitive) |
| CDR | CDR | 1.0 | 10 | Contents of Decrement Register (LISP primitive) |
| CONS | cons | 1.0 | 8 | Construct pair (LISP primitive) |
| NIL | NIL | 1.0 | 6 | Empty list / false value |
| lambda expression | تعبير لامبدا | 0.95 | 6 | Anonymous function definition |
| universal function | دالة عامة | 0.95 | 4 | Function that can compute any computable function |
| symbolic computation | حساب رمزي | 0.95 | 5 | Non-numeric computation on symbols |
| list notation | تدوين القائمة | 0.95 | 3 | Abbreviated form of dotted pairs |
| base case | حالة أساسية | 0.95 | 3 | Termination condition in recursion |
| well-foundedness | التأسيس الجيد | 0.85 | 1 | Property ensuring recursion terminates |
| composability | قابلية التركيب | 0.90 | 2 | Ability to combine functions |

## Terms Already in Glossary (Confirmed Usage)

These terms were already in the glossary and were used consistently:
- function (دالة)
- recursive (عودي)
- symbolic (رمزي)
- interpreter (مفسر)
- lambda calculus (حساب لامبدا)
- computation (حساب)
- formalism (شكلية)
- functional programming (البرمجة الوظيفية)
- algorithm (خوارزمية)
- machine learning (تعلم الآلة)
- declarative (تصريحي)

## Notes on Translation Choices

### S-expression vs Symbolic Expression
- Used "تعبير-S" as the primary term (following the paper's abbreviation)
- "تعبير رمزي" used interchangeably when emphasizing the "symbolic" nature
- Both forms are correct and context-dependent

### Function Names (apply, eval, cons, car, cdr)
- Kept in English as they are standard LISP function names
- No translation needed - these are programming language keywords
- Used consistently across all code examples

### Meta-Circular Evaluator
- "مُقيِّم دائري وصفي" chosen to capture both "meta" (وصفي) and "circular" (دائري)
- Alternative considered: "مقيّم ذاتي المرجع" (self-referential evaluator)
- Current choice better captures the technical meaning

### Homoiconicity
- "التماثل الأيقوني" chosen to convey "same representation"
- Literally: "iconic similarity/identity"
- Alternative considered: "توحيد الشيفرة والبيانات" (code-data unification)
- Current choice is more concise and technical

## Usage Statistics by Section

| Section | New Terms Introduced | Existing Terms Used |
|---------|---------------------|---------------------|
| Introduction | 3 | 8 |
| Recursive Functions | 5 | 10 |
| S-expressions | 6 | 7 |
| S-functions | 4 | 9 |
| Representation | 7 | 8 |
| Apply Function | 8 | 12 |
| Conditional Expressions | 3 | 6 |
| Conclusion | 2 | 7 |

**Total new terms:** 30
**Total glossary terms reused:** 67

## Recommendations for Glossary Maintenance

1. **Add all new terms** listed above to the main glossary
2. **Increment usage counts** for existing terms used in this translation
3. **Cross-reference** related terms (e.g., apply ↔ eval, S-expression ↔ S-function)
4. **Add paper reference** to glossary entries: "Used in classic-mccarthy-1960"
5. **Consider adding** LISP-specific subsection to glossary for programming language terms
