# Translation Prompt for Suggested Papers

Use this prompt when you want to translate papers from the suggestions list.

---

## Basic Prompt

```
Translate the next 5 unchecked papers from suggested_papers.md following the prompt.md workflow. Start with the highest priority unchecked papers from the "Top 25 Priority Papers" section.

After translation, update suggested_papers.md to check off completed papers (change [ ] to [x]).
```

---

## Batch Translation Prompt (10 papers)

```
Translate the next 10 unchecked papers from suggested_papers.md, prioritizing:
1. Tier 1A papers first (from "Top 25 Priority Papers")
2. Then Tier 1B papers
3. Then other Tier 1 papers in order

Follow the prompt.md workflow for each paper:
- Check for existing translations
- Use glossary terms
- Translate abstract to Arabic
- Back-translate for validation
- Score quality (aim for 0.85+)
- Update glossary
- Save to translations/ARXIV_ID.md

After completing all translations, update suggested_papers.md to mark completed papers with [x].

Show me a summary table of what was translated with quality scores.
```

---

## Domain-Specific Prompt

### Operating Systems Papers
```
Translate all unchecked Operating Systems papers (#1-6) from suggested_papers.md.

These are foundational CS papers, so pay special attention to:
- Accurate translation of OS terminology (processes, scheduling, memory management)
- Technical precision for Arabic CS students
- Consistent glossary usage

Follow prompt.md workflow and update checkboxes when done.
```

### Database Systems Papers
```
Translate the unchecked Database Systems papers (#7-14) from suggested_papers.md.

Focus on:
- Database terminology accuracy (transactions, consistency, distributed systems)
- Google/Amazon/Facebook system design concepts
- Clear technical explanations

Follow prompt.md workflow and update checkboxes when done.
```

### NLP Foundations Papers
```
Translate the unchecked NLP papers (#29-36) from suggested_papers.md.

These cover pre-transformer NLP foundations:
- Word embeddings (Word2Vec, GloVe, ELMo)
- Seq2seq and attention mechanism
- Context for understanding modern LLMs

Follow prompt.md workflow and update checkboxes when done.
```

### Quantum Computing Papers
```
Translate the unchecked Quantum Computing papers (#43-49) from suggested_papers.md.

Focus on:
- Quantum terminology accuracy
- Algorithm descriptions (Shor's, Grover's)
- Error correction concepts

Follow prompt.md workflow and update checkboxes when done.
```

---

## Custom Selection Prompt

```
Translate these specific papers from suggested_papers.md:
- #[NUMBER]: [PAPER NAME]
- #[NUMBER]: [PAPER NAME]
- #[NUMBER]: [PAPER NAME]

Follow prompt.md workflow and update checkboxes when done.
```

---

## Progress Check Prompt

```
Check suggested_papers.md and tell me:
1. How many papers are completed ([x])
2. How many remain ([ ])
3. Which Tier 1A papers are still unchecked
4. Recommend the next 5 papers I should translate based on priority
```

---

## Quick Start - Translate Top 5

```
Translate these 5 highest-priority papers from suggested_papers.md:
- #2: UNIX Time-Sharing System
- #7: Google File System (GFS)
- #8: Bigtable
- #9: Dynamo (Amazon)
- #80: PageRank

Follow prompt.md workflow, update checkboxes, and show me the quality scores.
```

---

## Notes

- Always check suggested_papers.md first to see current progress
- The file tracks 90 papers (3 are already translated)
- Prioritize filling critical gaps: OS, databases, compilers, networking
- Update checkboxes immediately after translation
- Target translation quality: 0.85+ score
- All translations should follow the format in prompt.md
