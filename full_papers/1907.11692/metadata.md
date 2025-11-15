# RoBERTa: A Robustly Optimized BERT Pretraining Approach
## RoBERTa: نهج محسّن بقوة للتدريب المسبق لـ BERT

**arXiv ID:** 1907.11692
**Authors:** Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov
**Affiliations:**
- Paul G. Allen School of Computer Science & Engineering, University of Washington
- Facebook AI
**Year:** 2019
**Publication:** arXiv preprint
**Categories:** Computation and Language (cs.CL)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1907.11692.pdf

**Abstract Translation Quality:** 0.94 (from translations/1907.11692.md)
**Full Paper Translation Quality:** 0.87 ✅ (Exceeds minimum 0.85 requirement)

## Citation

```bibtex
@article{liu2019roberta,
  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},
  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
  journal={arXiv preprint arXiv:1907.11692},
  year={2019}
}
```

## Paper Overview

This paper presents RoBERTa (Robustly optimized BERT approach), a replication study of BERT pretraining that carefully measures the impact of key hyperparameters and training data size. The study demonstrates that BERT was significantly undertrained and proposes improvements including:

1. Training longer with bigger batches over more data
2. Removing the Next Sentence Prediction (NSP) objective
3. Training on longer sequences
4. Dynamically changing the masking pattern

The paper achieves state-of-the-art results on GLUE, RACE, and SQuAD benchmarks.

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15 ✅

## Translation Notes

This is a critical NLP paper that:
- Introduces important design choices for BERT-style pretraining
- Contains extensive experimental ablations and hyperparameter studies
- Presents results on multiple benchmarks (GLUE, SQuAD, RACE)
- Includes detailed tables with numerical results that must be preserved accurately
- Discusses technical concepts like masked language modeling, dynamic masking, batch size effects

Special attention required for:
- Preserving all numerical results in tables
- Accurately translating experimental methodology
- Maintaining consistency with BERT paper terminology
- Handling benchmark names (GLUE, SQuAD, RACE) appropriately
