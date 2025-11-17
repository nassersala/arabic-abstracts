# OASIS: Object-based Analytics Storage for Intelligent SQL Query Offloading in Scientific Tabular Workloads
## OASIS: تخزين تحليلي قائم على الكائنات لتفريغ استعلامات SQL الذكية في أحمال العمل الجدولية العلمية

**arXiv ID:** 2509.01966
**Authors:** Soon Hwang, Junhyeok Park, Junghyun Ryu, Seonghoon Ahn, Jeoungahn Park, Jeongjin Lee, Soonyeal Yang, Jungki Noh, Woosuk Chung, Hoshik Kim, and Youngjae Kim
**Year:** 2025
**Publication:** arXiv preprint
**Categories:** cs.DB (Databases); cs.DC (Distributed, Parallel, and Cluster Computing)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/2509.01966.pdf

**Abstract Translation Quality:** 0.88 (from translations/2509.01966.md)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@article{hwang2025oasis,
  title={OASIS: Object-based Analytics Storage for Intelligent SQL Query Offloading in Scientific Tabular Workloads},
  author={Hwang, Soon and Park, Junhyeok and Ryu, Junghyun and Ahn, Seonghoon and Park, Jeoungahn and Lee, Jeongjin and Yang, Soonyeal and Noh, Jungki and Chung, Woosuk and Kim, Hoshik and Kim, Youngjae},
  journal={arXiv preprint arXiv:2509.01966},
  year={2025}
}
```

## Translation Team
- Translator: Claude Code (Session 2025-11-17)
- Reviewer: TBD
- Started: 2025-11-17
- Completed: TBD

## Paper Summary

This paper presents OASIS, a novel Computation-Enabled Object Storage (COS) system designed for SQL-based analytics in High-Performance Computing (HPC) environments. The system addresses three key limitations of existing COS systems:
1. Inflexible output formats that limit optimization
2. Limited support for complex operators and array-based expressions
3. Excessive inter-storage data movement due to fixed execution layers

OASIS achieves up to 32.7% performance improvement over Apache Spark with existing COS-based storage systems through:
- Flexible columnar output formats (Apache Arrow)
- Support for advanced operators (aggregate, sort) and array-aware expressions
- Dynamic query plan optimization across hierarchical storage layers (SODA algorithm)

The system is particularly relevant for scientific workloads in domains like Computational Fluid Dynamics (CFD), High-Energy Physics (HEP), and Particle-In-Cell (PIC) simulations.
