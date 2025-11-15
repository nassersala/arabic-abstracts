# A fast quantum mechanical algorithm for database search
## خوارزمية ميكانيكا الكم السريعة للبحث في قواعد البيانات

**arXiv ID:** quant-ph/9605043
**Authors:** Lov K. Grover (Bell Labs)
**Year:** 1996
**Publication:** STOC 1996 (Proceedings, 28th ACM Symposium on Theory of Computing, Philadelphia PA USA, pages 212-219)
**Categories:** Quantum Physics (quant-ph)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/quant-ph/9605043.pdf

**Abstract Translation Quality:** 0.93 (from translations/)
**Full Paper Translation Quality:** 0.877

## Citation

```bibtex
@inproceedings{grover1996fast,
  title={A fast quantum mechanical algorithm for database search},
  author={Grover, Lov K.},
  booktitle={Proceedings of the twenty-eighth annual ACM symposium on Theory of computing},
  pages={212--219},
  year={1996}
}
```

## Paper Description

This is Grover's seminal 1996 paper introducing the quantum search algorithm (Grover's algorithm), one of the most fundamental algorithms in quantum computing. The algorithm provides a quadratic speedup over classical algorithms for unstructured search, reducing the time complexity from O(N) to O(√N).

**Key Contributions:**
- Presents a quantum algorithm for searching an unsorted database in O(√N) steps
- Shows the algorithm is within a constant factor of the optimal quantum search
- Demonstrates the power of quantum superposition and amplitude amplification
- Has applications to NP-complete problems and cryptography

**Importance:**
- Foundational quantum computing algorithm alongside Shor's algorithm
- Demonstrates quantum advantage for a practical problem
- Inspired numerous extensions and applications in quantum algorithms
- Cited over 10,000 times

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-15
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Translation Summary

**Total Sections:** 9 (Abstract, Introduction, Problem Formulation, Algorithm, Proofs, Analysis, Implementation, Discussion, References)
**Average Quality Score:** 0.877
**All sections completed with quality ≥ 0.85** ✓

### Section Breakdown:
- 00-abstract.md (0.93) - Phone directory analogy and O(√N) complexity
- 01-introduction.md (0.87) - Quantum computing background, SAT/NP-completeness, Walsh-Hadamard
- 02-problem-formulation.md (0.89) - Mathematical problem statement
- 03-algorithm.md (0.86) - Algorithm steps, diffusion transform, amplitude amplification
- 04-proofs.md (0.85) - Theorems 1-3, corollaries, unitary transformations
- 05-analysis.md (0.87) - Lower bound Ω(√N) from [BBBV96]
- 06-implementation.md (0.88) - Practical considerations, quantum vs classical memory
- 07-discussion.md (0.86) - Extensions, multiple solutions, applications
- 08-references.md (0.90) - Complete bibliography with 17 references
