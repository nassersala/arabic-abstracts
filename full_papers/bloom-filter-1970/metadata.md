# Space/Time Trade-offs in Hash Coding with Allowable Errors
## مقايضات المساحة/الوقت في ترميز التجزئة مع الأخطاء المسموحة

**Author:** Burton H. Bloom
**Year:** 1970
**Publication:** Communications of the ACM, Vol. 13, No. 7, July 1970, pp. 422-426
**DOI:** 10.1145/362686.362692
**PDF:** https://crystal.uta.edu/~mcguigan/cse6350/papers/Bloom.pdf

**Abstract Translation Quality:** 0.93 (from translations/)
**Full Paper Translation Quality:** 0.88 (7 sections completed)

## Citation

```bibtex
@article{Bloom1970,
  author = {Bloom, Burton H.},
  title = {Space/Time Trade-offs in Hash Coding with Allowable Errors},
  journal = {Communications of the ACM},
  volume = {13},
  number = {7},
  year = {1970},
  pages = {422--426},
  doi = {10.1145/362686.362692}
}
```

## Historical Significance

This seminal 1970 paper introduced what is now known as the **Bloom filter**, a space-efficient probabilistic data structure for testing set membership. The data structure allows for false positives but never false negatives, making it ideal for applications where memory efficiency is critical and occasional false positives are acceptable.

**Impact:**
- Cited over 10,000 times
- Widely used in databases, web caching, network routers, and blockchain systems
- Foundational paper in probabilistic data structures
- Still highly relevant over 50 years after publication

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-15
- Started: 2025-11-15
- Completed: 2025-11-15 ✅

## Paper Structure

This 5-page paper consists of:
1. Abstract
2. Introduction (problem definition and motivation)
3. Description of three hash coding methods:
   - Conventional hash coding
   - Method 1 (multiple hash functions)
   - Method 2 (Bloom filter - the main contribution)
4. Mathematical analysis and comparison
5. Conclusion

The paper analyzes the trade-offs between space (hash area size), time (reject time), and error rate (false positive probability) in hash-based set membership testing.
