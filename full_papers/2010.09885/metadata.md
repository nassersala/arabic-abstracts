# ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property Prediction
## ChemBERTa: التدريب المسبق ذاتي الإشراف واسع النطاق للتنبؤ بخصائص الجزيئات

**arXiv ID:** 2010.09885
**Authors:** Seyone Chithrananda, Gabriel Grand, Bharath Ramsundar
**Year:** 2020
**Publication:** 34th Conference on Neural Information Processing Systems (NeurIPS 2020) - Preprint
**Categories:** cs.LG, cs.CL, physics.chem-ph, q-bio.BM
**DOI:** N/A (preprint)
**PDF:** https://arxiv.org/pdf/2010.09885.pdf

**Abstract Translation Quality:** 0.92 (from translations/)
**Full Paper Translation Quality:** 0.88 ✅

## Citation

```bibtex
@article{chithrananda2020chemberta,
  title={ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property Prediction},
  author={Chithrananda, Seyone and Grand, Gabriel and Ramsundar, Bharath},
  journal={arXiv preprint arXiv:2010.09885},
  year={2020}
}
```

## Translation Team
- Translator: Claude Sonnet 4.5 (Session 2025-11-16)
- Reviewer: TBD
- Started: 2025-11-16
- Completed: 2025-11-16 ✅

## Paper Overview

This paper introduces ChemBERTa, a transformer-based model for molecular property prediction that applies BERT-style masked language modeling to SMILES strings. Key contributions include:

1. Systematic evaluation of transformers on molecular property prediction tasks
2. Analysis of pretraining dataset size effects (100K to 10M compounds)
3. Comparison of tokenization strategies (BPE vs. SMILES-specific)
4. Comparison of SMILES vs. SELFIES representations
5. Release of 77M PubChem SMILES dataset for pretraining
6. Attention visualization tools for molecular understanding

The paper demonstrates that ChemBERTa scales well with pretraining data and offers competitive performance on MoleculeNet benchmarks, though not yet state-of-the-art.
