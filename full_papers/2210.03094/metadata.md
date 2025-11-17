# VIMA: General Robot Manipulation with Multimodal Prompts
## VIMA: التلاعب الروبوتي العام بموجهات متعددة الوسائط

**arXiv ID:** 2210.03094
**Authors:** Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen, Li Fei-Fei, Anima Anandkumar, Yuke Zhu, Linxi Fan
**Year:** 2022 (Submitted: October 6, 2022; Revised: May 28, 2023)
**Publication:** ICML 2023 (International Conference on Machine Learning)
**Categories:** cs.RO (Robotics), cs.AI (Artificial Intelligence), cs.LG (Machine Learning)
**DOI:** https://doi.org/10.48550/arXiv.2210.03094
**PDF:** https://arxiv.org/pdf/2210.03094.pdf
**Project Website:** https://vimalabs.github.io
**License:** CC BY 4.0

**Abstract Translation Quality:** 0.93 (from translations/)
**Full Paper Translation Quality:** 0.88 ✅

## Citation

```bibtex
@inproceedings{jiang2023vima,
  title={VIMA: General Robot Manipulation with Multimodal Prompts},
  author={Jiang, Yunfan and Gupta, Agrim and Zhang, Zichen and Wang, Guanzhi and Dou, Yongqiang and Chen, Yanjun and Fei-Fei, Li and Anandkumar, Anima and Zhu, Yuke and Fan, Linxi},
  booktitle={International Conference on Machine Learning},
  year={2023}
}
```

## Translation Team
- Translator: Claude (Session 2025-11-17)
- Reviewer: TBD
- Started: 2025-11-17
- Completed: 2025-11-17 ✅

## Paper Summary

This paper introduces VIMA (VisuoMotor Attention agent), a transformer-based robot learning system that processes multimodal prompts combining text and images to perform diverse manipulation tasks. Key contributions include:

1. **Multimodal Prompting Formulation**: Unifies various robot manipulation tasks through multimodal prompts
2. **VIMA-Bench Benchmark**: Simulation environment with 17 task templates, 650K+ expert trajectories
3. **VIMA Architecture**: Encoder-decoder transformer with object-centric visual tokenization
4. **Strong Performance**: 2.9× better zero-shot generalization, 2.7× better with 10× less data

## Technical Highlights

- Object-centric visual tokenization using Mask R-CNN
- Pre-trained T5 language model for text encoding
- Cross-attention conditioning between prompts and robot controller
- Four-level evaluation protocol for systematic generalization testing
