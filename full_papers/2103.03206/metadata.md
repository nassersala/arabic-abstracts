# Perceiver: General Perception with Iterative Attention
## Perceiver: إدراك عام باستخدام الانتباه التكراري

**arXiv ID:** 2103.03206
**Authors:** Andrew Jaegle, Felix Gimeno, Andrew Brock, Andrew Zisserman, Oriol Vinyals, João Carreira
**Year:** 2021
**Publication:** ICML 2021 (International Conference on Machine Learning)
**Categories:** cs.CV, cs.AI, cs.LG, cs.SD, eess.AS
**Submission Date:** March 4, 2021 (v1); Revised June 23, 2021 (v2)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/2103.03206.pdf

**Abstract Translation Quality:** 0.90 (from translations/)
**Full Paper Translation Quality:** 0.876 ✅

## Abstract

Biological systems perceive the world by simultaneously processing high-dimensional inputs from modalities as diverse as vision, audition, touch, proprioception, etc. The perception models used in deep learning on the other hand are designed for individual modalities, often relying on domain-specific assumptions such as the local grid structures exploited by virtually all existing vision models. These priors introduce helpful inductive biases, but also lock models to individual modalities. In this paper we introduce the Perceiver - a model that builds upon Transformers and hence makes few architectural assumptions about the relationship between its inputs, but that also scales to hundreds of thousands of inputs, like ConvNets. The model leverages an asymmetric attention mechanism to iteratively distill inputs into a tight latent bottleneck, allowing it to scale to handle very large inputs. We show that this architecture is competitive with or outperforms strong, specialized models on classification tasks across various modalities: images, point clouds, audio, video, and video+audio. The Perceiver obtains performance comparable to ResNet-50 and ViT on ImageNet without 2D convolutions by directly attending to 50,000 pixels. It is also competitive in all modalities in AudioSet.

## Citation

```bibtex
@inproceedings{jaegle2021perceiver,
  title={Perceiver: General Perception with Iterative Attention},
  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Jo{\~a}o},
  booktitle={International Conference on Machine Learning},
  pages={4651--4664},
  year={2021},
  organization={PMLR}
}
```

## Translation Team
- Translator: Claude (Session 2025-11-16)
- Reviewer: TBD
- Started: 2025-11-16
- Completed: 2025-11-16 ✅

## Paper Significance

This is a foundational paper from DeepMind that introduces a general-purpose perception architecture capable of handling multiple modalities (vision, audio, video, point clouds) without domain-specific architectural assumptions. The Perceiver's asymmetric attention mechanism and latent bottleneck design represent an important step toward unified multimodal models, influencing subsequent work like Perceiver IO and multimodal foundation models.
