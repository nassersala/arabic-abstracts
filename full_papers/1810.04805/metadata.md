# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
## BERT: التدريب المسبق للمحولات العميقة ثنائية الاتجاه لفهم اللغة

**arXiv ID:** 1810.04805
**Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
**Year:** 2018
**Publication:** NAACL 2019
**Categories:** Computation and Language (cs.CL)
**PDF:** https://arxiv.org/pdf/1810.04805.pdf

**Abstract Translation Quality:** 0.95 (from translations/)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@inproceedings{devlin-etal-2019-bert,
    title = "{BERT}: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    author = "Devlin, Jacob  and
      Chang, Ming-Wei  and
      Lee, Kenton  and
      Toutanova, Kristina",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1423",
    doi = "10.18653/v1/N19-1423",
    pages = "4171--4186"
}
```

## Paper Overview

BERT (Bidirectional Encoder Representations from Transformers) is one of the most influential papers in natural language processing. It introduced a new method for pre-training language representations that enabled deep bidirectional understanding of context. BERT achieved state-of-the-art results on 11 NLP tasks and revolutionized the field.

### Key Contributions
1. Masked Language Model (MLM) pre-training objective
2. Next Sentence Prediction (NSP) task for understanding sentence relationships
3. Deep bidirectional Transformer architecture
4. Demonstrated the power of transfer learning in NLP
5. Open-sourced pre-trained models and code

### Impact
- Cited over 100,000 times (as of 2024)
- Spawned numerous variants: RoBERTa, ALBERT, DistilBERT, etc.
- Became the foundation for modern NLP models
- Influenced the development of GPT series and other language models

## Translation Team
- Translator: Claude Code Session (claude/execute-prompt-full-paper-01J51SAJBVjFHPuqkE8bMzmr)
- Reviewer: TBD
- Started: 2025-11-14
- Completed: TBD

## Paper Structure
1. Introduction
2. Related Work
   - 2.1 Unsupervised Feature-based Approaches
   - 2.2 Unsupervised Fine-tuning Approaches
   - 2.3 Transfer Learning from Supervised Data
3. BERT
   - 3.1 Pre-training BERT
   - 3.2 Fine-tuning BERT
4. Experiments
   - 4.1 GLUE
   - 4.2 SQuAD v1.1
   - 4.3 SQuAD v2.0
   - 4.4 SWAG
5. Ablation Studies
   - 5.1 Effect of Pre-training Tasks
   - 5.2 Effect of Model Size
   - 5.3 Feature-based Approach with BERT
6. Conclusion
7. Appendices (optional for translation)
