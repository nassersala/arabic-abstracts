# Rainblock: Faster Transaction Processing in Public Blockchains
## Rainblock: معالجة أسرع للمعاملات في سلاسل الكتل العامة

**arXiv ID:** 1909.11590
**Authors:** Soujanya Ponnapalli, Aashaka Shah, Souvik Banerjee, Dahlia Malkhi, Amy Tai, Vijay Chidambaram, Michael Wei
**Year:** 2019
**Publication:** 2021 USENIX Annual Technical Conference (ATC '21)
**Pages:** 333-347
**Categories:** cs.DC (Distributed, Parallel, and Cluster Computing)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1909.11590.pdf
**HTML:** https://ar5iv.labs.arxiv.org/html/1909.11590

**Abstract Translation Quality:** 0.91 (from translations/)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@inproceedings{ponnapalli2021rainblock,
  title={RainBlock: Faster Transaction Processing in Public Blockchains},
  author={Ponnapalli, Soujanya and Shah, Aashaka and Banerjee, Souvik and Malkhi, Dahlia and Tai, Amy and Chidambaram, Vijay and Wei, Michael},
  booktitle={2021 USENIX Annual Technical Conference (USENIX ATC 21)},
  pages={333--347},
  year={2021}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-16
- Reviewer: TBD
- Started: 2025-11-16
- Completed: TBD

## Paper Overview

This paper presents RAINBLOCK, a new architecture for public blockchains that increases transaction throughput without affecting security. The key innovation is tackling the I/O bottleneck on two fronts:
1. Decoupling transaction processing from I/O and removing I/O from the critical path
2. Reducing I/O amplification by customizing storage for blockchains using the novel Distributed Sharded Merkle tree (DSM-TREE)

**Performance:**
- Single miner: 27.4K transactions/second (27× improvement over Ethereum)
- Geo-distributed (4 regions, 3 continents): 20K transactions/second
