# Deep contextualized word representations
## تمثيلات الكلمات السياقية العميقة

**arXiv ID:** 1802.05365
**Authors:** Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer
**Year:** 2018
**Publication:** NAACL 2018 (Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers))
**Categories:** Computation and Language (cs.CL)
**PDF:** https://arxiv.org/pdf/1802.05365.pdf
**ACL Anthology:** https://aclanthology.org/N18-1202/

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** 0.90 ✅

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
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-1202",
    doi = "10.18653/v1/N18-1202",
    pages = "2227--2237"
}
```

## Paper Overview

ELMo (Embeddings from Language Models) introduced deep contextualized word representations that revolutionized NLP by modeling both complex characteristics of word use and how these uses vary across linguistic contexts. Unlike traditional word embeddings (Word2Vec, GloVe), ELMo representations are functions of the entire input sentence, allowing the same word to have different representations in different contexts.

### Key Contributions
1. Deep bidirectional language model (biLM) for contextualized representations
2. Character-based word representations to handle out-of-vocabulary words
3. Demonstrated that exposing all layers of the pre-trained model improves performance
4. Achieved state-of-the-art results on six diverse NLP tasks
5. Showed the importance of pre-training for transfer learning in NLP

### Impact
- Pioneered the era of contextualized embeddings in NLP
- Cited over 15,000 times (as of 2024)
- Influenced the development of BERT, GPT, and other transformer-based models
- Established pre-training + fine-tuning as the standard paradigm in NLP
- Open-sourced pre-trained models and code (AllenNLP)

## Translation Team
- Translator: Claude Code Session (claude/parallel-agents-full-paper-01K7engvhgwdxBz3MUjGpTnm)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15 ✅

## Paper Structure
1. Introduction
2. Related Work
3. ELMo
   - 3.1 Bidirectional language models
   - 3.2 ELMo
   - 3.3 Using biLMs for supervised NLP tasks
4. Evaluation
   - 4.1 Question Answering
   - 4.2 Textual Entailment
   - 4.3 Semantic Role Labeling
   - 4.4 Coreference Resolution
   - 4.5 Named Entity Recognition
   - 4.6 Sentiment Analysis
5. Analysis
   - 5.1 Alternate layer weighting schemes
   - 5.2 Where to include ELMo?
   - 5.3 What information is captured by the biLM's representations?
6. Conclusion
