# Type-level Property Based Testing
## الاختبار القائم على الخصائص على مستوى الأنواع

**arXiv ID:** 2407.12726
**Authors:** Thomas Ekström Hansen, Edwin Brady
**Year:** 2024
**Publication:** 9th ACM SIGPLAN International Workshop on Type-Driven Development (TyDe '24), September 6, 2024, Milan, Italy
**Categories:** cs.PL (Programming Languages), cs.SE (Software Engineering)
**DOI:** https://doi.org/10.1145/3678000.3678206
**PDF:** https://arxiv.org/pdf/2407.12726.pdf

**Abstract Translation Quality:** 0.88 (from translations/)
**Full Paper Translation Quality:** 0.866 ✅

## Abstract

We present an automated framework for solidifying the cohesion between software specifications, their dependently typed models, and implementation at compile time. Model Checking and type checking are currently separate techniques for automatically verifying the correctness of programs. Using Property Based Testing (PBT), Indexed State Monads (ISMs), and dependent types, we are able to model several interesting systems and network protocols, have the type checker verify that our implementation behaves as specified, and test that our model matches the specification's semantics; a step towards combining model and type checking.

## Citation

```bibtex
@inproceedings{hansen2024typelevel,
  title={Type-level Property Based Testing},
  author={Hansen, Thomas Ekström and Brady, Edwin},
  booktitle={Proceedings of the 9th ACM SIGPLAN International Workshop on Type-Driven Development (TyDe '24)},
  year={2024},
  month={September},
  pages={13},
  location={Milan, Italy},
  publisher={ACM},
  address={New York, NY, USA},
  doi={10.1145/3678000.3678206}
}
```

## Translation Team
- Translator: Claude Code (Session 2025-11-17)
- Reviewer: TBD
- Started: 2025-11-17
- Completed: 2025-11-17

## Paper Structure
- 13 pages total
- 6 main sections:
  1. Introduction/Motivation
  2. QuickCheck in Idris2
  3. Example: ATM
  4. Generalising
  5. Evaluation & Further Work
  6. Conclusion

## Key Topics
- Property Based Testing (PBT)
- Dependent Types
- Type Checking
- Model Checking
- Indexed State Monads (ISMs)
- State Machines
- QuickCheck implementation
- Idris2 programming language
