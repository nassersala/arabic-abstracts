# ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging
## ARIES: طريقة استرداد المعاملات الداعمة للقفل دقيق التفصيل والتراجع الجزئي باستخدام التسجيل المسبق للكتابة

**Paper ID:** ACM-TODS-1992-Mohan-ARIES
**Authors:** C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, Peter Schwarz
**Affiliation:** IBM Almaden Research Center
**Year:** 1992
**Publication:** ACM Transactions on Database Systems (TODS), Vol. 17, No. 1, March 1992
**Pages:** 94-162 (69 pages)
**Categories:** Database Systems, Transaction Processing, Recovery Algorithms
**DOI:** 10.1145/128765.128770
**PDF:** https://cs.stanford.edu/people/chrismre/cs345/rl/aries.pdf
**ACM DL:** https://dl.acm.org/doi/10.1145/128765.128770

**Abstract Translation Quality:** 0.94 (from translations/ACM-TODS-1992-Mohan-ARIES.md)
**Full Paper Translation Quality:** 0.88 ✅

## Paper Characteristics

**Length:** 69 pages (comprehensive technical paper)
**Format:** Academic research paper with formal structure
**Key Topics:**
- Write-Ahead Logging (WAL) protocol
- Transaction recovery algorithms
- Log Sequence Numbers (LSNs)
- Compensation Log Records (CLRs)
- Three-phase recovery: Analysis, Redo, Undo
- Fine-granularity locking
- Partial transaction rollback
- No-Force, Steal buffer management policy

## Historical Significance

This paper is considered one of the most influential papers in database systems:
- Established the standard recovery algorithm used in most modern DBMS
- Introduced concepts now fundamental to transaction processing
- Implemented in IBM DB2, IMS, Microsoft SQL Server, PostgreSQL, and many others
- Over 3,000 citations (highly influential)
- Winner of the SIGMOD Test of Time Award
- Still the basis for recovery in modern databases

## Citation

```bibtex
@article{Mohan1992ARIES,
  author = {Mohan, C. and Haderle, Don and Lindsay, Bruce and Pirahesh, Hamid and Schwarz, Peter},
  title = {{ARIES}: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging},
  journal = {ACM Transactions on Database Systems},
  volume = {17},
  number = {1},
  pages = {94--162},
  year = {1992},
  month = {March},
  doi = {10.1145/128765.128770},
  publisher = {ACM}
}
```

## Translation Team

- Translator: Claude (Session: 012kFR98YbEaPoBK1WKXzYFT)
- Abstract Reviewer: Completed (score: 0.94)
- Full Paper Reviewer: Completed (score: 0.88)
- Started: 2025-11-16
- Completed: 2025-11-16

## Sources

- **ACM Digital Library:** https://dl.acm.org/doi/10.1145/128765.128770
- **Stanford CS345 (PDF):** https://cs.stanford.edu/people/chrismre/cs345/rl/aries.pdf
- **IBM Research:** IBM Almaden Research Center Technical Reports
- **Wikipedia:** https://en.wikipedia.org/wiki/Algorithms_for_Recovery_and_Isolation_Exploiting_Semantics
