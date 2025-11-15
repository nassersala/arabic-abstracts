# Full Paper Translation Prompt

This prompt guides the translation of complete research papers from English to Arabic, building on the 341 abstracts already translated in this repository.

## Directory Structure

```
arabic-abstracts/
├── translations/          # 341 abstract translations (keep as-is)
├── full_papers/           # NEW: Complete paper translations
│   └── ARXIV_ID/
│       ├── metadata.md    # Title, authors, abstract, paper info
│       ├── 00-abstract.md # Full abstract (copy from translations/)
│       ├── 01-introduction.md
│       ├── 02-related-work.md
│       ├── 03-methodology.md
│       ├── 04-experiments.md
│       ├── 05-results.md
│       ├── 06-conclusion.md
│       └── progress.md    # Section-by-section progress tracking
```

## Priority Papers to Translate

Start with the most influential papers from our existing abstracts. These are foundational papers that CS students should read:

### Tier 1A: Foundational Systems (Translate First)
- [x] **classic-dijkstra-1968** - Dijkstra's "Go To Statement Considered Harmful" - COMPLETED ✅ (0.89 quality)
- [x] **google-file-system-2003** - The Google File System (GFS) - COMPLETED ✅ (0.90 quality)
- [x] **classic-dean-2004** - MapReduce: Simplified Data Processing on Large Clusters - COMPLETED ✅ (0.874 quality)
- [x] **dynamo-2007** - Dynamo: Amazon's Highly Available Key-value Store - COMPLETED ✅ (0.875 quality)
- [x] **chord-2001** - Chord: A Scalable Peer-to-peer Lookup Service - COMPLETED ✅ (0.89 quality)
- [x] **classic-nakamoto-2008** - Bitcoin: A Peer-to-Peer Electronic Cash System - COMPLETED ✅ (0.872 quality)
- [ ] Add UNIX, TCP/IP papers if available

### Tier 1B: Deep Learning Foundations
- [x] **1406.2661** - Generative Adversarial Networks (GANs) - COMPLETED ✅
- [x] **1706.03762** - Transformer paper (Attention Is All You Need) - COMPLETED ✅
- [x] **1512.03385** - ResNet (Deep Residual Learning for Image Recognition) - COMPLETED ✅
- [x] **1810.04805** - BERT (Pre-training of Deep Bidirectional Transformers) - COMPLETED ✅
- [x] **2005.14165** - GPT-3 (Language Models are Few-Shot Learners) - COMPLETED ✅
- [x] **alexnet-2012** - ImageNet Classification with Deep CNNs (AlexNet) - COMPLETED ✅ (0.90 quality)
- [x] **1409.1556** - Very Deep Convolutional Networks (VGGNet) - COMPLETED ✅ (0.88 quality)
- [x] **batchnorm-2015** - Batch Normalization - COMPLETED ✅ (0.876 quality)
- [x] **adam-2014** - Adam: A Method for Stochastic Optimization - COMPLETED ✅ (0.88 quality)

### Tier 2: Influential Modern Papers
- [ ] Check translations/ for highly-cited papers (2015-2020)
- [ ] Prioritize papers with citation counts > 1000
- [ ] Focus on: distributed systems, ML/DL, databases, networking

### Tier 3: Domain-Specific Important Papers
- [ ] Quantum computing foundations
- [ ] Computer graphics classics
- [ ] HCI influential papers
- [ ] Security/cryptography papers

## Translation Workflow

### Step 1: Select Paper and Setup

1. Choose next unchecked paper from priority list above
2. Verify the abstract exists in `translations/ARXIV_ID.md`
3. Create directory structure:
   ```bash
   mkdir -p full_papers/ARXIV_ID
   ```
4. Fetch the full PDF from arXiv (arXiv:ARXIV_ID)
5. Extract text and identify sections

### Step 2: Create Progress Tracker

Create `full_papers/ARXIV_ID/progress.md`:

