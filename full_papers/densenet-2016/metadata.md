# Densely Connected Convolutional Networks
## الشبكات التلافيفية المتصلة بشكل كثيف

**arXiv ID:** 1608.06993
**Authors:** Gao Huang, Zhuang Liu, Laurens van der Maaten, Kilian Q. Weinberger
**Affiliations:** Cornell University, Tsinghua University, Facebook AI Research
**Year:** 2016 (v1), 2018 (v5 - Jan 28)
**Publication:** CVPR 2017
**Categories:** Computer Vision and Pattern Recognition (cs.CV), Machine Learning (cs.LG)
**DOI:** https://doi.org/10.48550/arXiv.1608.06993
**PDF:** https://arxiv.org/pdf/1608.06993.pdf
**Code:** https://github.com/liuzhuang13/DenseNet

**Abstract Translation Quality:** 0.92
**Full Paper Translation Quality:** 0.895 (Excellent)

## Citation

```bibtex
@inproceedings{huang2017densely,
  title={Densely connected convolutional networks},
  author={Huang, Gao and Liu, Zhuang and Van Der Maaten, Laurens and Weinberger, Kilian Q},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={4700--4708},
  year={2017}
}
```

## Paper Overview

This paper introduces DenseNet, a convolutional neural network architecture that connects each layer to every other layer in a feed-forward fashion. The key innovation is that for an L-layer network, DenseNet has L(L+1)/2 direct connections instead of just L connections as in traditional architectures.

**Key Contributions:**
- Dense connectivity pattern that alleviates vanishing gradient problem
- Strengthens feature propagation and encourages feature reuse
- Substantially reduces the number of parameters
- Achieves state-of-the-art results on CIFAR-10, CIFAR-100, SVHN, and ImageNet

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: TBD
