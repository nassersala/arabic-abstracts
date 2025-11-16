# Charlotte: Composable Authenticated Distributed Data Structures, Technical Report
## Charlotte: بنى البيانات الموزعة المصادق عليها والقابلة للتركيب، تقرير تقني

**arXiv ID:** 1905.03888
**Authors:** Isaac Sheff, Xinwen Wang, Haobin Ni, Robbert van Renesse, Andrew C. Myers
**Year:** 2019
**Publication:** Technical Report (arXiv)
**Categories:** cs.DC (Distributed, Parallel, and Cluster Computing); cs.CR (Cryptography and Security)
**DOI:** N/A (Technical Report)
**PDF:** https://arxiv.org/pdf/1905.03888.pdf

**Abstract Translation Quality:** 0.90 (from translations/)
**Full Paper Translation Quality:** In Progress

## Citation

```bibtex
@article{sheff2019charlotte,
  title={Charlotte: Composable Authenticated Distributed Data Structures, Technical Report},
  author={Sheff, Isaac and Wang, Xinwen and Ni, Haobin and van Renesse, Robbert and Myers, Andrew C.},
  journal={arXiv preprint arXiv:1905.03888},
  year={2019}
}
```

## Translation Team
- Translator: Claude Code (Session 2025-11-16)
- Reviewer: TBD
- Started: 2025-11-16
- Completed: In Progress

## Paper Summary

Charlotte introduces a framework for building composable, authenticated distributed data structures. The system uses hash-based references between data blocks to form a "blockweb" (directed acyclic graph). This enables applications to operate independently when possible and share blocks when desired, while supporting heterogeneous trust models where different observers maintain distinct beliefs about system failures. Key contributions include mechanisms for data immutability, self-authentication, and implementations demonstrating both consensus and proof-of-work approaches.