```markdown
# Translation Progress: [Paper Title]

**arXiv ID:** ARXIV_ID
**Started:** YYYY-MM-DD
**Status:** In Progress / Completed

## Sections

- [ ] 00-abstract.md
- [ ] 01-introduction.md
- [ ] 02-background.md (or related-work)
- [ ] 03-methodology.md (or approach/system-design)
- [ ] 04-experiments.md (or implementation)
- [ ] 05-results.md (or evaluation)
- [ ] 06-discussion.md (if present)
- [ ] 07-conclusion.md
- [ ] 08-references.md (optional - translate paper titles only)

## Quality Scores by Section

| Section | Score | Notes |
|---------|-------|-------|
| Abstract | 0.XX | |
| Introduction | 0.XX | |
| ... | | |

**Overall Translation Quality:** TBD
**Estimated Completion:** XX%
```

### Step 3: Create Metadata File

Create `full_papers/ARXIV_ID/metadata.md`:

```markdown
# [English Title]
## [Arabic Title]

**arXiv ID:** ARXIV_ID
**Authors:** Full author list
**Year:** YYYY
**Publication:** Conference/Journal name
**Categories:** arXiv categories
**DOI:** (if available)
**PDF:** https://arxiv.org/pdf/ARXIV_ID.pdf

**Abstract Translation Quality:** X.XX (from translations/)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
[Original BibTeX]
```

## Translation Team
- Translator: [LLM Session ID or human name]
- Reviewer: TBD
- Started: YYYY-MM-DD
- Completed: YYYY-MM-DD
```

### Step 4: Translate Each Section

For each section (01-introduction.md, 02-..., etc.):

1. **Read glossary**: Load `translations/glossary.md` for consistent terminology
2. **Extract section**: Get the full English text for this section
3. **Translate to Arabic**:
   - Use glossary terms consistently
   - Preserve mathematical equations (LaTeX format)
   - Keep figure/table references in both languages
   - Maintain citation format [1], [2], etc.
   - Handle inline code snippets appropriately

4. **Format the section file**:

```markdown
# Section N: [English Section Title]
## القسم N: [Arabic Section Title]

**Section:** introduction / methodology / etc.
**Translation Quality:** X.XX
**Glossary Terms Used:** term1, term2, term3

---

### English Version

[Full English text of section]

---

### النسخة العربية

[Full Arabic translation]

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:** [list new technical terms]
- **Equations:** [count of math equations]
- **Citations:** [count of references cited in section]
- **Special handling:** [any special cases - algorithms, code, tables]

### Quality Metrics

