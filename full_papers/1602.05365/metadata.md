# A Specification of Open Transactional Memory for Haskell
## مواصفة ذاكرة المعاملات المفتوحة لـ Haskell

**arXiv ID:** 1602.05365
**Authors:** Marino Miculan, Marco Peressotti
**Year:** 2016
**Publication:** arXiv preprint
**Categories:** cs.PL (Programming Languages)
**DOI:** N/A
**PDF:** https://arxiv.org/pdf/1602.05365.pdf

**Abstract Translation Quality:** 0.87 (from translations/)
**Full Paper Translation Quality:** 0.867 ✅

## Abstract

### English
Transactional memory (TM) has emerged as a promising abstraction for concurrent programming alternative to lock-based synchronizations. However, most TM models admit only isolated transactions, which are not adequate in multi-threaded programming where transactions have to interact via shared data before committing. In this paper, we present Open Transactional Memory (OTM), a programming abstraction supporting safe, data-driven interactions between composable memory transactions. This is achieved by relaxing isolation between transactions, still ensuring atomicity: threads of different transactions can interact by accessing shared variables, but then their transactions have to commit together—actually, these transactions are transparently merged. This model allows for loosely-coupled interactions since transaction merging is driven only by accesses to shared data, with no need to specify participants beforehand. In this paper we provide a specification of the OTM in the setting of Concurrent Haskell, showing that it is a conservative extension of current STM abstraction. In particular, we provide a formal semantics, which allows us to prove that OTM satisfies the opacity criterion.

### العربية
ظهرت ذاكرة المعاملات (TM) كتجريد واعد للبرمجة المتزامنة بديلاً عن المزامنات المعتمدة على الأقفال. ومع ذلك، تقبل معظم نماذج TM معاملات معزولة فقط، والتي ليست كافية في البرمجة متعددة الخيوط حيث يجب أن تتفاعل المعاملات عبر البيانات المشتركة قبل الالتزام. في هذا البحث، نقدم ذاكرة المعاملات المفتوحة (OTM)، وهو تجريد برمجي يدعم التفاعلات الآمنة والمدفوعة بالبيانات بين معاملات الذاكرة القابلة للتركيب. يتحقق ذلك من خلال تخفيف العزل بين المعاملات، مع الاستمرار في ضمان الذرية: يمكن للخيوط من معاملات مختلفة التفاعل عن طريق الوصول إلى المتغيرات المشتركة، ولكن بعد ذلك يجب أن تلتزم معاملاتها معاً - في الواقع، يتم دمج هذه المعاملات بشفافية. يتيح هذا النموذج التفاعلات ضعيفة الاقتران حيث يتم دفع دمج المعاملات فقط من خلال الوصول إلى البيانات المشتركة، دون الحاجة إلى تحديد المشاركين مسبقاً. في هذا البحث نقدم مواصفة لـ OTM في إطار Concurrent Haskell، موضحين أنها امتداد محافظ لتجريد STM الحالي. بشكل خاص، نقدم دلالات رسمية تسمح لنا بإثبات أن OTM تحقق معيار العتامة.

## Citation

```bibtex
@article{miculan2016specification,
  title={A Specification of Open Transactional Memory for Haskell},
  author={Miculan, Marino and Peressotti, Marco},
  journal={arXiv preprint arXiv:1602.05365},
  year={2016}
}
```

## Paper Structure

1. **Introduction** - Motivation and overview of OTM
2. **Concurrency in Haskell** - Background on STM and concurrent programming in Haskell
3. **Composable open transactions** - Core concepts and design of OTM
4. **Formal specification of OTM** - Formal semantics and opacity proof
5. **Conclusions** - Summary and future work

## Translation Team
- Translator: Claude Sonnet 4.5 (Session 2025-11-15)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15 ✅

## Notes
This paper presents a formal specification of Open Transactional Memory (OTM) for Haskell, extending the existing Software Transactional Memory (STM) abstraction. The paper is technical and includes formal semantics, mathematical proofs, and Haskell code examples.
