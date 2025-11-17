# Privacy-Preserving Machine Learning with Fully Homomorphic Encryption for Deep Neural Network
## تعلم الآلة الحافظ للخصوصية مع التشفير المتماثل الكامل للشبكات العصبية العميقة

**arXiv ID:** 2106.07229
**Authors:** Joon-Woo Lee, HyungChul Kang, Yongwoo Lee, Woosuk Choi, Jieun Eom, Maxim Deryabin, Eunsang Lee, Junghyun Lee, Donghoon Yoo, Young-Sik Kim, Jong-Seon No
**Year:** 2021
**Publication:** arXiv preprint (Submitted June 14, 2021)
**Categories:** cs.LG (Machine Learning), cs.CR (Cryptography and Security)
**DOI:** N/A (preprint)
**PDF:** https://arxiv.org/pdf/2106.07229.pdf
**Pages:** 12

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@article{lee2021privacy,
  title={Privacy-Preserving Machine Learning with Fully Homomorphic Encryption for Deep Neural Network},
  author={Lee, Joon-Woo and Kang, HyungChul and Lee, Yongwoo and Choi, Woosuk and Eom, Jieun and Deryabin, Maxim and Lee, Eunsang and Lee, Junghyun and Yoo, Donghoon and Kim, Young-Sik and No, Jong-Seon},
  journal={arXiv preprint arXiv:2106.07229},
  year={2021}
}
```

## Paper Summary

This groundbreaking paper implements ResNet-20 using RNS-CKKS fully homomorphic encryption (FHE) with bootstrapping for privacy-preserving machine learning on the CIFAR-10 dataset. Key achievements:

- **First implementation** of standard ResNet-20 with FHE and bootstrapping
- **90.67% accuracy** on CIFAR-10 (previous FHE best: 77%)
- **98.67% agreement** with plaintext ResNet-20 results
- Uses state-of-the-art approximation methods for ReLU (not simple polynomial replacements)
- **First FHE implementation** of softmax function (prevents model extraction attacks)
- Requires 1,149 bootstrapping operations
- Inference time: ~4 hours on dual Intel Xeon Platinum 8280 CPU (112 cores)

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Session: 2025-11-17
- Started: 2025-11-17
- Completed: TBD

## Technical Significance

**Cryptography Contributions:**
- Advanced bootstrapping implementation with failure probability < 2^-40
- First practical use of RNS-CKKS bootstrapping in deep neural networks
- Novel handling of non-arithmetic functions (ReLU, softmax) via minimax approximation

**Machine Learning Contributions:**
- Proves FHE can support standard deep learning architectures (not just HE-friendly networks)
- Enables encrypted inference without retraining models
- Demonstrates feasibility of privacy-preserving ML at scale

**Key Innovation:** Unlike previous work that replaced activation functions with simple polynomials, this work uses precise polynomial approximations of standard functions, enabling much higher accuracy.
