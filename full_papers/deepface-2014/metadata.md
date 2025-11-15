# DeepFace: Closing the Gap to Human-Level Performance in Face Verification
## DeepFace: سد الفجوة نحو الأداء البشري في التحقق من الوجه

**Paper ID:** deepface-2014
**Authors:** Yaniv Taigman, Ming Yang, Marc'Aurelio Ranzato, Lior Wolf
**Year:** 2014
**Publication:** IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2014
**Affiliation:** Facebook AI Research, Tel Aviv University
**Categories:** Computer Vision, Deep Learning, Face Recognition
**PDF:** https://www.cs.toronto.edu/~ranzato/publications/taigman_cvpr14.pdf
**Semantic Scholar:** https://www.semanticscholar.org/paper/DeepFace:-Closing-the-Gap-to-Human-Level-in-Face-Taigman-Yang/9f2efadf66817f1b38f58b3f50c7c8f34c69d89a

**Abstract Translation Quality:** 0.92
**Full Paper Translation Quality:** 0.893 (Average across 7 sections)

## Citation

```bibtex
@inproceedings{taigman2014deepface,
  title={DeepFace: Closing the Gap to Human-Level Performance in Face Verification},
  author={Taigman, Yaniv and Yang, Ming and Ranzato, Marc'Aurelio and Wolf, Lior},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages={1701--1708},
  year={2014}
}
```

## Paper Summary

DeepFace introduces a nine-layer deep neural network with more than 120 million parameters for face recognition. The system achieves 97.35% accuracy on the Labeled Faces in the Wild (LFW) dataset, closely approaching human-level performance (97.53%). Key contributions include:

1. **3D Face Alignment**: Explicit 3D face modeling for accurate alignment and frontalization
2. **Deep Architecture**: Nine-layer network using locally connected layers without weight sharing
3. **Large-Scale Training**: Trained on 4 million facial images from 4,000+ identities (Social Face Classification dataset)
4. **State-of-the-Art Results**: 97.35% on LFW, 91.4% on YouTube Faces dataset

The paper demonstrates that coupling accurate 3D model-based alignment with large-capacity deep networks trained on massive datasets can achieve near-human performance in unconstrained face recognition.

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Translation Notes

This paper is foundational to modern face recognition systems and introduced several important concepts:
- Locally connected layers (without weight sharing) for aligned face images
- 3D frontalization for robust alignment
- Demonstrating deep learning superiority over hand-crafted features in face recognition

Key terms to translate consistently:
- Face verification (التحقق من الوجه)
- Face recognition (التعرف على الوجوه)
- 3D alignment (المحاذاة ثلاثية الأبعاد)
- Frontalization (التحويل الأمامي)
- Locally connected layers (طبقات محلية الاتصال)
- Fiducial points (النقاط المرجعية)
- Deep neural network (الشبكة العصبية العميقة)
