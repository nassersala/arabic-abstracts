# Position: Categorical Deep Learning is an Algebraic Theory of All Architectures
## موقف: التعلم العميق الفئوي هو نظرية جبرية لجميع البنى المعمارية

**arXiv ID:** 2402.15332
**Authors:** Bruno Gavranović (Symbolica AI, University of Edinburgh), Paul Lessard (Symbolica AI), Andrew Dudzik (Google DeepMind), Tamara von Glehn (Google DeepMind), João G. M. Araújo (Google DeepMind), Petar Veličković (Google DeepMind, University of Cambridge)
**Year:** 2024
**Publication:** ICML 2024 (41st International Conference on Machine Learning, Vienna, Austria)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Category Theory (math.CT); Rings and Algebras (math.RA); Machine Learning (stat.ML)
**PDF:** https://arxiv.org/pdf/2402.15332.pdf
**Pages:** 32 pages (main paper) + extensive appendices

**Abstract Translation Quality:** 0.93 (from translations/2402.15332.md)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@inproceedings{gavranovic2024categorical,
  title={Position: Categorical Deep Learning is an Algebraic Theory of All Architectures},
  author={Gavranovi\'c, Bruno and Lessard, Paul and Dudzik, Andrew and von Glehn, Tamara and Ara\'ujo, Jo\~ao G. M. and Veli\v{c}kovi\'c, Petar},
  booktitle={Proceedings of the 41st International Conference on Machine Learning},
  year={2024},
  series={PMLR 235},
  address={Vienna, Austria}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-17
- Reviewer: TBD
- Started: 2025-11-17
- Completed: TBD

## Paper Overview

This position paper proposes applying category theory—specifically, the universal algebra of monads valued in a 2-category of parametric maps—as a unified framework for specifying and studying deep learning architectures. The authors demonstrate that this framework:

1. **Recovers Geometric Deep Learning**: Shows how constraints from geometric deep learning (equivariance, invariance) emerge naturally
2. **Describes Implementations**: Provides formal definitions for RNNs, recursive networks, and other architectures
3. **Bridges Top-Down and Bottom-Up**: Connects high-level constraints with low-level implementations
4. **Encodes CS Constructs**: Naturally represents lists, trees, automata, and other computer science structures

### Key Contributions

- **Monad Algebra Homomorphisms**: Generalization of equivariant maps from geometric deep learning
- **2-Category Para**: Framework for parametric morphisms that models weight sharing and weight tying
- **Lax Algebras**: Formal theory of recurrent/recursive neural networks via algebraically free monads
- **Universal Properties**: Shows RNNs, Mealy machines, and similar architectures arise from universal constructions

### Technical Scope

The paper combines concepts from:
- **Category Theory**: Functors, natural transformations, monads, 2-categories, adjunctions
- **Deep Learning**: Neural architectures, equivariance, geometric deep learning, RNNs
- **Computer Science**: Automata theory, functional programming, type theory
- **Algebra**: Universal algebra, algebraic theories, Lawvere theories
