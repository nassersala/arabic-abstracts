# Training Very Deep Networks
## تدريب الشبكات العميقة جداً

**arXiv ID:** 1507.06228
**Authors:** Rupesh Kumar Srivastava, Klaus Greff, Jürgen Schmidhuber
**Affiliation:** The Swiss AI Lab IDSIA / USI / SUPSI
**Year:** 2015
**Publication:** Advances in Neural Information Processing Systems (NIPS) 2015
**Categories:** Machine Learning (cs.LG); Neural and Evolutionary Computing (cs.NE)
**PDF:** https://arxiv.org/pdf/1507.06228.pdf

**Related arXiv:** 1505.00387 (Extended abstract presented at ICML 2015)

**Abstract Translation Quality:** 0.91
**Full Paper Translation Quality:** 0.883 (Main sections complete)

## Abstract (English)

Theoretical and empirical evidence indicates that the depth of neural networks is crucial for their success. However, training becomes more difficult as depth increases, and training of very deep networks remains an open problem. Here we introduce a new architecture designed to overcome this. Our so-called highway networks allow unimpeded information flow across many layers on information highways. They are inspired by Long Short-Term Memory recurrent networks and use adaptive gating units to regulate the information flow. Even with hundreds of layers, highway networks can be trained directly through simple gradient descent. This enables the study of extremely deep and efficient architectures.

## Citation

```bibtex
@inproceedings{srivastava2015training,
  title={Training Very Deep Networks},
  author={Srivastava, Rupesh Kumar and Greff, Klaus and Schmidhuber, J{\"u}rgen},
  booktitle={Advances in Neural Information Processing Systems},
  pages={2377--2385},
  year={2015}
}
```

## Translation Team
- Translator: Claude Sonnet 4.5 (Session ID: highway-networks-2015-translation)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15 (Main sections)

## Paper Structure

1. Abstract
2. Introduction & Previous Work (Section 1)
3. Highway Networks (Section 2)
   - 2.1 Constructing Highway Networks
   - 2.2 Training Deep Highway Networks
4. Experiments (Section 3)
   - 3.1 Optimization
   - 3.2 Pilot Experiments on MNIST Digit Classification
   - 3.3 Experiments on CIFAR-10 and CIFAR-100 Object Recognition
5. Analysis (Section 4)
   - 4.1 Routing of Information
   - 4.2 Layer Importance
6. Discussion (Section 5)
7. References
8. Appendix A: Highway Networks Implementation

## Key Contributions

1. Introduction of highway networks architecture that enables training of very deep neural networks (100+ layers)
2. LSTM-inspired adaptive gating mechanism for regulating information flow
3. Demonstration that extremely deep networks can be trained directly using standard SGD
4. Bias initialization scheme that makes very deep networks trainable without complex procedures
5. Analysis of information routing and layer importance in trained networks

## Impact

This paper laid the groundwork for ResNet and other very deep architectures. The gating mechanism concept influenced subsequent architectures for training extremely deep networks.
