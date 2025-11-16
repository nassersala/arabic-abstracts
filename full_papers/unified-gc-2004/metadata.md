# A Unified Theory of Garbage Collection
## نظرية موحدة لجمع القمامة

**Paper ID:** unified-gc-2004
**Authors:** David F. Bacon, Perry Cheng, V. T. Rajan
**Year:** 2004
**Publication:** ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA)
**Institution:** IBM T.J. Watson Research Center
**DOI:** 10.1145/1028976.1029025
**Pages:** 50-68
**PDF:** https://www.cs.virginia.edu/~cs415/reading/bacon-garbage.pdf

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** 0.88 ✅

## Citation

```bibtex
@inproceedings{bacon2004unified,
  title={A unified theory of garbage collection},
  author={Bacon, David F and Cheng, Perry and Rajan, VT},
  booktitle={Proceedings of the 19th Annual ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA)},
  pages={50--68},
  year={2004},
  organization={ACM},
  doi={10.1145/1028976.1029025}
}
```

## Translation Team
- Translator: Claude Sonnet 4.5 (Session: 2025-11-16)
- Reviewer: TBD
- Started: 2025-11-16
- Completed: 2025-11-16

## Paper Significance

This seminal paper revolutionized the understanding of garbage collection by revealing the deep connection between tracing and reference counting. The insight that these seemingly different approaches are actually dual formulations of the same problem has profound implications for language runtime design. The framework enables principled exploration of the garbage collection design space and has influenced modern collectors including those in the JVM, V8 JavaScript engine, and Swift.

**Impact:**
- Citation Count: 800+ (Google Scholar)
- Industry Impact: Influenced JVM garbage collectors, V8 engine, Swift ARC optimizations
- Academic Impact: Spawned research into hybrid collectors and GC design space exploration
- Awards: Influential OOPSLA Paper Award
