# QuickerCheck: Implementing and Evaluating a Parallel Run-Time for QuickCheck
## QuickerCheck: تطبيق وتقييم وقت تشغيل متوازي لـ QuickCheck

**arXiv ID:** 2404.16062
**Authors:** Robert Krook, Nicholas Smallbone, Bo Joel Svensson, Koen Claessen
**Year:** 2024
**Publication:** IFL 2023 (Implementation and Application of Functional Languages)
**Categories:** cs.PL (Programming Languages)
**DOI:** https://doi.org/10.48550/arXiv.2404.16062
**PDF:** https://arxiv.org/pdf/2404.16062.pdf
**Pages:** 12

**Abstract Translation Quality:** 0.90 (from translations/)
**Full Paper Translation Quality:** 0.872 ✅

## Citation

```bibtex
@article{krook2024quickercheck,
  title={QuickerCheck: Implementing and Evaluating a Parallel Run-Time for QuickCheck},
  author={Krook, Robert and Smallbone, Nicholas and Svensson, Bo Joel and Claessen, Koen},
  journal={arXiv preprint arXiv:2404.16062},
  year={2024},
  note={IFL 2023}
}
```

## Translation Team
- Translator: Claude Sonnet 4.5 (Session 2025-11-17)
- Reviewer: TBD
- Started: 2025-11-17
- Completed: 2025-11-17

## Paper Summary

This paper presents QuickerCheck, a parallel runtime system for QuickCheck, a widely-used property-based testing framework for Haskell. The authors address two key challenges: (1) parallelizing the testing loop while maintaining QuickCheck's size-based test generation strategy, and (2) parallelizing the shrinking process that finds minimal counterexamples. The work achieves 3-9× speedups on heavyweight benchmarks and evaluates two shrinking approaches: deterministic (matching sequential behavior) and greedy (faster but non-deterministic).
