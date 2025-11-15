# Playing Atari with Deep Reinforcement Learning
## لعب Atari باستخدام التعلم المعزز العميق

**arXiv ID:** 1312.5602
**Authors:** Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller
**Year:** 2013
**Publication:** NIPS Deep Learning Workshop 2013
**Categories:** cs.LG (Machine Learning)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1312.5602.pdf

**Abstract Translation Quality:** 0.92 (from translations/)
**Full Paper Translation Quality:** 0.884

## Citation

```bibtex
@article{mnih2013playing,
  title={Playing atari with deep reinforcement learning},
  author={Mnih, Volodymyr and Kavukcuoglu, Koray and Silver, David and Graves, Alex and Antonoglou, Ioannis and Wierstra, Daan and Riedmiller, Martin},
  journal={arXiv preprint arXiv:1312.5602},
  year={2013}
}
```

## Translation Team
- Translator: Claude (Session 2025-11-15)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Significance

This is one of the most influential papers in deep reinforcement learning, introducing Deep Q-Networks (DQN). It demonstrated for the first time that deep neural networks could learn control policies directly from high-dimensional sensory input (raw pixels) using reinforcement learning. The paper established the foundation for modern deep RL and proved that combining deep learning with Q-learning could work contrary to earlier theoretical concerns.

Key contributions:
- First successful application of deep learning to RL with high-dimensional inputs
- Introduction of experience replay for stabilizing deep Q-learning
- Demonstrated super-human performance on Atari games without hand-crafted features
- Single architecture and hyperparameters across multiple games
