Search arXiv for "SEARCH_QUERY_HERE" and get the top 5 papers.

FIRST: Check if translations/glossary.md exists. If not, create it with these default CS terms:

---
# Computer Science Glossary (English ↔ Arabic)

| English | Arabic | Confidence | Usage Count | Notes |
|---------|--------|------------|-------------|-------|
| algorithm | خوارزمية | 1.0 | 0 | Standard term |
| data structure | بنية البيانات | 1.0 | 0 | Standard term |
| machine learning | تعلم الآلة | 1.0 | 0 | Standard term |
| neural network | شبكة عصبية | 1.0 | 0 | Standard term |
| deep learning | تعلم عميق | 1.0 | 0 | Standard term |
| transformer | محول | 0.8 | 0 | Deep learning architecture |
| attention mechanism | آلية الانتباه | 0.9 | 0 | Used in transformers |
---

Then for each paper:

1. Fetch the paper metadata (title, authors, abstract, year, arXiv ID)

2. Read translations/glossary.md and use those terms for consistency

3. Translate the abstract to Modern Standard Arabic:
   - Apply glossary terms where they appear
   - Use proper technical terminology
   - Preserve mathematical notation
   - Track which glossary terms you used

4. Translate the title to Arabic

5. Back-translate the Arabic abstract to English for validation

6. Score the translation quality (0.0-1.0) based on:
   - Semantic equivalence with original
   - Technical accuracy
   - Completeness
   - Coherence
   - Consistency with glossary

7. If score < 0.85, improve and retry (max 3 iterations)

8. Update translations/glossary.md:
   - Increment usage count for terms you used
   - Add new technical terms you encountered (start confidence at 0.7-0.8)

9. Save the best translation to: translations/ARXIV_ID.md

Use this markdown format:

---
# [English Title]
## [Arabic Title]

**arXiv ID:** ARXIV_ID  
**Authors:** Author list  
**Year:** YEAR  
**Categories:** Categories  
**Translation Quality:** SCORE  
**Glossary Terms Used:** term1, term2, term3

### English Abstract
[original abstract]

### الملخص العربي
[arabic translation]

### Back-Translation (Validation)
[back translation]

### Translation Metrics
- Iterations: N
- Final Score: X.XX
- Quality: High/Medium/Low
---

Show me:
- Summary table of all papers with quality scores
- Updated glossary statistics (new terms added, most used terms)