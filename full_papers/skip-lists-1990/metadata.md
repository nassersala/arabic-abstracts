# Skip Lists: A Probabilistic Alternative to Balanced Trees
## قوائم التخطي: بديل احتمالي للأشجار المتوازنة

**Paper ID:** skip-lists-1990
**Author:** William Pugh
**Affiliation:** University of Maryland, College Park
**Year:** 1990
**Publication:** Communications of the ACM, Vol. 33, No. 6, June 1990, pp. 668-676
**Categories:** Data Structures, Algorithms
**DOI:** 10.1145/78973.78977
**PDF:** https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** 0.88

## Citation

```bibtex
@article{Pugh1990SkipLists,
  author = {Pugh, William},
  title = {Skip Lists: A Probabilistic Alternative to Balanced Trees},
  journal = {Communications of the ACM},
  volume = {33},
  number = {6},
  pages = {668--676},
  year = {1990},
  month = {June},
  doi = {10.1145/78973.78977},
  publisher = {ACM}
}
```

## Historical Significance

Skip lists, introduced by William Pugh in 1990, provide a simple probabilistic alternative to balanced trees like AVL trees and red-black trees. They are used in many practical systems including:
- Redis (sorted sets implementation)
- LevelDB and RocksDB (MemTable implementation)
- Lucene (inverted index skip lists)
- ConcurrentSkipListMap in Java

Their simplicity makes them easier to implement correctly than self-balancing trees, while still providing O(log n) expected time complexity for search, insertion, and deletion operations.

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Session ID: 2025-11-16
- Started: 2025-11-16
- Completed: 2025-11-16

## Section Breakdown
1. **00-abstract.md** (0.94) - Probabilistic alternative to balanced trees
2. **01-introduction.md** (0.88) - Motivation and comparison with traditional structures
3. **02-skip-lists.md** (0.87) - Algorithm descriptions (search, insert, delete)
4. **03-analysis.md** (0.86) - Mathematical analysis and complexity bounds
5. **04-implementation.md** (0.87) - Performance measurements and practical considerations
6. **05-conclusions.md** (0.88) - Summary, applications, and future work

**Overall Quality:** 0.88 (exceeds minimum threshold of 0.85)
