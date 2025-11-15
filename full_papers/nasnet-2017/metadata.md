# Learning Transferable Architectures for Scalable Image Recognition
## تعلم معماريات قابلة للنقل للتعرف على الصور القابلة للتوسع

**arXiv ID:** 1707.07012
**Authors:** Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le
**Year:** 2017
**Publication:** IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2018
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Learning (cs.LG); Neural and Evolutionary Computing (cs.NE)
**DOI:** 10.1109/CVPR.2018.00907
**PDF:** https://arxiv.org/pdf/1707.07012.pdf

**Abstract Translation Quality:** 0.91
**Full Paper Translation Quality:** 0.89

## Citation

```bibtex
@article{zoph2017learning,
  title={Learning Transferable Architectures for Scalable Image Recognition},
  author={Zoph, Barret and Vasudevan, Vijay and Shlens, Jonathon and Le, Quoc V},
  journal={arXiv preprint arXiv:1707.07012},
  year={2017}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Summary

This paper introduces NASNet, a neural architecture search method that learns optimal convolutional architectures automatically. The key innovation is the "NASNet search space" which enables transferability - searching for the best convolutional cell on CIFAR-10 and transferring it to ImageNet. The resulting architecture achieves state-of-the-art accuracy (82.7% top-1 on ImageNet, 2.4% error on CIFAR-10) while being 28% more computationally efficient than previous best models.
