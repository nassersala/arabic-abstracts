# BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers
## BEVFormer: تعلم تمثيل منظور عين الطائر من صور الكاميرات المتعددة عبر المحولات الزمكانية

**arXiv ID:** 2203.17270
**Authors:** Zhiqi Li, Wenhai Wang, Hongyang Li, Enze Xie, Chonghao Sima, Tong Lu, Yu Qiao, Jifeng Dai
**Year:** 2022
**Publication:** ECCV 2022 (European Conference on Computer Vision)
**Categories:** cs.CV (Computer Vision and Pattern Recognition)
**DOI:** https://doi.org/10.48550/arXiv.2203.17270
**PDF:** https://arxiv.org/pdf/2203.17270.pdf

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@inproceedings{li2022bevformer,
  title={BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers},
  author={Li, Zhiqi and Wang, Wenhai and Li, Hongyang and Xie, Enze and Sima, Chonghao and Lu, Tong and Qiao, Yu and Dai, Jifeng},
  booktitle={European Conference on Computer Vision (ECCV)},
  year={2022}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-17
- Reviewer: TBD
- Started: 2025-11-17
- Completed: TBD

## Paper Summary

This paper presents BEVFormer, a unified framework for 3D visual perception in autonomous driving that generates bird's-eye-view (BEV) representations from multi-camera images using spatiotemporal transformers. The key innovations are:

1. **Grid-shaped BEV queries** that serve as learnable parameters to aggregate spatial and temporal information
2. **Spatial cross-attention** that enables each query to extract features across camera views
3. **Temporal self-attention** that recurrently fuses historical BEV features

The approach achieves 56.9% NDS on nuScenes test set, outperforming previous camera-based methods by 9.0 points and matching LiDAR-based systems. It demonstrates significant improvements in velocity estimation and object detection under low-visibility conditions.

## Domain

- **Primary:** Computer Vision
- **Secondary:** Autonomous Driving, 3D Perception, Deep Learning
- **Applications:** Self-driving cars, multi-camera perception, BEV representation learning
