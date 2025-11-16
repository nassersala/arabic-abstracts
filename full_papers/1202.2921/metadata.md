# Evaluation strategies for monadic computations
## استراتيجيات التقييم للحسابات الموناد

**arXiv ID:** 1202.2921
**Authors:** Tomas Petricek
**Year:** 2012
**Publication:** arXiv preprint
**Categories:** cs.PL (Programming Languages)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1202.2921.pdf

**Abstract Translation Quality:** 0.87 (from translations/)
**Full Paper Translation Quality:** 0.867

## Citation

```bibtex
@article{petricek2012evaluation,
  title={Evaluation strategies for monadic computations},
  author={Petricek, Tomas},
  journal={arXiv preprint arXiv:1202.2921},
  year={2012}
}
```

## Translation Team
- Translator: Claude (Session 2025-11-15)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Translation Summary

This paper presents an alternative approach to translating functional code to monadic form that abstracts the evaluation strategy using an operation called *malias*. The translation covers:

1. **Abstract** (0.88) - Introduction to the malias operation and its applications
2. **Introduction** (0.87) - Motivation and examples comparing call-by-value and call-by-name
3. **Abstracting Evaluation Strategy** (0.86) - Formal translation using malias and operation laws
4. **Computational Semi-Bimonads** (0.85) - Category theory foundations
5. **Practical Applications** (0.87) - Implementation using monad transformers, call-by-need semantics
6. **Related Work** (0.86) - Comparison with other approaches
7. **Conclusion** (0.88) - Summary of contributions

The paper makes important theoretical and practical contributions to functional programming, particularly in addressing Wadler's open question about call-by-need semantics in monadic translations.
