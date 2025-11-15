# Why Functional Programming Matters
## لماذا تُهِم البرمجة الوظيفية

**Paper ID:** hughes-1989
**Author:** John Hughes
**Year:** 1989 (original publication), based on 1984 Chalmers memo
**Publication:** The Computer Journal, Vol. 32, No. 2, 1989, pp. 98-107
**Also in:** Research Topics in Functional Programming, ed. D. Turner, Addison-Wesley, 1990, pp. 17-42
**DOI:** 10.1093/comjnl/32.2.98
**PDF:** https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf
**Author Page:** https://www.cse.chalmers.se/~rjmh/Papers/whyfp.html

**Abstract Translation Quality:** 0.89 (from translations/hughes-1989.md)
**Full Paper Translation Quality:** TBD

## Paper Significance

This is one of the most influential papers in functional programming literature. John Hughes argues that functional programming matters not because of what it removes (assignment statements, side effects) but because of what it adds: powerful tools for modularity through higher-order functions and lazy evaluation. The paper has been translated into multiple languages and is widely cited in functional programming education.

## Citation

```bibtex
@article{Hughes1989,
  author = {Hughes, John},
  title = {Why Functional Programming Matters},
  journal = {The Computer Journal},
  volume = {32},
  number = {2},
  pages = {98--107},
  year = {1989},
  publisher = {Oxford University Press},
  doi = {10.1093/comjnl/32.2.98}
}
```

## Paper Structure

The paper is structured around demonstrating two key features of functional languages:

1. **Higher-Order Functions** - Functions that take other functions as arguments
2. **Lazy Evaluation** - Delayed computation that enables infinite data structures

The paper uses Miranda code examples to demonstrate:
- List manipulation (sum, product, map, filter using foldr)
- Tree operations
- Newton-Raphson square root algorithm
- Numerical differentiation with Richardson extrapolation
- Alpha-beta pruning for game trees

## Translation Team

- Translator: Claude (Session 2025-11-15)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: TBD

## Translation Notes

This paper includes extensive Miranda code examples that will be preserved in English with Arabic commentary. Key terms:
- functional programming → البرمجة الوظيفية
- higher-order functions → الدوال من الرتبة العليا
- lazy evaluation → التقييم الكسول
- modularity → النمطية
- foldr → الطي من اليمين
- composition → التركيب
