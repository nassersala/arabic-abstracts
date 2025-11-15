# Spatial Transformer Networks
## شبكات المحوّل المكاني

**arXiv ID:** 1506.02025
**Authors:** Max Jaderberg, Karen Simonyan, Andrew Zisserman, Koray Kavukcuoglu
**Year:** 2015
**Publication:** Neural Information Processing Systems (NIPS 2015)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)
**DOI:** https://doi.org/10.48550/arXiv.1506.02025
**PDF:** https://arxiv.org/pdf/1506.02025.pdf

**Abstract Translation Quality:** 0.88
**Full Paper Translation Quality:** 0.87

## Citation

```bibtex
@inproceedings{jaderberg2015spatial,
  title={Spatial Transformer Networks},
  author={Jaderberg, Max and Simonyan, Karen and Zisserman, Andrew and Kavukcuoglu, Koray},
  booktitle={Advances in Neural Information Processing Systems},
  volume={28},
  year={2015}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-15
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Overview

This foundational paper introduces the Spatial Transformer module, a differentiable component that can be inserted into convolutional neural networks to explicitly handle spatial transformations of feature maps. The module learns to actively transform data within the network, enabling invariance to translation, scale, rotation, and more generic warping without extra supervision or modifications to the optimization process.

### Key Contributions
1. Introduction of the Spatial Transformer module
2. Three-component architecture: Localisation Network, Parameterised Sampling Grid, and Differentiable Image Sampling
3. Demonstration of learned spatial invariance
4. State-of-the-art performance on multiple benchmarks

### Impact
- Influential work in computer vision and deep learning
- Introduced explicit spatial manipulation capabilities to neural networks
- Widely cited and adopted in various vision tasks
