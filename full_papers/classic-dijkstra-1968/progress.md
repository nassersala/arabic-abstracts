# Translation Progress: Go To Statement Considered Harmful

**arXiv ID:** N/A (Pre-arXiv era, 1968)
**Publication ID:** classic-dijkstra-1968
**Started:** 2025-11-14
**Status:** In Progress

## Paper Structure Notes

This is a 2-page letter to the editor (not a formal research paper), so it has a simpler structure than typical papers:
- **Format:** Single essay/argument
- **Length:** ~11 paragraphs
- **No formal sections:** No introduction, methodology, conclusion sections
- **Structure:** Continuous argumentative essay with acknowledgements at end

## Sections

- [x] 00-abstract.md (copy from translations/classic-dijkstra-1968.md) ✓
- [~] 01-main-text.md (paragraphs 1-11: full argumentative essay) - 10% complete (1/11 paragraphs)
- [ ] 02-acknowledgements.md (acknowledgement paragraph) - Incorporated into 01-main-text.md
- [ ] 03-references.md (2 references) - Incorporated into 01-main-text.md

**Note:** Since this is a short 2-page letter, acknowledgements and references are included in 01-main-text.md rather than separate files.

## Quality Scores by Section

| Section | Score | Notes |
|---------|-------|-------|
| Abstract | 0.91 | ✓ Completed in translations/ |
| Main Text - Para 1 | 0.93 | ✓ Opening thesis translated |
| Main Text - Para 2-11 | TBD | Awaiting full source text |
| Acknowledgements | TBD | Awaiting full source text |
| References | TBD | 2 citations to translate |

**Overall Translation Quality:** TBD
**Estimated Completion:** 10% (abstract complete, paragraph 1 complete, structure established)

## Translation Notes

### Key Themes to Translate:
1. **Core thesis:** Quality of programmers inversely correlates with goto density
2. **Static vs Dynamic:** Gap between program text (static) and process execution (dynamic)
3. **Coordinate systems:** How to track program progress/state
4. **Control structures:** Conditionals, procedures, loops as alternatives to goto
5. **Program correctness:** Verification and understanding

### Special Terminology:
- "go to statement" vs "goto statement" (inconsistent in original)
- "textual index" (coordinate in program text)
- "dynamic index" (runtime counter, e.g., loop iteration)
- "intellectually manageable" (key concept)
- "unbridled use" (uncontrolled usage)

### Translation Challenges:
- This is argumentative prose, not technical exposition
- Dijkstra's writing style is distinctive and formal
- Must preserve the rhetorical force of the argument
- Balance between formal Arabic and readable style

## Session Log

### 2025-11-14 - Initial Setup and First Translation
- ✅ Verified abstract exists (0.91 quality score)
- ✅ Created directory structure: `full_papers/classic-dijkstra-1968/`
- ✅ Created metadata.md with paper details, citation, historical context
- ✅ Created progress.md tracking file
- ✅ Loaded glossary.md and identified key terms:
  - statement (جملة), algorithm (خوارزمية), control flow (تدفق التحكم)
  - correctness (صحة), verification (التحقق), structured programming (برمجة مهيكلة)
  - procedure (إجراء), process (عملية), loop (حلقة)
- ✅ Created 00-abstract.md from translations/
- ✅ Created 01-main-text.md template with structure
- ✅ Translated paragraph 1 (opening thesis) - Quality: 0.93
- ⚠️  **Blocked:** Need full source text from EWD215 to continue
- ⏳ **Next:** Obtain full paper text, translate remaining 10 paragraphs

### Source Text Status
- **Available:** Opening paragraph, structure outline, paragraph opening sentences
- **Needed:** Full text of paragraphs 2-11, acknowledgements, references
- **Source:** https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD215.html
- **Alternative:** CACM original or PDF extraction

### Translation Approach Established
- ✅ Using glossary terms consistently
- ✅ Preserving formal academic Arabic style
- ✅ Keeping programming keywords (goto, if, while) in English
- ✅ Quality scoring per paragraph: semantic (0.93), technical (0.95), readability (0.90)
- ✅ Target: >0.85 for all sections
