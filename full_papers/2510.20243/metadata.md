# HHEML: Hybrid Homomorphic Encryption for Privacy-Preserving Machine Learning on Edge
## HHEML: التشفير المتماثل الهجين للتعلم الآلي الحافظ للخصوصية على الحافة

**arXiv ID:** 2510.20243
**Authors:** Yu Hin Chan, Hao Yang, Shiyu Shen, Xingyu Fan, Shengzhe Lyu, Patrick S. Y. Hung, Ray C. C. Cheung
**Year:** 2025
**Publication:** arXiv preprint
**Categories:** cs.CR (Cryptography and Security), cs.DC (Distributed, Parallel, and Cluster Computing)
**DOI:** https://doi.org/10.48550/arXiv.2510.20243
**PDF:** https://arxiv.org/pdf/2510.20243.pdf

**Abstract Translation Quality:** 0.89
**Full Paper Translation Quality:** 0.875 (8 sections, all ≥0.86)

## Abstract

Privacy-preserving machine learning (PPML) is an emerging topic to handle secure machine learning inference over sensitive data in untrusted environments. Fully homomorphic encryption (FHE) enables computation directly on encrypted data on the server side, making it a promising approach for PPML. However, it introduces significant communication and computation overhead on the client side, making it impractical for edge devices. Hybrid homomorphic encryption (HHE) addresses this limitation by combining symmetric encryption (SE) with FHE to reduce the computational cost on the client side, and combining with an FHE-friendly SE can also lessen the processing overhead on the server side, making it a more balanced and efficient alternative. This work proposes a hardware-accelerated HHE architecture built around a lightweight symmetric cipher optimized for FHE compatibility and implemented as a dedicated hardware accelerator. Beyond this, the paper presents several microarchitectural optimizations to achieve higher performance and energy efficiency. The proposed work is integrated into a full PPML pipeline, enabling secure inference with significantly lower latency and power consumption than software implementations. Experiments on a PYNQ-Z2 platform with the MNIST dataset show over a 50× reduction in client-side encryption latency and nearly a 2× gain in hardware throughput compared to existing FPGA-based HHE accelerators.

## Key Contributions

1. First end-to-end HHE framework with hardware acceleration integrated into a full PPML pipeline
2. Hardware implementation of the Pasta cipher for efficient ciphertext transformation
3. Dual-XOF pipelined architecture achieving 2× throughput improvement
4. System-level evaluation demonstrating 50× lower client-side latency on PYNQ-Z2 FPGA

## Citation

```bibtex
@article{chan2025hheml,
  title={HHEML: Hybrid Homomorphic Encryption for Privacy-Preserving Machine Learning on Edge},
  author={Chan, Yu Hin and Yang, Hao and Shen, Shiyu and Fan, Xingyu and Lyu, Shengzhe and Hung, Patrick S. Y. and Cheung, Ray C. C.},
  journal={arXiv preprint arXiv:2510.20243},
  year={2025}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Session ID: 2025-11-17
- Started: 2025-11-17
- Completed: 2025-11-17

## Translation Quality Breakdown

All sections meet or exceed the target quality threshold of 0.85:

| Section | Quality Score |
|---------|---------------|
| 00 - Abstract | 0.89 |
| 01 - Introduction | 0.88 |
| 02 - Related Work | 0.87 |
| 03 - Background | 0.88 |
| 04 - HHEML | 0.87 |
| 05 - Hardware Design | 0.86 |
| 06 - Evaluation | 0.87 |
| 07 - Conclusion | 0.88 |
| **Overall Average** | **0.875** ✅ |

## Paper Significance

This paper represents cutting-edge research in hardware-accelerated homomorphic encryption, combining:
- **FHE**: Fully Homomorphic Encryption for secure computation on encrypted data
- **HHE**: Hybrid approach combining symmetric encryption with FHE for efficiency
- **Hardware Acceleration**: FPGA-based implementation on PYNQ-Z2 platform
- **Edge Computing**: Optimized for resource-constrained devices
- **Pasta Cipher**: FHE-friendly symmetric cipher designed for low multiplicative depth
- **PPML**: Privacy-Preserving Machine Learning applications

The work addresses critical challenges in deploying privacy-preserving ML on edge devices, making it highly relevant for IoT and edge computing scenarios.
