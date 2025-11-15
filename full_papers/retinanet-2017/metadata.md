# Focal Loss for Dense Object Detection
## الخسارة المُركزة لكشف الأجسام الكثيف

**arXiv ID:** 1708.02002
**Authors:** Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, Piotr Dollár
**Year:** 2017 (Submitted: Aug 7, 2017; Revised: Feb 7, 2018)
**Publication:** IEEE International Conference on Computer Vision (ICCV) 2017
**Categories:** cs.CV (Computer Vision and Pattern Recognition)
**DOI:** 10.1109/ICCV.2017.324
**PDF:** https://arxiv.org/pdf/1708.02002.pdf
**Code:** https://github.com/facebookresearch/Detectron

**Abstract Translation Quality:** 0.91
**Full Paper Translation Quality:** 0.903

## Citation

```bibtex
@inproceedings{lin2017focal,
  title={Focal loss for dense object detection},
  author={Lin, Tsung-Yi and Goyal, Priya and Girshick, Ross and He, Kaiming and Doll{\'a}r, Piotr},
  booktitle={Proceedings of the IEEE international conference on computer vision},
  pages={2980--2988},
  year={2017}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Summary

This landmark paper introduces the Focal Loss, a novel loss function designed to address class imbalance in dense object detection. The authors propose RetinaNet, a simple one-stage object detector that achieves state-of-the-art accuracy while maintaining real-time performance. The focal loss down-weights the contribution of easy examples during training, allowing the model to focus on hard, misclassified examples. This work revolutionized one-stage object detection and has been widely adopted in computer vision applications.

**Key Contributions:**
1. Identification of class imbalance as the primary obstacle for one-stage detectors
2. Introduction of Focal Loss to address this imbalance
3. RetinaNet architecture combining Feature Pyramid Networks with anchor-based detection
4. State-of-the-art results surpassing two-stage detectors while maintaining speed
