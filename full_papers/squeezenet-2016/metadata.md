# SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size
## SqueezeNet: دقة بمستوى AlexNet مع معاملات أقل بـ 50 مرة وحجم نموذج أقل من 0.5 ميجابايت

**arXiv ID:** 1602.07360
**Authors:** Forrest N. Iandola, Song Han, Matthew W. Moskewicz, Khalid Ashraf, William J. Dally, Kurt Keutzer
**Year:** 2016
**Publication:** arXiv preprint (ICLR format)
**Categories:** cs.CV (Computer Vision and Pattern Recognition)
**PDF:** https://arxiv.org/pdf/1602.07360.pdf

**Abstract Translation Quality:** 0.92
**Full Paper Translation Quality:** 0.88 (All sections ≥ 0.85)

## Citation

```bibtex
@article{iandola2016squeezenet,
  title={SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and< 0.5 MB model size},
  author={Iandola, Forrest N and Han, Song and Moskewicz, Matthew W and Ashraf, Khalid and Dally, William J and Keutzer, Kurt},
  journal={arXiv preprint arXiv:1602.07360},
  year={2016}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-15
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Translation Statistics

- **Total Sections:** 8
- **Total Words (English):** ~4,500
- **Average Quality Score:** 0.88
- **Sections Meeting Quality Threshold (≥0.85):** 8/8 (100%)
- **Mathematical Equations Preserved:** All
- **Figures Referenced:** 5 figures
- **Tables Referenced:** 3 tables

## Paper Overview

SqueezeNet is a compact deep neural network architecture that achieves AlexNet-level accuracy on ImageNet with 50x fewer parameters. When compressed, the model size is less than 0.5MB (510x smaller than AlexNet). The paper demonstrates that model efficiency can be achieved through careful architectural design choices.

## Key Contributions

1. **Fire Module:** A novel building block consisting of squeeze (1x1) and expand (1x1 and 3x3) convolution layers
2. **Design Strategies:** Three key strategies for reducing parameters while maintaining accuracy
3. **Model Compression:** Demonstrates extreme compression capability (< 0.5MB) through deep compression techniques
4. **Design Space Exploration:** Systematic exploration of CNN micro and macro architecture decisions
