# Transpiling Programming Computable Functions to Answer Set Programs
## تحويل الدوال القابلة للحوسبة والبرمجة إلى برامج مجموعة الإجابات

**arXiv ID:** 1808.07770
**Authors:** Ingmar Dasseville, Marc Denecker
**Affiliation:** KU Leuven, Dept. of Computer Science, B-3001 Leuven, Belgium
**Year:** 2018
**Publication:** arXiv preprint
**Categories:** cs.PL (Programming Languages)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1808.07770.pdf

**Abstract Translation Quality:** 0.90 (from translations/)
**Full Paper Translation Quality:** 0.88

## Citation

```bibtex
@article{dasseville2018transpiling,
  title={Transpiling Programming Computable Functions to Answer Set Programs},
  author={Dasseville, Ingmar and Denecker, Marc},
  journal={arXiv preprint arXiv:1808.07770},
  year={2018}
}
```

## Translation Team
- Translator: Claude Code Session (2025-11-16)
- Reviewer: TBD
- Started: 2025-11-16
- Completed: 2025-11-16

## Paper Overview

This paper presents a translation mechanism from Programming Computable Functions (PCF), a theoretical foundation for functional programming languages, to Answer Set Programming (ASP), a declarative programming paradigm for solving search problems. The translation enables the use of functional programming abstractions for specifying search problems while leveraging existing ASP solver technology.

**Key Contributions:**
1. A formal translation algorithm from PCF to ASP
2. Soundness characterization of the translation
3. Extension to support multiple interpretations (search problems)
4. Implementation and demonstration (https://dtai.cs.kuleuven.be/krr/pcf2asp)
5. Foundation for the Functional Modelling System (FMS)

**Sections:**
- Abstract
- 1. Introduction
- 2. Programming Computable Functions (PCF)
  - 2.1 Syntax
  - 2.2 Operational Semantics
- 3. Answer Set Programming (ASP)
  - 3.1 Language
  - 3.2 Grounding (and Solving)
- 4. Translation
  - 4.1 Characterisation of the translation
  - 4.2 Conventions
  - 4.3 Static Preamble
  - 4.4 Translation Algorithm
  - 4.5 Optimisations
  - 4.6 Implementation
- 5. Applications
  - 5.1 Multiple interpretations for one variable
  - 5.2 Towards a more expressive language
- 6. Conclusion
- References

**Total Pages:** ~15 pages
**Estimated Lines:** ~717 lines
