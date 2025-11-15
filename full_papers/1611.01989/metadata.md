# DeepCoder: Learning to Write Programs
## DeepCoder: تعلم كتابة البرامج

**arXiv ID:** 1611.01989
**Authors:** Matej Balog, Alexander L. Gaunt, Marc Brockschmidt, Sebastian Nowozin, Daniel Tarlow
**Year:** 2016 (Published at ICLR 2017)
**Publication:** International Conference on Learning Representations (ICLR 2017)
**Categories:** Machine Learning (cs.LG)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1611.01989.pdf

**Abstract Translation Quality:** 0.93 (from translations/)
**Full Paper Translation Quality:** 0.875 (Average of all sections)

## Citation

```bibtex
@inproceedings{balog2017deepcoder,
  title={DeepCoder: Learning to Write Programs},
  author={Balog, Matej and Gaunt, Alexander L and Brockschmidt, Marc and Nowozin, Sebastian and Tarlow, Daniel},
  booktitle={International Conference on Learning Representations},
  year={2017}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Summary

DeepCoder is a pioneering work that combines deep learning with program synthesis. The paper presents a novel approach to solving programming competition-style problems from input-output examples by training a neural network to predict properties of programs. The neural network's predictions are used to guide traditional search-based program synthesis techniques (DFS, SMT solvers, enumerative search), achieving order-of-magnitude speedups.

## Key Contributions

1. **LIPS Framework**: Learning Inductive Program Synthesis - a framework for using machine learning to guide program synthesis
2. **DSL Design**: A domain-specific language expressive enough for programming competition problems
3. **Neural Guidance**: Using neural networks to predict function usage from input-output examples
4. **Empirical Results**: Orders of magnitude speedup over baseline approaches (15-900× faster)

## Technical Highlights

- **Problem**: Inductive program synthesis from input-output examples
- **Approach**: Learn to predict program attributes (which functions appear) from examples
- **Architecture**: Feed-forward encoder with binary classifiers for function prediction
- **Search Integration**: Neural predictions guide DFS, Sort-and-Add, Sketch, and λ2 solvers
- **Results**: Solves programs of length 5 with ~10^10 search space

## Sections Structure

1. Introduction
2. Background on Inductive Program Synthesis
3. Learning Inductive Program Synthesis (LIPS)
4. DeepCoder (Method)
   - 4.1 Domain Specific Language and Attributes
   - 4.2 Data Generation
   - 4.3 Machine Learning Model
   - 4.4 Search
   - 4.5 Training Loss Function
5. Experiments
   - 5.1 DeepCoder Compared to Baselines
   - 5.2 Generalization Across Program Lengths
   - 5.3 Alternative Models
6. Related Work
7. Discussion and Future Work
