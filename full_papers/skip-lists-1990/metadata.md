# Skip Lists: A Probabilistic Alternative to Balanced Trees
## قوائم التخطي: بديل احتمالي للأشجار المتوازنة

**Author:** William Pugh
**Year:** 1990
**Publication:** Communications of the ACM, Vol. 33, No. 6, June 1990, pp. 668-676
**DOI:** 10.1145/78973.78977
**PDF:** https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** 0.88 ✅

## Citation

```bibtex
@article{pugh1990skip,
  title={Skip lists: a probabilistic alternative to balanced trees},
  author={Pugh, William},
  journal={Communications of the ACM},
  volume={33},
  number={6},
  pages={668--676},
  year={1990},
  publisher={ACM New York, NY, USA}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-15
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15 ✅

## Paper Sections
1. Introduction
2. Skip Lists
3. Algorithms for Skip Lists
4. Probabilistic Analysis
5. Implementing Skip Lists
6. Comparisons with Balanced Trees
7. Conclusion

## Historical Significance

Skip lists, introduced by William Pugh in 1990, revolutionized the field of data structures by demonstrating that probabilistic approaches could achieve the same asymptotic performance as complex deterministic balanced tree structures, but with significantly simpler implementation. This paper has had lasting impact on practical systems:

- **Redis** uses skip lists to implement sorted sets
- **LevelDB** and **RocksDB** use skip lists in their MemTable implementations
- **Apache Lucene** uses skip lists for posting list compression
- Widely taught in algorithms courses as an elegant probabilistic data structure

The paper demonstrates that randomization can simplify algorithm design while maintaining expected O(log n) performance for search, insertion, and deletion operations.
