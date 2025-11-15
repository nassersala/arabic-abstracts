# SSD: Single Shot MultiBox Detector
## كاشف الأجسام أحادي الطلقة متعدد الصناديق (SSD)

**arXiv ID:** 1512.02325
**Authors:** Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg
**Year:** 2016 (ECCV 2016, submitted December 2015)
**Publication:** European Conference on Computer Vision (ECCV)
**Categories:** cs.CV (Computer Vision and Pattern Recognition)
**DOI:** TBD
**PDF:** https://arxiv.org/pdf/1512.02325.pdf

**Abstract Translation Quality:** 0.90
**Full Paper Translation Quality:** 0.873 (Excellent - All sections ≥ 0.86)

## Citation

```bibtex
@inproceedings{liu2016ssd,
  title={SSD: Single shot multibox detector},
  author={Liu, Wei and Anguelov, Dragomir and Erhan, Dumitru and Szegedy, Christian and Reed, Scott and Fu, Cheng-Yang and Berg, Alexander C},
  booktitle={European conference on computer vision},
  pages={21--37},
  year={2016},
  organization={Springer}
}
```

## Translation Team
- Translator: Claude (Session: 2025-11-15)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Overview
SSD presents a method for detecting objects in images using a single deep neural network. The approach discretizes bounding box outputs into default boxes across different aspect ratios and scales, and combines predictions from multiple feature maps to handle varying object sizes. Achieves 72.1% mAP on VOC2007 at 58 FPS (300×300 input) and 75.1% mAP (500×500 input).
