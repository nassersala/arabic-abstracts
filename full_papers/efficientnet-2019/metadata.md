# EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
## EfficientNet: إعادة التفكير في توسيع النموذج للشبكات العصبية الالتفافية

**arXiv ID:** 1905.11946
**Authors:** Mingxing Tan, Quoc V. Le
**Year:** 2019
**Publication:** Proceedings of the 36th International Conference on Machine Learning (ICML 2019), PMLR 97:6105-6114
**Categories:** Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (stat.ML)
**DOI:** https://doi.org/10.48550/arXiv.1905.11946
**PDF:** https://arxiv.org/pdf/1905.11946.pdf
**Code:** https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet

**Abstract Translation Quality:** 0.91 (from translations/)
**Full Paper Translation Quality:** 0.886 (averaged across 7 sections)

## Citation

```bibtex
@inproceedings{tan2019efficientnet,
  title={Efficientnet: Rethinking model scaling for convolutional neural networks},
  author={Tan, Mingxing and Le, Quoc},
  booktitle={International conference on machine learning},
  pages={6105--6114},
  year={2019},
  organization={PMLR}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Summary

This influential paper introduces EfficientNet, a new family of convolutional neural networks that achieves state-of-the-art accuracy while being significantly more efficient than previous models. The key innovation is a compound scaling method that uniformly scales network depth, width, and resolution using a simple compound coefficient. EfficientNet-B7 achieved 84.3% top-1 accuracy on ImageNet while being 8.4x smaller and 6.1x faster than the best existing ConvNet at the time.

## Sections Structure

1. **Abstract** - Overview of compound scaling and main results
2. **Introduction** - Problem motivation and key contributions
3. **Related Work** - ConvNet efficiency and model scaling literature
4. **Compound Model Scaling** - Theoretical foundation and scaling methodology
5. **EfficientNet Architecture** - Neural architecture search and baseline network design
6. **Experiments** - ImageNet results, transfer learning, and ablation studies
7. **Discussion** - Analysis and insights
8. **Conclusion** - Summary and future directions
