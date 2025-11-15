# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.94
**Glossary Terms Used:** language model (نموذج لغوي), pretraining (تدريب مسبق), BERT, hyperparameter (معامل فائق), training data (بيانات التدريب), performance (أداء), replication study (دراسة تكرار), benchmark (معيار), GLUE, RACE, SQuAD, optimization (تحسين)

---

### English Version

Language model pretraining has led to significant performance gains but careful comparison between different approaches is challenging. Training is computationally expensive, often done on private datasets of different sizes, and, as we will show, hyperparameter choices have significant impact on the final results. We present a replication study of BERT pretraining (Devlin et al., 2019) that carefully measures the impact of many key hyperparameters and training data size. We find that BERT was significantly undertrained, and can match or exceed the performance of every model published after it. Our best model achieves state-of-the-art results on GLUE, RACE and SQuAD. These results highlight the importance of previously overlooked design choices, and raise questions about the source of recently reported improvements. We release our models and code.

---

### النسخة العربية

أدى التدريب المسبق لنماذج اللغة إلى مكاسب كبيرة في الأداء، لكن المقارنة الدقيقة بين المناهج المختلفة تمثل تحدياً. التدريب مكلف حسابياً، وغالباً ما يتم على مجموعات بيانات خاصة بأحجام مختلفة، وكما سنُظهر، فإن اختيارات المعاملات الفائقة لها تأثير كبير على النتائج النهائية. نقدم دراسة تكرار للتدريب المسبق لـ BERT (Devlin وآخرون، 2019) تقيس بعناية تأثير العديد من المعاملات الفائقة الرئيسية وحجم بيانات التدريب. نجد أن BERT كان يعاني من نقص كبير في التدريب، ويمكنه مطابقة أو تجاوز أداء كل نموذج نُشر بعده. يحقق نموذجنا الأفضل نتائج متقدمة على GLUE وRACE وSQuAD. تبرز هذه النتائج أهمية خيارات التصميم المتجاهلة سابقاً، وتثير تساؤلات حول مصدر التحسينات المُبلغ عنها مؤخراً. نصدر نماذجنا والكود.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** RoBERTa (implicit), BERT, pretraining, hyperparameters, masked language modeling
- **Equations:** None
- **Citations:** Devlin et al., 2019 (BERT paper)
- **Special handling:** Benchmark names (GLUE, RACE, SQuAD) kept in English as standard practice

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.94
- Readability: 0.94
- Glossary consistency: 0.93
- **Overall section score:** 0.94

This translation was completed previously in the abstracts collection and has been copied here for completeness.
