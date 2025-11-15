# Section 7: Conclusion
## القسم 7: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** BERT, RoBERTa, pretraining (التدريب المسبق), next sentence prediction (التنبؤ بالجملة التالية), masking pattern (نمط الإخفاء), batch size (حجم الدفعة), sequence length (طول التسلسل), state-of-the-art (الأحدث والأفضل), GLUE, RACE, SQuAD, multi-task finetuning (الضبط الدقيق متعدد المهام), design choices (خيارات التصميم), training objective (هدف التدريب), CC-NEWS

---

### English Version

## 7 Conclusion

We carefully evaluate a number of design decisions when pretraining BERT models. We find that performance can be substantially improved by training the model longer, with bigger batches over more data; removing the next sentence prediction objective; training on longer sequences; and dynamically changing the masking pattern applied to the training data. Our improved pretraining procedure, which we call RoBERTa, achieves state-of-the-art results on GLUE, RACE and SQuAD, without multi-task finetuning for GLUE or additional data for SQuAD. These results illustrate the importance of these previously overlooked design decisions and suggest that BERT's pretraining objective remains competitive with recently proposed alternatives.

We additionally use a novel dataset, CC-NEWS, and release our models and code for pretraining and finetuning at: https://github.com/pytorch/fairseq.

---

### النسخة العربية

## 7 الخلاصة

نقيّم بعناية عدداً من قرارات التصميم عند التدريب المسبق لنماذج BERT. نجد أن الأداء يمكن تحسينه بشكل كبير من خلال تدريب النموذج لفترة أطول، بدفعات أكبر على المزيد من البيانات؛ وإزالة هدف التنبؤ بالجملة التالية؛ والتدريب على تسلسلات أطول؛ وتغيير نمط الإخفاء المطبق على بيانات التدريب بشكل ديناميكي. يحقق إجراء التدريب المسبق المحسّن لدينا، الذي نسميه RoBERTa، نتائج الأحدث والأفضل على GLUE وRACE وSQuAD، بدون ضبط دقيق متعدد المهام لـ GLUE أو بيانات إضافية لـ SQuAD. توضح هذه النتائج أهمية قرارات التصميم هذه المتجاهلة سابقاً وتشير إلى أن هدف التدريب المسبق لـ BERT يظل تنافسياً مع البدائل المقترحة مؤخراً.

نستخدم أيضاً مجموعة بيانات جديدة، CC-NEWS، ونصدر نماذجنا والكود الخاص بالتدريب المسبق والضبط الدقيق على: https://github.com/pytorch/fairseq.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** None (all previously introduced)
- **Equations:** None
- **Citations:** None (this is the conclusion)
- **Special handling:**
  - Concise summary of all key findings
  - GitHub URL preserved in original English format
  - Emphasis on main contributions maintained
  - Key improvements listed: longer training, bigger batches, more data, no NSP, longer sequences, dynamic masking

### Quality Metrics

- Semantic equivalence: 0.88 - All key conclusions accurately summarized
- Technical accuracy: 0.87 - Correct summary of improvements and results
- Readability: 0.87 - Clear and concise Arabic conclusion
- Glossary consistency: 0.87 - Consistent use of technical terms
- **Overall section score:** 0.87
