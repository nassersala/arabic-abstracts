# Mask R-CNN
## شبكة ماسك آر-سي إن إن

**arXiv ID:** 1703.06870
**Authors:** Kaiming He, Georgia Gkioxari, Piotr Dollár, Ross Girshick
**Year:** 2017
**Publication:** IEEE International Conference on Computer Vision (ICCV)
**Categories:** cs.CV (Computer Vision and Pattern Recognition)
**DOI:** 10.1109/ICCV.2017.322
**PDF:** https://arxiv.org/pdf/1703.06870.pdf

**Abstract Translation Quality:** 0.88
**Full Paper Translation Quality:** 0.876

## Citation

```bibtex
@inproceedings{he2017mask,
  title={Mask r-cnn},
  author={He, Kaiming and Gkioxari, Georgia and Doll{\'a}r, Piotr and Girshick, Ross},
  booktitle={Proceedings of the IEEE international conference on computer vision},
  pages={2961--2969},
  year={2017}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-15
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Summary

This paper presents Mask R-CNN, a conceptually simple, flexible, and general framework for object instance segmentation. Mask R-CNN extends Faster R-CNN by adding a branch for predicting an object mask in parallel with the existing branch for bounding box recognition. The method is simple to train and adds only a small overhead to Faster R-CNN, running at 5 fps. Mask R-CNN achieves top results in all three tracks of the COCO suite of challenges, including instance segmentation, bounding-box object detection, and person keypoint detection.

## Key Contributions

1. **RoIAlign Layer**: A novel spatial alignment layer that fixes the misalignment problem in RoIPool
2. **Decoupled Mask and Class Prediction**: Binary masks per class instead of multinomial masks
3. **Simple and Effective Architecture**: Extends Faster R-CNN with minimal overhead
4. **State-of-the-art Results**: Best performance on COCO 2016 challenges
5. **General Framework**: Successfully applied to keypoint detection as well
