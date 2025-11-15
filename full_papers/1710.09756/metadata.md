# Linear Haskell: Practical Linearity in a Higher-Order Polymorphic Language
## Haskell الخطي: الخطية العملية في لغة متعددة الأشكال من الرتبة العليا

**arXiv ID:** 1710.09756
**Authors:** Jean-Philippe Bernardy, Mathieu Boespflug, Ryan R. Newton, Simon Peyton Jones, Arnaud Spiwack
**Year:** 2017
**Publication:** Proceedings of the ACM on Programming Languages, Vol. 2, No. POPL, Article 5 (January 2018)
**Categories:** cs.PL (Programming Languages)
**DOI:** 10.1145/3158093
**PDF:** https://arxiv.org/pdf/1710.09756.pdf

**Abstract Translation Quality:** 0.89 (from translations/)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@article{bernardy2018linear,
  title={Linear Haskell: practical linearity in a higher-order polymorphic language},
  author={Bernardy, Jean-Philippe and Boespflug, Mathieu and Newton, Ryan R and Peyton Jones, Simon and Spiwack, Arnaud},
  journal={Proceedings of the ACM on Programming Languages},
  volume={2},
  number={POPL},
  pages={1--29},
  year={2018},
  publisher={ACM New York, NY, USA}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Started: 2025-11-15
- Completed: TBD

## Paper Overview

This paper presents Linear Haskell, a linear type system designed for integration with existing functional programming languages. The key innovation is attaching linearity to function arrows rather than creating separate linear and non-linear type variants. This design allows:

1. **Backwards compatibility**: Existing Haskell programs continue to work
2. **Code reuse**: Functions can work uniformly in both linear and non-linear contexts
3. **Practical applications**: Safe in-place updates and protocol enforcement

The paper includes a formal core calculus (λq→), implementation in GHC, and case studies demonstrating the approach.
