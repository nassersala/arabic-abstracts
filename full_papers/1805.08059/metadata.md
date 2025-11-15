# One Monad to Prove Them All
## موناد واحد لإثباتها جميعاً

**arXiv ID:** 1805.08059
**Authors:** Sandra Dylus, Jan Christiansen, Finn Teegen
**Affiliations:**
- University of Kiel, Germany
- Flensburg University of Applied Sciences, Germany
**Year:** 2019
**Publication:** The Art, Science, and Engineering of Programming, vol. 3, no. 3, 2019, article 8; 32 pages
**Categories:** cs.PL (Programming Languages)
**DOI:** 10.22152/programming-journal.org/2019/3/8
**PDF:** https://arxiv.org/pdf/1805.08059.pdf
**Submitted:** September 25, 2018
**Published:** February 1, 2019

**Abstract Translation Quality:** 0.89 (from translations/)
**Full Paper Translation Quality:** TBD

## Keywords
Haskell, monads, free monad, containers, verification, proof assistant, Coq, functional programming

## Citation

```bibtex
@article{Dylus2019,
  author = {Sandra Dylus and Jan Christiansen and Finn Teegen},
  title = {One Monad to Prove Them All},
  journal = {The Art, Science, and Engineering of Programming},
  volume = {3},
  number = {3},
  year = {2019},
  pages = {8:1--8:32},
  doi = {10.22152/programming-journal.org/2019/3/8}
}
```

## ACM CCS 2012
- Theory of computation → Program verification
- Software and its engineering → Functional languages

## Abstract (English)

One Monad to Prove Them All is a modern fairy tale about curiosity and perseverance, two important properties of a successful PhD student. We follow the PhD student Mona on her adventure of proving properties about Haskell programs in the proof assistant Coq.

The paper addresses the challenge of translating Haskell functions into Coq while handling partiality through monadic representations. Building on prior work in Agda, the authors develop a novel approach using free monads and containers that overcomes limitations in Coq's termination checker. Their solution enables "monad-generic properties" rather than requiring separate proofs for each monad instance. The approach is evaluated through a case study comparing queue implementations.

## Translation Team
- Translator: Claude (Anthropic) - Session 2025-11-15
- Reviewer: TBD
- Started: 2025-11-15
- Completed: TBD

## Paper Structure
1. Preamble (Introduction)
2. The Problem (Strict Positivity Requirements)
3. The Solution (Free Monads and Containers)
4. A Simple Proof (Proving Associativity of Append)
5. A Case Study (Queue Implementations)
6. The End (Conclusion and Future Work)
- Appendix A: Technical Details

## Notes
This is a literate Coq file that can be compiled with Coq versions 8.7 and 8.8. The paper presents an educational narrative about formal verification of Haskell programs using dependent types.