- Semantic equivalence: X.XX
- Technical accuracy: X.XX
- Readability: X.XX
- Glossary consistency: X.XX
- **Overall section score:** X.XX
```

5. **Back-translate key paragraphs** (first paragraph, last paragraph, complex sections)
6. **Score the translation** (0.0-1.0 scale)
7. **If score < 0.85**: Revise and retry (max 3 iterations)
8. **Update glossary**: Add new terms, increment usage counts
9. **Update progress.md**: Check off the section, add quality score

### Step 5: Handle Special Content

#### Mathematical Equations
- Keep LaTeX notation: `$E = mc^2$` or `$$\int_0^\infty f(x)dx$$`
- Add Arabic explanation after complex equations
- Example:
  ```markdown
  $$\mathcal{L} = -\mathbb{E}_{x \sim p_{data}}[\log D(x)]$$

  حيث $\mathcal{L}$ هي دالة الخسارة للمميز (Discriminator)
  ```

#### Figures and Tables
- Keep figure/table numbers the same
- Translate captions:
  ```markdown
  **Figure 3:** System architecture overview
  **الشكل 3:** نظرة عامة على معمارية النظام
  ```

#### Algorithms and Code
- Keep code in English (industry standard)
- Translate comments and descriptions
- Example:
  ```markdown
  **Algorithm 1:** Gradient Descent
  **الخوارزمية 1:** الانحدار التدرجي

  [Code stays in English]

  **الوصف:** تقوم هذه الخوارزمية بتحديث المعاملات...
  ```

#### References
- In `08-references.md`, translate paper titles only
- Keep author names, years, venues in English
- Mark which references already have Arabic abstracts in our repo

### Step 6: Final Review

1. **Read entire translated paper** for flow and consistency
2. **Verify all sections** are checked off in progress.md
3. **Calculate overall quality score** (average of section scores)
4. **Update metadata.md** with completion date and final score
5. **Create summary** in progress.md

### Step 7: Update Master Progress List

After completing a paper, update this file (prompt_full_paper.md) by checking off the paper in the priority list above.

## Quality Standards

### Minimum Acceptable Scores
- Abstract: ≥ 0.90 (already done in translations/)
- Introduction: ≥ 0.85
- Technical sections: ≥ 0.85
- Conclusion: ≥ 0.85
- Overall paper: ≥ 0.85

### What Makes a High-Quality Translation?
- ✅ Preserves all technical meaning
- ✅ Uses consistent glossary terms
- ✅ Maintains formal academic Arabic style
- ✅ Handles math/code/figures appropriately
- ✅ Flows naturally in Arabic
- ✅ Back-translation matches original semantics
- ❌ No omissions or additions
- ❌ No mistranslations of technical terms
- ❌ No awkward literal translations

## Session Workflow

When starting a new translation session:

```
I want to translate the next priority paper from prompt_full_paper.md.

1. Check the priority list and select the next unchecked Tier 1A paper
2. Set up the directory structure
3. Create metadata.md and progress.md
4. Start translating sections in order
5. Update progress.md after each section
6. When complete, update the checklist in prompt_full_paper.md

Target: Complete at least 3-5 sections per session.
Show me progress summary at the end.
```

## Glossary Management

- **Always read** `translations/glossary.md` before translating
- **Update after each section** with new terms and usage counts
- **Maintain consistency** across all sections of the paper
- **Flag ambiguous terms** for review

## Progress Tracking Commands

### Check Overall Progress
```
Count how many papers in full_papers/ are:
- In progress (have progress.md but not complete)
- Completed (all sections checked in progress.md)
- Show completion percentage for in-progress papers
```

### Resume In-Progress Paper
```
I want to continue translating [ARXIV_ID].
- Show me progress.md
- Tell me which section is next
- Load glossary and continue translation
```

### Quick Stats
```
Show me:
- Total papers in translations/ (abstracts): 341
- Total papers in full_papers/ (complete): X
- In-progress papers: Y
- Next priority paper to start: [name]
```

## Notes

- **Paper selection**: Prioritize foundational papers that CS students cite most
- **Time estimate**: A full paper takes 5-10 sessions depending on length
- **Incremental progress**: It's OK to do 2-3 sections per session
- **Quality over speed**: Better to have 10 excellent translations than 50 mediocre ones
- **Community value**: These translations will help Arabic-speaking CS students worldwide

## Tips for LLM Agents

- Break long sections into subsections if > 3 pages
- Take special care with definitions and theorems
- Flag papers that are too math-heavy (may need human expert review)
- If paper has 10+ sections, create subsection files (e.g., 03a-methodology-overview.md)
- Update progress.md frequently to track your work
- If you get stuck on terminology, mark it in translation notes

---

**Last Updated:** 2025-11-15
**Papers Completed:** 28 (Session 1: GANs, Transformer, ResNet, BERT, GPT-3, Dijkstra, GFS, MapReduce, Dynamo, Chord, AlexNet, VGGNet, BatchNorm, Adam, Bitcoin, FaceNet, FCN, R-CNN, Highway Networks | Session 2: Algorithmic Game Theory, Opetopes, Differential Privacy, NMT-Attention, Seq2Seq, Gödel, QAOA, Haskell Physics, Adam)
**Papers In Progress:** 0
**Next Up:** Continue with remaining 313 untranslated papers
