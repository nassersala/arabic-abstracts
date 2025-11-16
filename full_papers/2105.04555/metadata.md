# Customized Monte Carlo Tree Search for LLVM/Polly's Composable Loop Optimization Transformations
## بحث شجرة مونت كارلو المخصص لتحويلات تحسين الحلقات القابلة للتركيب في LLVM/Polly

**arXiv ID:** 2105.04555
**Authors:** Jaehoon Koo, Prasanna Balaprakash, Michael Kruse, Xingfu Wu, Paul Hovland, Mary Hall
**Affiliations:**
- Argonne National Laboratory (Mathematics and Computer Science Division)
- University of Utah (School of Computing)

**Year:** 2021
**Publication:** 2021 International Workshop on Performance Modeling, Benchmarking and Simulation of High Performance Computer Systems (PMBS)
**Pages:** 82-93
**Categories:** cs.PL (Programming Languages), cs.AI (Artificial Intelligence), cs.DC (Distributed/Parallel Computing), cs.LG (Machine Learning), cs.PF (Performance)
**DOI:** 10.1109/PMBS54543.2021.00015
**arXiv DOI:** https://doi.org/10.48550/arXiv.2105.04555
**PDF:** https://arxiv.org/pdf/2105.04555.pdf
**IEEE Xplore:** https://ieeexplore.ieee.org/document/9652671/

**Keywords:** autotuning, Clang, Polly, loop optimization, Monte Carlo Tree Search, polyhedral compilation, compiler optimization, pragma directives

**Abstract Translation Quality:** 0.91 (from translations/2105.04555.md)
**Full Paper Translation Quality:** 0.875 (average across all 8 sections) ✅

**Citation Count:** 7 (as of IEEE Xplore)
**Downloads:** 266 (IEEE Xplore)

## Citation

```bibtex
@inproceedings{koo2021customized,
  title={Customized Monte Carlo Tree Search for LLVM/Polly's Composable Loop Optimization Transformations},
  author={Koo, Jaehoon and Balaprakash, Prasanna and Kruse, Michael and Wu, Xingfu and Hovland, Paul and Hall, Mary},
  booktitle={2021 International Workshop on Performance Modeling, Benchmarking and Simulation of High Performance Computer Systems (PMBS)},
  pages={82--93},
  year={2021},
  organization={IEEE},
  doi={10.1109/PMBS54543.2021.00015}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Session 2025-11-16
- Reviewer: TBD
- Started: 2025-11-16
- Completed: 2025-11-16 ✅

## Paper Summary

This paper addresses the challenge of finding optimal combinations of loop transformations in the LLVM/Polly compiler framework. The authors develop a customized Monte Carlo Tree Search (MCTS) algorithm to navigate the tree-structured search space of composable loop transformations exposed by Clang/Polly pragma directives.

### Key Contributions:
1. **Tree-based search space modeling**: Representing loop transformation combinations as a tree where each node is a specific optimization sequence
2. **Customized MCTS algorithm**: Two-phase approach combining exploration and exploitation with a restart mechanism
3. **Empirical evaluation**: Comparison with random, greedy, and breadth-first search on PolyBench kernels and ECP proxy applications
4. **Significant performance gains**: 2.3× average speedup over Polly's default heuristic optimizations

### Related Work:
- User-Directed Loop-Transformations in Clang (Kruse et al., 2018)
- Autotuning Search Space for Loop Transformations (2020)
- Polyhedral compilation and optimization techniques
