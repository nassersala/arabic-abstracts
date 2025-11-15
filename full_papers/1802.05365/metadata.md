# Deep contextualized word representations
## تمثيلات الكلمات السياقية العميقة

**arXiv ID:** 1802.05365
**Authors:** Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer
**Year:** 2018
**Publication:** NAACL 2018
**Categories:** Computation and Language (cs.CL)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1802.05365.pdf

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** 0.89 ✅

## Citation

```bibtex
@inproceedings{peters-etal-2018-deep,
    title = "Deep Contextualized Word Representations",
    author = "Peters, Matthew E.  and
      Neumann, Mark  and
      Iyyer, Mohit  and
      Gardner, Matt  and
      Clark, Christopher  and
      Lee, Kenton  and
      Zettlemoyer, Luke",
    booktitle = "Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-1202",
    doi = "10.18653/v1/N18-1202",
    pages = "2227--2237"
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Paper Summary
This paper introduces ELMo (Embeddings from Language Models), a deep contextualized word representation that captures both syntactic and semantic information and handles polysemy. ELMo uses representations from all internal layers of a bidirectional LSTM language model (biLM) trained on a large corpus. The method significantly improves state-of-the-art results across six NLP tasks including question answering, textual entailment, and sentiment analysis.
