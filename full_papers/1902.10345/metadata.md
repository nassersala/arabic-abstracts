# Stateful Dataflow Multigraphs: A Data-Centric Model for Performance Portability on Heterogeneous Architectures
## الرسوم البيانية المتعددة لتدفق البيانات الحافظة للحالة: نموذج محوري للبيانات لقابلية نقل الأداء على المعماريات غير المتجانسة

**arXiv ID:** 1902.10345
**Authors:** Tal Ben-Nun, Johannes de Fine Licht, Alexandros N. Ziogas, Timo Schneider, Torsten Hoefler
**Year:** 2019
**Publication:** SC '19: International Conference for High Performance Computing, Networking, Storage, and Analysis
**Categories:** Programming Languages (cs.PL); Distributed, Parallel, and Cluster Computing (cs.DC); Performance (cs.PF)
**DOI:** https://doi.org/10.1145/3295500.3356173
**PDF:** https://arxiv.org/pdf/1902.10345.pdf

**Abstract Translation Quality:** 0.92 (from translations/)
**Full Paper Translation Quality:** 0.87

## Citation

```bibtex
@inproceedings{Ben-Nun2019SDFG,
  title={Stateful Dataflow Multigraphs: A Data-Centric Model for Performance Portability on Heterogeneous Architectures},
  author={Tal Ben-Nun and Johannes de Fine Licht and Alexandros N. Ziogas and Timo Schneider and Torsten Hoefler},
  booktitle={SC '19: International Conference for High Performance Computing, Networking, Storage, and Analysis},
  year={2019},
  organization={ACM},
  doi={10.1145/3295500.3356173}
}
```

## Translation Team
- Translator: Claude (Session 2025-11-15)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Summary

This groundbreaking paper introduces Stateful Dataflow Multigraphs (SDFGs), a novel data-centric intermediate representation that addresses the growing complexity of programming heterogeneous high-performance computing systems. The authors present a complete framework that separates scientific code development from performance optimization, enabling domain scientists to write code once while performance engineers optimize it for different hardware platforms (CPUs, GPUs, FPGAs) without modifying the original source.

### Key Contributions:
1. **SDFG Representation**: A hierarchical graph-based IR combining fine-grained data dependencies with high-level control flow
2. **DaCe Framework**: Complete open-source implementation with Python/MATLAB/TensorFlow frontends
3. **DIODE IDE**: Interactive optimization environment for performance engineers
4. **Performance Results**: Competitive with expert-tuned libraries (98.6% of Intel MKL, 70% of CUBLAS), up to 5 orders of magnitude faster than naive FPGA synthesis

### Significance:
- Addresses performance portability crisis in HPC
- Enables strict separation of concerns between domain scientists and performance engineers
- Demonstrates practical viability across diverse workloads and hardware platforms
- Provides extensible transformation framework for code optimization
